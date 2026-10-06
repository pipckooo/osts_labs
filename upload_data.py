import pandas as pd
import psycopg2
conn = psycopg2.connect(
    database="traffic_db",
    user='postgres',
    password='pass',
    host='localhost',
    port= '5432'
)
csv_dir = "/home/oleh/.cache/kagglehub/datasets/razanihababdellatif/emergency-dispatch-and-traffic-physics-dataset/versions/1/synthetic_traffic_benchmark_200k.csv"

# Source - https://stackoverflow.com/a/58380448
# Posted by Blaine McMahon, modified by community. See post 'Timeline' for change history
# Retrieved 2026-09-16, License - CC BY-SA 4.0



cur = conn.cursor()


with open(csv_dir, 'r') as f:
    next(f)  
    cur.copy_from(f, 'traffic_accident_records', sep=',',null='')  

conn.commit()


