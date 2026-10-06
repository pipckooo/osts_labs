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

sql_timestamp = '''with randomized as (
    select 
        record_id,
        timestamp '2025-01-01 00:00:00' 
            + (timestamp '2025-12-31 23:59:59' - timestamp '2025-01-01 00:00:00') * random() as new_ts
    from traffic_accident_records
)
update traffic_accident_records t
set 
    timestamp   = r.new_ts,
    record_date = r.new_ts::date,
    hour        = extract(hour from r.new_ts)::smallint,
    month       = extract(month from r.new_ts)::smallint,
    day_of_week = to_char(r.new_ts, 'FMDay'),
    time_of_day = case 
        when extract(hour from r.new_ts) between 5 and 11 then 'Morning'
        when extract(hour from r.new_ts) between 12 and 16 then 'Afternoon'
        when extract(hour from r.new_ts) between 17 and 20 then 'Evening'
        else 'Night'
    end
from randomized r
where t.record_id = r.record_id;  ''';

cursor.execute(sql_timestamp)
print("Timestamps has been updated successfully !!");


conn.close()