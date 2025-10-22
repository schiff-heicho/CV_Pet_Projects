-- Триггер для обновления инвентаря после оформления заказа
CREATE OR REPLACE FUNCTION update_inventory_after_order()
RETURNS TRIGGER AS $$
BEGIN
    -- Уменьшаем количество вина на складе при оформлении заказа
    UPDATE inventory
    SET quantity = quantity - NEW.quantity
    WHERE wine_id = NEW.wine_id 
      AND location_id = (SELECT location_id FROM orders WHERE order_id = NEW.order_id);
    
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_inventory_trigger
AFTER INSERT ON order_details
FOR EACH ROW
EXECUTE FUNCTION update_inventory_after_order();

-- Триггер для автоматического обновления статуса лояльности клиента
CREATE OR REPLACE FUNCTION update_loyalty_status()
RETURNS TRIGGER AS $$
DECLARE
    total_spent DECIMAL(12,2);
BEGIN
    -- Рассчитываем общую сумму покупок клиента
    SELECT SUM(od.quantity * w.price) INTO total_spent
    FROM orders o
    JOIN order_details od ON o.order_id = od.order_id
    JOIN wines w ON od.wine_id = w.wine_id
    WHERE o.customer_id = NEW.customer_id;
    
    -- Обновляем статус карты лояльности
    IF total_spent > 20000 THEN
        UPDATE customers
        SET loyalty_card = TRUE
        WHERE customer_id = NEW.customer_id;
    END IF;
    
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE TRIGGER update_loyalty_status_trigger
AFTER INSERT ON orders
FOR EACH ROW
EXECUTE FUNCTION update_loyalty_status();

-- Триггер для логирования изменений цен
CREATE OR REPLACE FUNCTION log_price_changes()
RETURNS TRIGGER AS $$
BEGIN
    -- Если цена изменилась, добавляем запись в историю
    IF NEW.price <> OLD.price THEN
        -- Деактивируем старую запись о цене
        UPDATE wine_price_history
        SET end_date = CURRENT_DATE,
            is_current = FALSE
        WHERE wine_id = NEW.wine_id AND is_current = TRUE;
        
        -- Добавляем новую запись
        INSERT INTO wine_price_history (wine_id, start_date, price, is_current)
        VALUES (NEW.wine_id, CURRENT_DATE, NEW.price, TRUE);
    END IF;
    
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER log_price_changes_trigger
AFTER UPDATE OF price ON wines
FOR EACH ROW
EXECUTE FUNCTION log_price_changes();
