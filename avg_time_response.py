# -- Source - https://stackoverflow.com/a/22965061
# -- Posted by pozs, modified by community. See post 'Timeline' for change history
# -- Retrieved 2026-09-16, License - CC BY-SA 4.0

# select timestamp '2014-01-10 20:00:00' +
#        random() * (timestamp '2014-01-20 20:00:00' -
#                    timestamp '2014-01-10 10:00:00')


import psycopg2

conn = psycopg2.connect(
    database="traffic_db",
    user='postgres',
    password='pass',
    host='localhost',
    port= '5432'
)

conn.autocommit = True

cursor = conn.cursor()

sql_timestamp = '''select avg(actual_response_time_min) from traffic_accident_records where actual_response_time_min!=0;''';

cursor.execute(sql_timestamp)
query_result = cursor.fetchall()
print("Average actual response time :" ,  query_result[0][0]);


sql_timestamp = '''select avg(baseline_expected_response_time_min) from traffic_accident_records where baseline_expected_response_time_min!=0;''';


cursor.execute(sql_timestamp)
query_result = cursor.fetchall()
print("Average expected response time :" ,  query_result[0][0]);

conn.close()