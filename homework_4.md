Module 4 Homework: Analytics Engineering with dbt

Question 3. Counting Records in fct_monthly_zone_revenue
After running your dbt project, query the fct_monthly_zone_revenue model.

What is the count of records in the fct_monthly_zone_revenue model?

SELECT count(*) FROM prod.fct_monthly_zone_revenue


Question 4. Best Performing Zone for Green Taxis (2020)
Using the fct_monthly_zone_revenue table, find the pickup zone with the highest total revenue (revenue_monthly_total_amount) for Green taxi trips in 2020.

Which zone had the highest revenue?

SELECT
    pickup_zone,
    SUM(revenue_monthly_total_amount) as total_revenue
FROM prod.fct_monthly_zone_revenue
WHERE YEAR(revenue_month) = 2020 AND service_type = 'Green'
GROUP BY 1
ORDER BY total_revenue DESC
LIMIT 1

Question 5. Green Taxi Trip Counts (October 2019)
Using the fct_monthly_zone_revenue table, what is the total number of trips (total_monthly_trips) for Green taxis in October 2019?

SELECT
    SUM(total_monthly_trips)
FROM prod.fct_monthly_zone_revenue
WHERE YEAR(revenue_month) = 2019
  AND MONTH(revenue_month) = 10
  AND service_type = 'Green'
  
Question 6. Build a Staging Model for FHV Data
Create a staging model for the For-Hire Vehicle (FHV) trip data for 2019.

Staging model:
{{ config(materialized='view') }}

select
    dispatching_base_num,
    cast(pickup_datetime as timestamp) as pickup_datetime,
    cast(dropoff_datetime as timestamp) as dropoff_datetime,
    cast(pulocationid as integer) as pickup_location_id,
    cast(dolocationid as integer) as dropoff_location_id,
    sr_flag
from {{ source('staging', 'fhv_tripdata') }}
where dispatching_base_num is not null 


What is the count of records in stg_fhv_tripdata?

SELECT count(*) FROM prod.stg_fhv_tripdata
