import os
import requests
from dotenv import load_dotenv
import psycopg2

load_dotenv()

API_URL = os.getenv("API_URL")

def fetch_products():
    response = requests.get(API_URL)
    return response.json()

def process_products(res_data):
    processed = []
    for product in res_data:
        product_id = product['id']
        product_name = product['name']
        product_data = product['data']
        if(isinstance(product_data, dict)):
            for key,value in product_data.items():
                processed.append({
                    'id': product_id,
                    'name': product_name,
                    'key': key,
                    'value':value
                })
        else:
            processed.append({
                'id': product_id,
                'name': product_name,
                'key': None,
                'value': None
            })
    return processed
    
def insert_into_db(processed_products):
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")
    DB_NAME = os.getenv("DB_NAME")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")

    connection = psycopg2.connect(
        host = DB_HOST,
        port = DB_PORT,
        database = DB_NAME,
        user = DB_USER,
        password = DB_PASSWORD
    )

    cursor = connection.cursor()

    for product in processed_products:
        if(product['key'] != None and product['value'] != None):
            cursor.execute("INSERT INTO products(id, name, key, value) VALUES(%s, %s, %s, %s)", (product['id'], product['name'], product['key'], product['value']))
        else:
            cursor.execute("INSERT INTO products(id, name) VALUES(%s, %s)", (product['id'], product['name']))
    
    connection.commit()
    cursor.close()
    connection.close()
    print("data successfully inserted in the db!")

if __name__ == "__main__":
    res_data = fetch_products()
    processed_products = process_products(res_data)
    insert_into_db(processed_products)