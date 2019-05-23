import os
import gzip
import json
import sqlite3
import requests
from sys import exit
from datetime import date
from urllib import request
from shutil import copyfileobj

DIR = '.../weather'

def api_key():
    with open(os.path.join(DIR, 'app.id'), 'r') as f:
        return f.read()


def city_list_download():
    if os.path.exists(os.path.join(DIR, 'city_list.json.gz')):
        pass
    else:
        request.urlretrieve('http://bulk.openweathermap.org/sample/city.list.json.gz',
                            os.path.join(DIR, 'city_list.json.gz'))
        with gzip.open(os.path.join(DIR, 'city_list.json.gz'), 'rb') as f_out:
            with open(os.path.join(DIR, 'city_list.json'), 'wb') as f_in:
                copyfileobj(f_out, f_in)


def create_db():
    conn = sqlite3.connect(os.path.join(DIR, 'weather.db'))
    cursor = conn.cursor()

    try:
        cursor.execute("""CREATE TABLE weather
                          (id_city INTEGER PRIMARY KEY, City VARCHAR(255), date TEXT,
                          temperature TEXT, id_weather TEXT)
                       """)
    except sqlite3.OperationalError:
        pass


def city_id_list(req_city):   
    with open(os.path.join(DIR, 'city_list.json'), 'r', encoding='UTF-8') as f:
        data = json.load(f)

        city_list = []
        for city in data:
            if city['name'] == req_city:
                city_list.append([city['name'], city['country'], city['id']])
                
    id_list = []
    if len(city_list) == 0:
        print('Неверный ввод')
        exit()       
    elif len(city_list) > 1:
        country_list = []
        for city in city_list:
            if city[1] not in country_list:
                country_list.append(city[1])
        if len(country_list) > 1:
            for country in country_list:
                print(country)
            req_country = input('Уточните страну:').upper()
            for city in city_list:
                if city[1] == req_country:
                    id_list.append(city[2])
            return id_list
        else:
            for city in city_list:
                id_list.append(city[2])
            return id_list    
    else:
        id_list.append(city_list[0][2])
        return id_list


def city_available(city_id):
    conn = sqlite3.connect(os.path.join(DIR, 'weather.db'))
    cursor = conn.cursor()
    cursor.execute("SELECT id_city FROM weather")
    req = cursor.fetchall()

    for el in req:
        if city_id == el[0]:
            return True


def forecast(city_id):    
    res = requests.get('http://api.openweathermap.org/data/2.5/weather',
                       params = {'id': city_id, 'units': 'metric',
                                 'APPID': api_key()})
    res = res.json()
    return [[(res['id'], res['name'], str(date.today()),
             res['main']['temp'], res['weather'][0]['id'])],
            [res['sys']['country'], res['coord']['lon'], res['coord']['lat']]]


def db_filling(data_list):
    conn = sqlite3.connect(os.path.join(DIR, 'weather.db'))
    cursor = conn.cursor()
    cursor.executemany("INSERT INTO weather VALUES (?, ?, ?, ?, ?)", data_list[0])
    conn.commit()
    output(data_list)


def db_edit(data_list):
    conn = sqlite3.connect(os.path.join(DIR, 'weather.db'))
    cursor = conn.cursor()

    cursor.execute(f"SELECT date FROM weather WHERE id_city = {data_list[0][0][0]}")
    req = cursor.fetchall()

    if data_list[0][0][2] != req[0]:
        cursor.execute(f"""UPDATE weather SET temperature = {data_list[0][0][3]},
                       date = {data_list[0][0][2]}, id_weather = {data_list[0][0][4]}
                       WHERE id_city = {data_list[0][0][0]}""")
        conn.commit()
        output(data_list)
    elif data_list[0][0][2] == req[0]:
        cursor.execute(f"""UPDATE weather
                       SET temperature = {data_list[0][0][3]}
                       WHERE id_city = {data_list[0][0][0]}""")
        conn.commit()
        output(data_list)


def output(data_list):
    print()
    print(f'Город --------  {data_list[0][0][1]}, {data_list[1][0]}')
    print(f'Температура --  {data_list[0][0][3]} C')
    print(f'Координаты ---  [{data_list[1][1]}, {data_list[1][2]}]')
    print(f'Дата ---------  {data_list[0][0][2]}')


def main():    
    city_list_download()
    req_city = input('Введите город: ').title()
    if not os.path.exists(os.path.join(DIR, 'weather.db')):
        create_db()
    else:
        pass
    for city_id in city_id_list(req_city):
        if city_available(city_id):
            db_edit(forecast(city_id))
        else:
            db_filling(forecast(city_id))


if __name__ == '__main__':
    main()

# Города для проверки:    

# Sochi - единственный в мире
# Moscow -  город с названием в двух странах
# Bryansk - два города в одной стране
# Feodosia - неизвестный ввод
