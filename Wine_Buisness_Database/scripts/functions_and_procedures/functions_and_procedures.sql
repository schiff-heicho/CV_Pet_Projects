-- Хранимые процедуры и функции для базы данных виннного <ВинТех>

DELIMITER $$

-- 1. Процедура оформления заказа
CREATE PROCEDURE process_order(
    IN customer_id INT,
    IN location_id INT,
    IN wine_id INT,
    IN quantity INT
)
BEGIN
    DECLARE current_stock INT;
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        RESIGNAL;
    END;

    START TRANSACTION;

    -- Проверка наличия товара
    SELECT inventory.quantity INTO current_stock 
    FROM inventory 
    WHERE inventory.wine_id = wine_id 
      AND inventory.location_id = location_id;

    IF current_stock >= quantity THEN
        -- Создание заказа
        INSERT INTO orders (customer_id, order_date, order_type, location_id, status)
        VALUES (customer_id, NOW(), 'offline', location_id, 'processing');

        -- Добавление деталей заказа
        INSERT INTO order_details (order_id, wine_id, quantity)
        VALUES (LAST_INSERT_ID(), wine_id, quantity);

        -- Обновление инвентаря
        UPDATE inventory 
        SET quantity = quantity - quantity
        WHERE wine_id = wine_id 
          AND location_id = location_id;

        COMMIT;
    ELSE
        ROLLBACK;
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Недостаточно товара на складе';
    END IF;
END$$

-- 2. Процедура обновления цены
CREATE PROCEDURE update_wine_price(
    IN p_wine_id INT,
    IN new_price DECIMAL(10,2)
BEGIN
    START TRANSACTION;
    
    -- Деактивация старой цены
    UPDATE wine_price_history 
    SET end_date = CURDATE(), 
        is_current = FALSE 
    WHERE wine_id = p_wine_id 
      AND is_current = TRUE;

    -- Добавление новой цены
    INSERT INTO wine_price_history (wine_id, start_date, price, is_current)
    VALUES (p_wine_id, CURDATE(), new_price, TRUE);

    -- Обновление основной таблицы
    UPDATE wines 
    SET price = new_price 
    WHERE wine_id = p_wine_id;

    COMMIT;
END$$

-- 3. Функция расчета статуса лояльности
CREATE FUNCTION calculate_loyalty_status(
    customer_id INT
) 
RETURNS VARCHAR(20)
DETERMINISTIC
BEGIN
    DECLARE total_spent DECIMAL(12,2);
    
    SELECT SUM(od.quantity * w.price) INTO total_spent
    FROM orders o
    JOIN order_details od ON o.order_id = od.order_id
    JOIN wines w ON od.wine_id = w.wine_id
    WHERE o.customer_id = customer_id;

    RETURN CASE
        WHEN total_spent > 50000 THEN 'VIP'
        WHEN total_spent BETWEEN 20000 AND 50000 THEN 'Premium'
        ELSE 'Standard'
    END;
END$$

-- 4. Функция проверки остатков
CREATE FUNCTION get_available_quantity(
    target_wine_id INT,
    target_location_id INT
) 
RETURNS INT
DETERMINISTIC
BEGIN
    DECLARE stock INT;
    
    SELECT quantity INTO stock 
    FROM inventory 
    WHERE wine_id = target_wine_id 
      AND location_id = target_location_id;

    RETURN IFNULL(stock, 0);
END$$

DELIMITER ;
