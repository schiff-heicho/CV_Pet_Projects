-- Индекс для ускорения поиска текущих цен
CREATE INDEX idx_current_prices ON wine_price_history(wine_id, is_current)
WHERE is_current = TRUE;

-- Составной индекс для инвентаризации
CREATE INDEX idx_inventory_search ON inventory(location_id, wine_id, quantity);

-- Индекс для поиска клиентов по географии
CREATE INDEX idx_customer_geo ON customers(city, loyalty_card);
