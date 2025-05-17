import psycopg2
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()
conn = psycopg2.connect(
    dbname="winetech_db",
    user="admin",
    password="secret",
    host="localhost"
)
cursor = conn.cursor()

# Генерация регионов
regions = [
    ('Бордо', 'Франция'), ('Тоскана', 'Италия'), 
    ('Рибера-дель-Дуэро', 'Испания'), ('Напа', 'США')
]
for region in regions:
    cursor.execute(
        "INSERT INTO regions (name, country) VALUES (%s, %s)",
        region
    )

# Генерация сортов винограда
varietals = ['Каберне Совиньон', 'Мерло', 'Шардоне', 'Совиньон Блан', 'Пино Нуар']
for grape in varietals:
    cursor.execute("INSERT INTO grape_varieties (name) VALUES (%s)", (grape,))

# Генерация вин (200 позиций)
cursor.execute("SELECT id FROM regions")
region_ids = [row[0] for row in cursor.fetchall()]

cursor.execute("SELECT id FROM grape_varieties")
grape_ids = [row[0] for row in cursor.fetchall()]

for _ in range(200):
    wine_name = f"{fake.word().capitalize()} {fake.word().capitalize()}"
    vintage = random.randint(2010, 2022)
    price = round(random.uniform(15, 250), 2)
    region_id = random.choice(region_ids)
    grape_id = random.choice(grape_ids)
    
    cursor.execute(
        """INSERT INTO wines 
        (name, vintage, price, region_id, grape_id) 
        VALUES (%s, %s, %s, %s, %s)""",
        (wine_name, vintage, price, region_id, grape_id)
    )

# Генерация продаж (5000 транзакций)
cursor.execute("SELECT id FROM wines")
wine_ids = [row[0] for row in cursor.fetchall()]

for _ in range(5000):
    wine_id = random.choice(wine_ids)
    quantity = random.randint(1, 12)
    sale_date = fake.date_between(start_date='-2y', end_date='today')
    customer_id = random.randint(1, 1000)  # Предполагаем существование таблицы customers
    
    cursor.execute(
        """INSERT INTO sales 
        (wine_id, quantity, sale_date, customer_id) 
        VALUES (%s, %s, %s, %s)""",
        (wine_id, quantity, sale_date, customer_id)
    )

conn.commit()
cursor.close()
conn.close()
