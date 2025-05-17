DROP TABLE IF EXISTS wine_regions;
CREATE TABLE wine_regions (
    region_id INT PRIMARY KEY AUTO_INCREMENT,
    region_name VARCHAR(128) NOT NULL UNIQUE,
    subregion_name VARCHAR(128) NOT NULL,
    country VARCHAR(64) NOT NULL,
    climate VARCHAR(64) NOT NULL
);

DROP TABLE IF EXISTS wines;
CREATE TABLE wines (
    wine_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(128) NOT NULL,
    region_id INT REFERENCES wine_regions(region_id),
    production_year YEAR NOT NULL,
    type ENUM('красное', 'белое', 'роза', 'игристое') NOT NULL,
    price DECIMAL(10, 2) NOT NULL CHECK (price > 0),
    rating DECIMAL(3, 1) CHECK (rating BETWEEN 0 AND 10)
);

DROP TABLE IF EXISTS wine_price_history;
CREATE TABLE wine_price_history (
    price_history_id INT PRIMARY KEY AUTO_INCREMENT,
    wine_id INT REFERENCES wines(wine_id),
    start_date DATE NOT NULL,
    end_date DATE CHECK (end_date > start_date),
    price DECIMAL(10, 2) NOT NULL CHECK (price > 0),
    is_current BOOLEAN DEFAULT TRUE
);

DROP TABLE IF EXISTS locations;
CREATE TABLE locations (
    location_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(128) NOT NULL,
    country VARCHAR(64) NOT NULL,
    city VARCHAR(64) NOT NULL,
    address VARCHAR(128) NOT NULL,
    type ENUM('online', 'offline') NOT NULL
);

DROP TABLE IF EXISTS customers;
CREATE TABLE customers (
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(64) NOT NULL,
    last_name VARCHAR(64) NOT NULL,
    email VARCHAR(64) UNIQUE NOT NULL,
    city VARCHAR(64) NOT NULL,
    loyalty_card BOOLEAN DEFAULT FALSE
);

DROP TABLE IF EXISTS inventory;
CREATE TABLE inventory (
    -- inventory_id INT PRIMARY KEY AUTO_INCREMENT,
    wine_id INT REFERENCES wines(wines_id),
    location_id INT REFERENCES locations(location_id),
    quantity INT NOT NULL CHECK (quantity >= 0),
    last_delivery_date DATE NOT NULL,

    PRIMARY KEY(wine_id, location_id)
);

DROP TABLE IF EXISTS orders;
CREATE TABLE orders (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT REFERENCES customers(customer_id),
    order_date DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
    order_type ENUM('online', 'offline') NOT NULL,
    location_id INT REFERENCES locations(location_id),
    status ENUM('completed', 'processing') DEFAULT 'processing' NOT NULL,
);

DROP TABLE IF EXISTS order_details;
CREATE TABLE order_details (
    order_details_id INT PRIMARY KEY AUTO_INCREMENT,
    order_id INT REFERENCES orders(order_id),
    wine_id INT REFERENCES wines(wine_id),
    quantity INT NOT NULL CHECK (quantity > 0),
);
