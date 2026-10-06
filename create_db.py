import psycopg2

conn = psycopg2.connect(
   database="postgres",
    user='postgres',
    password='pass',
    host='localhost',
    port= '5432'
)

conn.autocommit = True

cursor = conn.cursor()

sql = ''' CREATE database traffic_db ''';

cursor.execute(sql)
print("Database has been created successfully !!");

conn.close()