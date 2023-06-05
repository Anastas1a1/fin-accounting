from multiprocessing.sharedctypes import Value
import sqlite3
import requests


def new_transaction(us_id, transaction):
    fname = 'database/' + str(us_id) + '.db'
    db = sqlite3.connect(fname)
    sql = db.cursor()

    # data['name'],
    # data['cur'],
    # data['sum'],
    # data['rate'],
    # data['note']

    sql.execute("""CREATE TABLE IF NOT EXISTS users (
        us_name TEXT,
        summa FLOAT,
        currency TEXT,
        rate FLOAT,
        fee total FLOAT,
        note TEXT
        )""")
    db.commit()
    
    sql.execute("INSERT INTO users VALUES(?, ?, ?, ?, ?, ?);", transaction)
    db.commit()  
    
    sql.execute("SELECT * FROM users;")
    all_results = sql.fetchall()
    print(all_results)  
    # = dict(sorted(cond.items(), key = lambda item: item[1]))
    
    
def parse_rate(rate):
    try:
        data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
        print (data['Valute'][rate]['Value'])  
        return data['Valute'][rate]['Value']
    except:   
        print("No currency rate")
        return 0      
    
# parse_rate('EUR')
transaction = ('Nastya', 123, 'RUB', 1, 123, '')
new_transaction(123456, transaction)