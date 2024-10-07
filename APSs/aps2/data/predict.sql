DROP TABLE IF EXISTS sales_analytics.scoring_ml_pedroatp;

create table sales_analytics.scoring_ml_pedroatp as 
WITH temp AS (
    WITH last_dates AS (
        SELECT 
            store_id,
            MAX(date_sale) AS last_day
        FROM
            sales.item_sale
        GROUP BY 
            store_id
    )
    SELECT
        store_id,
        last_day + i AS new_date
    FROM
        last_dates,
        GENERATE_SERIES(1, 8) AS i
)
SELECT 
    store_id,
    EXTRACT(YEAR FROM new_date) AS year,
    EXTRACT(MONTH FROM new_date) AS month,
    EXTRACT(DAY FROM new_date) AS day,
    EXTRACT(ISODOW FROM new_date) AS weekday,
    NULL::FLOAT AS total_sales
FROM temp;
 
