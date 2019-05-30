import os
import csv
import sys
import json
import sqlite3

DIR = '.../weather'

def export_json(file_name = None, city_name = None):
    json_lst = list()
    keys = ['city id', 'city name', 'date', 'temperature', 'weather id']

    conn = sqlite3.connect(os.path.join(DIR, 'weather.db'))
    cursor = conn.cursor()

    if city_name == None:
        cursor.execute("SELECT * FROM weather")
        rows = cursor.fetchall()
        for row in rows:
            data = {x: y for x, y in zip(keys, row)}
            json_lst.append(data)
    else:
        cursor.execute("SELECT City, id_city FROM weather")
        names = cursor.fetchall()
        id_lst = list()
        for name in names:
            if name[0] == f'{city_name}':
                id_lst.append(name[1])
        for city in id_lst:
            cursor.execute(f"SELECT * FROM weather WHERE id_city={city}")
            rows = cursor.fetchall()
            for row in rows:
                data = {x: y for x, y in zip(keys, row)}
                json_lst.append(data)
        if id_lst == []:
            print(f'Города "{city_name}" нет в базе')

    with open(os.path.join(DIR, file_name + '.json'), 'a', encoding='UTF-8') as f:
        json.dump(json_lst, f)


def export_csv(file_name = None, city_name = None):
    keys = ['city id', 'city name', 'date', 'temperature', 'weather id']

    conn = sqlite3.connect(os.path.join(DIR, 'weather.db'))
    cursor = conn.cursor()

    if city_name == None:
        cursor.execute("SELECT * FROM weather")
        rows = cursor.fetchall()
        with open(os.path.join(DIR, file_name + '.csv'), 'a', encoding='UTF-8', newline='') as f:
            writer = csv.writer(f, delimiter=';')
            for row in rows:
                for csv_line in zip(keys, row):
                    writer.writerow(csv_line)
    else:
        cursor.execute("SELECT City, id_city FROM weather")
        names = cursor.fetchall()
        id_lst = list()
        for name in names:
            if name[0] == f'{city_name}':
                id_lst.append(name[1])
        for city in id_lst:
            cursor.execute(f"SELECT * FROM weather WHERE id_city={city}")
            rows = cursor.fetchall()
            with open(os.path.join(DIR, file_name + '.csv'), 'a', encoding='UTF-8', newline='') as f:
                writer = csv.writer(f, delimiter=';')
                for row in rows:
                    for csv_line in zip(keys, row):
                        writer.writerow(csv_line)
        if id_lst == []:
            print(f'Города "{city_name}" нет в базе')


def icon(weather_id):
    group1 = [300, 301, 302, 310, 311, 312, 313, 314, 321, 520, 521, 522, 531]
    group2 = [500, 501, 502, 503, 504]
    group3 = [200, 201, 202, 210, 211, 212, 221, 230, 231, 232]
    group4 = [511, 600, 601, 602, 611, 612, 613, 615, 616, 620, 621, 622]
    group5 = [701, 711, 721, 731, 741, 751, 761, 762, 771, 781]
    group6 = [800]
    group7 = [801]
    group8 = [802]
    group9 = [803, 804]
    if int(weather_id) in group1:
        return '9d'
    elif int(weather_id) in group2:
        return '10d'
    elif int(weather_id) in group3:
        return '11d'
    elif int(weather_id) in group4:
        return '13d'
    elif int(weather_id) in group5:
        return '50d'
    elif int(weather_id) in group6:
        return '01d'
    elif int(weather_id) in group7:
        return '02d'
    elif int(weather_id) in group8:
        return '03d'
    elif int(weather_id) in group9:
        return '04d'


def export_html(file_name = None, city_name = None):
    conn = sqlite3.connect(os.path.join(DIR, 'weather.db'))
    cursor = conn.cursor()

    if city_name == None:
        cursor.execute("SELECT * FROM weather")
        rows = cursor.fetchall()

        with open(os.path.join(DIR, file_name + '.html'), 'a', encoding='UTF-8') as f:
            for row in rows:
                html_tag = f"""
                            <html>
                            <head>
                            <title> Weather {row[1]} </title>
                            </head>
                            <body>
                            <div style="font-size: medium; font-weight: bold">{row[1]}</div>
                            <div>{row[3]} C</div>
                            <div>{row[2]}</div>
                            <div>
                            <img height="45" width="45" style="border: medium none; width: 45px; height: 45px;
                            background: url(&quot;http://openweathermap.org/img/w/{icon(row[4])}.png&quot;)
                            repeat scroll 0% 0% transparent;
                            " alt="title" src="http://openweathermap.org/images/transparent.png"/>
                            </div>
                            </body>
                            </html>
                            """
                f.write(html_tag)
    else:
        cursor.execute("SELECT City, id_city FROM weather")
        names = cursor.fetchall()
        id_lst = list()
        for name in names:
            if name[0] == f'{city_name}':
                id_lst.append(name[1])
        for city in id_lst:
            cursor.execute(f"SELECT * FROM weather WHERE id_city={city}")
            rows = cursor.fetchall()
            for row in rows:
                with open(os.path.join(DIR, file_name + '.html'), 'a', encoding='UTF-8') as f:
                    html_tag = f"""
                                <html>
                                <head>
                                <title> Weather {row[1]} </title>
                                </head>
                                <body>
                                <div style="font-size: medium; font-weight: bold">{row[1]}</div>
                                <div>{row[3]} C</div>
                                <div>{row[2]}</div>
                                <div>
                                <img height="45" width="45" style="border: medium none; width: 45px; height: 45px;
                                background: url(&quot;http://openweathermap.org/img/w/{icon(row[4])}.png&quot;)
                                repeat scroll 0% 0% transparent;
                                " alt="title" src="http://openweathermap.org/images/transparent.png"/>
                                </div>
                                </body>
                                </html>
                                """
                    f.write(html_tag)
        if id_lst == []:
            print(f'Города "{city_name}" нет в базе')


def main():
    if len(sys.argv) == 1:
        print('Задайте "--help" для получения справки')
    elif len(sys.argv) == 2:
        form = sys.argv[1]
        if form == '--help':
            print("""
Экспорт базы в формате csv: "--csv filename" Oдин город: "--csv filename <город>"
Экспорт базы в формате json: "--json filename" Oдин город: "--json filename <город>"
Экспорт базы в формате html: "--html filename" Oдин город: "--html filename <город>"
                    """)
        else:
            print('Задан неверный аргумент. Задайте "--help" для получения справки')
    elif len(sys.argv) > 2 and len(sys.argv) <= 4:
        form = sys.argv[1]
        file_name = sys.argv[2]
        if form == '--csv':
            if len(sys.argv) == 4:
                city_name = sys.argv[3].title()
                export_csv(file_name, city_name)
            else:
                export_csv(file_name)
        elif form == '--json':
            if len(sys.argv) == 4:
                city_name = sys.argv[3].title()
                export_json(file_name, city_name)
            else:
                export_json(file_name)
        elif form == '--html':
            if len(sys.argv) == 4:
                city_name = sys.argv[3].title()
                export_html(file_name, city_name)
            else:
                export_html(file_name)
        else:
            print('Задан неверный аргумент. Задайте "--help" для получения справки')


if __name__ == '__main__':
    main()