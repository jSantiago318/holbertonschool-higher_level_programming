#!/usr/bin/python3
"""Flask app displaying product data from JSON, CSV, or a SQLite database."""
import csv
import json
import sqlite3

from flask import Flask, render_template, request

app = Flask(__name__)


def read_json(filename):
    """Read and return the list of products stored in a JSON file."""
    with open(filename, 'r') as file:
        return json.load(file)


def read_csv(filename):
    """Read and return the list of products stored in a CSV file."""
    products = []
    with open(filename, 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            products.append({
                'id': int(row['id']),
                'name': row['name'],
                'category': row['category'],
                'price': float(row['price'])
            })
    return products


def read_sql(filename):
    """Read and return the list of products stored in a SQLite database."""
    conn = sqlite3.connect(filename)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, category, price FROM Products')
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]


@app.route('/products')
def products():
    """Display products read from a JSON, CSV, or SQLite source.

    Query parameters:
        source: ``json``, ``csv`` or ``sql`` (required).
        id: optional product id used to filter the results.
    """
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source == 'json':
        data = read_json('products.json')
    elif source == 'csv':
        data = read_csv('products.csv')
    elif source == 'sql':
        try:
            data = read_sql('products.db')
        except sqlite3.Error as error:
            return render_template('product_display.html', error=str(error))
    else:
        return render_template('product_display.html', error='Wrong source')

    if product_id is not None:
        try:
            target_id = int(product_id)
        except ValueError:
            target_id = None
        data = [product for product in data if product['id'] == target_id]
        if not data:
            return render_template('product_display.html',
                                   error='Product not found')

    return render_template('product_display.html', products=data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
