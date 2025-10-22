-- Представление "Топ-10 самых популярных вин по продажам"
CREATE OR REPLACE VIEW top_selling_wines AS
SELECT 
    w.wine_id,
    w.name,
    w.type,
    SUM(od.quantity) AS total_sold,
    SUM(od.quantity * w.price) AS total_revenue
FROM 
    wines w
JOIN 
    order_details od ON w.wine_id = od.wine_id
GROUP BY 
    w.wine_id, w.name, w.type
ORDER BY 
    total_sold DESC
LIMIT 10;

-- Представление "Региональные продажи по странам"
CREATE OR REPLACE VIEW regional_sales AS
SELECT
    wr.country,
    COUNT(DISTINCT o.order_id) AS orders_count,
    SUM(od.quantity) AS bottles_sold,
    SUM(od.quantity * w.price) AS revenue,
    AVG(w.rating) AS avg_rating
FROM
    wines w
JOIN
    wine_regions wr ON w.region_id = wr.region_id
JOIN
    order_details od ON w.wine_id = od.wine_id
JOIN
    orders o ON od.order_id = o.order_id
GROUP BY
    wr.country
ORDER BY
    revenue DESC;
