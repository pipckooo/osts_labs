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

sql = ''' create table if not exists traffic_accident_records (
    record_id varchar(64) ,
    timestamp timestamp ,
    record_date date,
    hour integer ,
    month integer ,
    day_of_week varchar(15),
    time_of_day varchar(20),
    is_holiday boolean,

    area_type varchar(50),
    road_type varchar(50),
    intersection_type varchar(50),
    speed_limit_kmh integer,
    weather varchar(50),
    road_condition varchar(50),
    visibility_m numeric(8, 2),
    congestion_index numeric(5, 2),

    
    vehicle_type varchar(50),
    driver_age numeric(4, 1),
    driver_experience_yrs numeric(4, 1),
    vehicle_age_yrs numeric(4, 1),
    recorded_speed_kmh numeric(5, 2),

    
    baseline_expected_response_time_min numeric(6, 2),
    accident_occurred boolean ,
    collision_type varchar(50),
    vehicles_involved integer,
    accident_severity varchar(50),
    dispatch_priority varchar(20),
    actual_response_time_min numeric(6, 2),
    road_closure_duration_min numeric(7, 2)
); ''';

cursor.execute(sql)
print("Table has been created successfully !!");

conn.close()