from flask import Flask, render_template, session, redirect, url_for
import sqlite3

app = Flask(__name__)
app.secret_key = 'stylehive_secret'

def get_products():
    conn = sqlite3.connect('stylehive.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, price, image FROM products")
    products = cursor.fetchall()
    conn.close()
    return products

@app.route('/')
def index():
    products = get_products()
    return render_template('index.html', products=products)

@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    if 'cart' not in session:
        session['cart'] = []
    session['cart'].append(product_id)
    return redirect(url_for('index'))

@app.route('/cart')
def cart():
    cart_items = []
    total = 0
    if 'cart' in session:
        conn = sqlite3.connect('stylehive.db')
        cursor = conn.cursor()
        for pid in session['cart']:
            cursor.execute("SELECT name, price FROM products WHERE id=?", (pid,))
            result = cursor.fetchone()
            if result:
                cart_items.append(result)
                total += result[1]
        conn.close()
    return render_template('cart.html', cart_items=cart_items, total=total)

if __name__ == '__main__':
    app.run(debug=True)
