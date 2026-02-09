Creat bucket and load the data:
<img width="1723" height="691" alt="image" src="https://github.com/user-attachments/assets/16c6b6a7-258f-4c91-9016-12904c962601" />


Create the External Table from GCS:
de-zoomcamp-ny-yellow-taxi-set-sun-2026/*.parquet


Question 1. <img width="1675" height="527" alt="image" src="https://github.com/user-attachments/assets/193d5bce-75db-4020-a037-9fabdebddf4c" />
Question 2. Correct answer - 0 MB for the External Table and 155.12 MB for the Materialized Table
0 Mb for the Materialized Table is is not possible
18.82 MB for the External Table and 47.60 MB for the Materialized Table - too small

Question 4. 
<img width="1622" height="497" alt="image" src="https://github.com/user-attachments/assets/dc791b88-7b13-4a5f-b6e2-43212c47827e" />

Question 5.
CREATE OR REPLACE TABLE zoomcamp.yellow_taxi_partitioned
PARTITION BY DATE(tpep_dropoff_datetime)
CLUSTER BY VendorID AS
SELECT *
FROM zoomcamp.yellow_taxi_external;

Question 6.

<img width="1644" height="542" alt="image" src="https://github.com/user-attachments/assets/447ad238-3d8c-491f-bbb2-994c1077bec4" />
<img width="1712" height="586" alt="image" src="https://github.com/user-attachments/assets/54a41aa0-1bed-41c7-88f9-f68f0841be0b" />


