import duckdb
import pandas as pd

con = duckdb.connect('taxi.db')

con.execute("""
CREATE TABLE green_taxi AS
SELECT * FROM 'green_tripdata_2025-11.parquet'
""")

con.execute("""
CREATE TABLE zones AS
SELECT * FROM read_csv_auto('taxi_zone_lookup.csv')
""")

# Task 3: Counting short trips
def task3_total_trips():
    df = con.execute("""
    SELECT COUNT(*) AS total_tips_less_one_mile
    FROM green_taxi
    WHERE lpep_pickup_datetime >= '2025-11-01' AND lpep_pickup_datetime < '2025-12-01'
        AND trip_distance <= 1
    """).fetchdf()
    print("Task 4 — Counting short trips")
    print(df.head())

# task3_total_trips()

# Task 4: Longest trip for each day
def task4_longest_trips():
    df = con.execute("""
    SELECT lpep_pickup_datetime
    FROM green_taxi
    WHERE trip_distance =
        (SELECT MAX(trip_distance) AS total_tips_less_one_mile
        FROM green_taxi
        WHERE trip_distance <= 100)
    """).fetchdf()
    print("Task 4 — Longest trip for each day")
    print(df.head())

# task4_longest_trips()

# Task 5: Biggest pickup zone
def task5_biggest_pickup_zpne():
    df = con.execute("""
    SELECT zones.Zone,
           SUM(total_amount) AS total_amount
    FROM green_taxi
        INNER JOIN zones ON green_taxi.PULocationID = zones.LocationID
    WHERE DATE(lpep_pickup_datetime) = DATE('2025-11-18')
    GROUP BY 1
    ORDER BY total_amount DESC
    """).fetchdf()
    print("Task 5 — Biggest pickup zone")
    print(df.head())

task5_biggest_pickup_zpne()

# Task 6: Largest tip
def task6_biggest_pickup_zone():
    df = con.execute("""
    SELECT zones.Zone
    FROM green_taxi
        INNER JOIN zones ON green_taxi.DOLocationID = zones.LocationID
    WHERE DATE(lpep_pickup_datetime) BETWEEN DATE('2025-11-01') AND DATE('2025-11-30')
        AND tip_amount = 
            (SELECT MAX(tip_amount) AS max_tip_amount
            FROM green_taxi
                INNER JOIN zones ON green_taxi.PULocationID = zones.LocationID
            WHERE zones.Zone = 'East Harlem North' AND DATE(lpep_pickup_datetime) BETWEEN DATE('2025-11-01') AND DATE('2025-11-30'))
    """).fetchdf()
    print("Task 6 — Largest tip")
    print(df.head())

task6_biggest_pickup_zone()





