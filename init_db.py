import sqlite3

conn = sqlite3.connect('stylehive.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS products (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT,
  price INTEGER,
  image TEXT
)''')

products = [
    ("Floral Dress", 1199, "https://via.placeholder.com/300x220?text=Floral+Dress"),
    ("High Heels", 1599, "https://via.placeholder.com/300x220?text=High+Heels"),
    ("Stylish Sunglasses", 699, "https://via.placeholder.com/300x220?text=Sunglasses"),
    ("Trendy Handbag", 1399, "https://via.placeholder.com/300x220?text=Handbag")
]

cursor.executemany("INSERT INTO products (name, price, image) VALUES (?, ?, ?)", products)
conn.commit()
conn.close()

print("Database initialized and filled!")
