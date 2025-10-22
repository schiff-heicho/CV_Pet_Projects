-- Хранимые процедуры и функции для базы данных виннного <ВинТех>

-- 1. Процедура оформления заказа
CREATE OR REPLACE PROCEDURE process_order(
    customer_id INT,
    location_id INT,
    wine_id INT,
    quantity INT
)
LANGUAGE plpgsql
AS $$
DECLARE
    current_stock INT;
    new_order_id INT;
BEGIN
    -- Проверка наличия товара
    SELECT inventory.quantity INTO current_stock 
    FROM inventory 
    WHERE inventory.wine_id = process_order.wine_id 
      AND inventory.location_id = process_order.location_id;

    IF current_stock >= quantity THEN
        -- Создание заказа
        INSERT INTO orders (customer_id, order_date, order_type, location_id, status)
        VALUES (process_order.customer_id, NOW(), 'offline', process_order.location_id, 'processing')
        RETURNING order_id INTO new_order_id;

        -- Добавление деталей заказа
        INSERT INTO order_details (order_id, wine_id, quantity)
        VALUES (new_order_id, process_order.wine_id, process_order.quantity);

    ELSE
        RAISE EXCEPTION 'Недостаточно товара на складе';
    END IF;
END;
$$;

-- 2. Функция расчета статуса лояльности
CREATE OR REPLACE FUNCTION calculate_loyalty_status(
    customer_id INT
) 
RETURNS VARCHAR(20)
LANGUAGE plpgsql
STABLE
AS $$
DECLARE
    total_spent DECIMAL(12,2);
BEGIN
    SELECT SUM(od.quantity * w.price) INTO total_spent
    FROM orders o
    JOIN order_details od ON o.order_id = od.order_id
    JOIN wines w ON od.wine_id = w.wine_id
    WHERE o.customer_id = calculate_loyalty_status.customer_id;

    RETURN CASE
        WHEN total_spent > 50000 THEN 'VIP'
        WHEN total_spent BETWEEN 20000 AND 50000 THEN 'Premium'
        ELSE 'Standard'
    END;
END;
$$;

-- 3. Функция проверки остатков
CREATE OR REPLACE FUNCTION get_available_quantity(
    target_wine_id INT,
    target_location_id INT
) 
RETURNS INT
LANGUAGE plpgsql
STABLE
AS $$
DECLARE
    stock INT;
BEGIN
    SELECT quantity INTO stock 
    FROM inventory 
    WHERE wine_id = target_wine_id 
      AND location_id = target_location_id;

    RETURN COALESCE(stock, 0);
END;
$$;
