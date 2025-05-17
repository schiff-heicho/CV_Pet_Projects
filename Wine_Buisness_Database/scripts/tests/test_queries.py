import pytest
import mysql.connector
from mysql.connector import Error

# Конфигурация тестовой БД
TEST_DB_CONFIG = {
    'host': 'localhost',
    'user': 'test_user',
    'password': 'test_password',
    'database': 'wine_db_test'
}

@pytest.fixture(scope='module')
def db_connection():
    """Фикстура для подключения к тестовой БД"""
    conn = None
    try:
        conn = mysql.connector.connect(**TEST_DB_CONFIG)
        yield conn
    finally:
        if conn:
            conn.close()

@pytest.fixture(scope='module', autouse=True)
def setup_test_database(db_connection):
    """Инициализация тестовых данных"""
    cursor = db_connection.cursor()
    
    # Выполнение DDL и DML скриптов
    with open('ddl.sql', 'r') as f:
        ddl_script = f.read()
    for statement in ddl_script.split(';'):
        if statement.strip():
            cursor.execute(statement)
    
    with open('dml.sql', 'r') as f:
        dml_script = f.read()
    for statement in dml_script.split(';'):
        if statement.strip():
            cursor.execute(statement)
    
    db_connection.commit()
    cursor.close()

def test_top5_expensive_wines(db_connection):
    """Тест для запроса топ-5 дорогих вин с рейтингом >9.0"""
    cursor = db_connection.cursor()
    cursor.execute("""
        SELECT name, price, rating 
        FROM wines 
        WHERE rating > 9.0 
        ORDER BY price DESC 
        LIMIT 5
    """)
    result = cursor.fetchall()
    
    assert len(result) == 5
    assert all(float(row[2]) > 9.0 for row in result)
    assert result == sorted(result, key=lambda x: x[1], reverse=True)

def test_avg_price_by_country(db_connection):
    """Тест средней цены по странам"""
    cursor = db_connection.cursor(dictionary=True)
    cursor.execute("""
        SELECT wr.country, AVG(w.price) AS avg_price
        FROM wines w
        JOIN wine_regions wr ON w.region_id = wr.region_id
        GROUP BY wr.country
    """)
    result = cursor.fetchall()
    
    assert len(result) > 5  # В данных есть >5 стран
    assert all(isinstance(row['avg_price'], float) for row in result)

def test_price_history_for_wine(db_connection):
    """Тест истории изменения цен"""
    cursor = db_connection.cursor()
    cursor.execute("""
        SELECT wine_id, price, start_date
        FROM wine_price_history
        WHERE wine_id = 1
    """)
    result = cursor.fetchall()
    
    assert len(result) >= 2  # В данных есть минимум 2 изменения
    assert result[0][1] != result[1][1]  # Цены должны различаться

def test_most_popular_wine_types(db_connection):
    """Тест популярности типов вин"""
    cursor = db_connection.cursor()
    cursor.execute("""
        SELECT w.type, COUNT(od.quantity) AS total_sold
        FROM wines w
        RIGHT JOIN order_details od ON w.wine_id = od.wine_id
        GROUP BY w.type
    """)
    result = cursor.fetchall()
    
    types = [row[0] for row in result]
    assert all(t in ['красное', 'белое', 'роза', 'игристое'] for t in types)

def test_high_rated_regions(db_connection):
    """Тест регионов с высоким рейтингом"""
    cursor = db_connection.cursor()
    cursor.execute("""
        SELECT wr.region_name, AVG(w.rating) AS avg_rating
        FROM wines w
        JOIN wine_regions wr ON w.region_id = wr.region_id
        GROUP BY wr.region_name
        HAVING AVG(w.rating) > 8.5
    """)
    result = cursor.fetchall()
    
    assert len(result) > 0
    assert all(float(row[1]) > 8.5 for row in result)

def test_loyalty_customers_total(db_connection):
    """Тест клиентов с картой лояльности"""
    cursor = db_connection.cursor()
    cursor.execute("""
        SELECT c.first_name, SUM(od.quantity * w.price) AS total_spent
        FROM customers c
        JOIN orders o ON c.customer_id = o.customer_id
        JOIN order_details od ON o.order_id = od.order_id
        JOIN wines w ON od.wine_id = w.wine_id
        WHERE c.loyalty_card = TRUE
        GROUP BY c.customer_id
    """)
    result = cursor.fetchall()
    
    assert len(result) > 10  # В данных есть >10 лояльных клиентов
    assert all(row[1] > 0 for row in result)

def test_vintage_years_analysis(db_connection):
    """Тест анализа винтажных годов"""
    cursor = db_connection.cursor()
    cursor.execute("""
        SELECT production_year, AVG(rating) AS avg_rating
        FROM wines
        GROUP BY production_year
    """)
    result = cursor.fetchall()
    
    assert 2015 in [row[0] for row in result]  # Проверка наличия тестовых данных

def test_monthly_sales_stats(db_connection):
    """Тест месячной статистики"""
    cursor = db_connection.cursor()
    cursor.execute("""
        SELECT DATE_FORMAT(order_date, '%%Y-%%m') AS month
        FROM orders
        GROUP BY month
    """)
    result = cursor.fetchall()
    
    assert len(result) >= 3  # В данных есть минимум 3 месяца

def test_top5_popular_wines(db_connection):
    """Тест топ-5 популярных вин"""
    cursor = db_connection.cursor()
    cursor.execute("""
        SELECT name, COUNT(od.order_id) AS order_count
        FROM wines w
        JOIN order_details od ON w.wine_id = od.wine_id
        GROUP BY w.wine_id
        ORDER BY order_count DESC
        LIMIT 5
    """)
    result = cursor.fetchall()
    
    assert len(result) == 5
    assert all(row[1] > 0 for row in result)

def test_loyalty_penetration(db_connection):
    """Тест проникновения лояльности"""
    cursor = db_connection.cursor()
    cursor.execute("""
        SELECT city, COUNT(*) AS total_customers
        FROM customers
        GROUP BY city
    """)
    result = cursor.fetchall()
    
    assert any(row[1] > 5 for row in result)  # Проверка условия HAVING

# Для генерации отчета о покрытии:
# pytest --cov=your_module --cov-report=html tests/
