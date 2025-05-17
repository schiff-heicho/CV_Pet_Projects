-- Представление "Топ-10 самых популярных вин по продажам"
CREATE VIEW top_selling_wines AS
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


-- Представление "Клиенты с VIP-статусом"
CREATE VIEW vip_customers AS
SELECT
    c.customer_id,
    CONCAT(c.first_name, ' ', c.last_name) AS customer_name,
    c.email,
    c.city,
    COUNT(o.order_id) AS total_orders,
    SUM(od.quantity * w.price) AS total_spent
FROM
    customers c
JOIN
    orders o ON c.customer_id = o.customer_id
JOIN
    order_details od ON o.order_id = od.order_id
JOIN
    wines w ON od.wine_id = w.wine_id
WHERE
    c.loyalty_card = TRUE
GROUP BY
    c.customer_id, customer_name, c.email, c.city
HAVING
    SUM(od.quantity * w.price) > 10000
ORDER BY
    total_spent DESC;


-- Представление "Региональные продажи по странам"
CREATE VIEW regional_sales AS
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
