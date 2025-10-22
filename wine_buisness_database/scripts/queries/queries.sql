-- Топ-5 самых дорогих вин с рейтингом выше 9.0 (WHERE, ORDER BY, LIMIT)
SELECT name, price, rating 
FROM wines 
WHERE rating > 9.0 
ORDER BY price DESC 
LIMIT 5;

-- Средняя цена вин по странам
SELECT wr.country, AVG(w.price) AS avg_price
FROM wines w
JOIN wine_regions wr ON w.region_id = wr.region_id
GROUP BY wr.country
ORDER BY avg_price DESC;

-- История изменения цен для конкретного вина
SELECT
    wine_id,
    price,
    start_date,
    LAG(price) OVER (ORDER BY start_date) AS prev_price,
    price - LAG(price) OVER (ORDER BY start_date) AS price_diff
FROM wine_price_history
WHERE wine_id = 1;

-- Самые популярные типы вин
SELECT w.type, COUNT(od.quantity) AS total_sold
FROM wines w
RIGHT JOIN order_details od ON w.wine_id = od.wine_id
GROUP BY w.type
ORDER BY total_sold DESC;

-- Винные регионы с самым высоким средним рейтингом
SELECT wr.region_name, AVG(w.rating) AS avg_rating
FROM wines w
JOIN wine_regions wr ON w.region_id = wr.region_id
GROUP BY wr.region_name
HAVING AVG(w.rating) > 8.5
ORDER BY avg_rating DESC;

-- Клиенты с картой лояльности и их общая сумма покупок
SELECT c.first_name, c.last_name, SUM(od.quantity * w.price) AS total_spent
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN order_details od ON o.order_id = od.order_id
JOIN wines w ON od.wine_id = w.wine_id
WHERE c.loyalty_card = TRUE
GROUP BY c.customer_id
ORDER BY total_spent DESC;

-- Лучшие винтажные года по среднему рейтингу
SELECT production_year, AVG(rating) AS avg_rating
FROM wines
WHERE production_year IN (
    SELECT DISTINCT production_year 
    FROM wines 
    WHERE rating > 9.0
)
GROUP BY production_year
ORDER BY avg_rating DESC;

-- Месячная статистика продаж и выручки
SELECT
    TO_CHAR(o.order_date, 'YYYY-MM') AS month,
    COUNT(DISTINCT o.order_id) AS orders_count,
    SUM(od.quantity) AS bottles_sold,
    SUM(od.quantity * w.price) AS revenue
FROM orders o
JOIN order_details od ON o.order_id = od.order_id
JOIN wines w ON od.wine_id = w.wine_id
GROUP BY TO_CHAR(o.order_date, 'YYYY-MM')
ORDER BY month;

-- Топ-5 самые популярные вина по количеству заказов
SELECT name, order_count FROM (
    SELECT
        w.name,
        COUNT(od.order_id) AS order_count,
        RANK() OVER (ORDER BY COUNT(od.order_id) DESC) AS popularity_rank
    FROM wines w
    JOIN order_details od ON w.wine_id = od.wine_id
    GROUP BY w.wine_id
) AS ranked_wines
WHERE popularity_rank <= 5;

-- Анализ клиентской активности: Проникновение программы лояльности по городам
SELECT
    city,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN loyalty_card = TRUE THEN 1 ELSE 0 END) AS loyalty_members,
    ROUND(SUM(CASE WHEN loyalty_card = TRUE THEN 1 ELSE 0 END) / COUNT(*) * 100, 2) AS loyalty_percentage
FROM customers
GROUP BY city
ORDER BY loyalty_percentage DESC;

-- Анализ выполнения заказов: Статистика по статусам заказов и времени обработки
SELECT 
    status,
    COUNT(*) AS orders_count,
    ROUND(COUNT(*) / (SELECT COUNT(*) FROM orders) * 100, 2) AS percentage,
    AVG(EXTRACT(EPOCH FROM (CURRENT_TIMESTAMP - order_date)) / 3600) AS avg_hours_pending
FROM orders
GROUP BY status;