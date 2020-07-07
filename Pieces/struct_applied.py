import pymysql
from faker import Faker
import random

def getData(rec):
    data = []
    id = range(1, rec+1)
    fake = Faker(locale='zh_CN')
    for i in id:
        data.append((
            i,
            random.randint(0, rec),
            fake.name(),
            fake.phone_number(),
            fake.ssn()
        ))
    return data

def insert_by_msyql(table):
    conn = pymysql.connect(host='localhost', user='root', password='', db='struct', charset='utf8mb4')
    cur = conn.cursor()
    try:
        sql = 'INSERT INTO pkg1 VALUES(%s,%s,%s,%s,%s)'
        cur.executemany(sql, table)
        conn.commit()
        print('[insert_by_mysql executemany] total:', len(table))
    except Exception as e:
        print('Error in [insert_by_mysql]:', e)
        conn.rollback()

def main():
    table = getData(10)
    print(table)
    insert_by_msyql(table)

if __name__ == '__main__':
    main()