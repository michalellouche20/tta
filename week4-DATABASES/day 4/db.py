import psycopg2

# Establish a connecti
conn = psycopg2.connect(
    dbname='pbslqzln',
    user='pbslqzln',
    password='7uAOFI7q3RoGJ9L2-bb4FPjmyF7e55bS',
    host='lucky.db.elephantsql.com',
    port='5432'
)

# Create a cursur object to execute SQL queries
cur = conn.cursor()

# CRUD  - Create (insert) Read (select) Update (update) Delete (delete)

# Insert query
# insert_query = 'INSERT INTO products (name, price) VALUES (%s, %s)'
# data_to_insert = ('iKey', 750)
# # cur.execute(insert_query, data_to_insert)
# cur.execute('INSERT INTO products (name, price) VALUES (%s, %s)', ('iKey', 750))



# Update query
# update_query = 'UPDATE products SET name=%s, price=%s WHERE id= %s'
# new_value = ('iCar2024', 9999, 8)
# cur.execute(update_query, new_value)

# Delete query
cur.execute('DELETE FROM products WHERE id=%s', ('8'))

# Commit the transaction
conn.commit()



# Execute a SELECT query
cur.execute('SELECT * FROM products')
rows = cur.fetchall()

for row in rows:
    print(row)


# Close the cursur and the connection
cur.close()
conn.close()



# Managing a Simple User Database

# Scenario:
# You're building a basic user management system that interacts with a PostgreSQL database. 
# Users should be able to:

# View all existing users.
# Add a new user.
# Update a user's information.
# Delete a user.

# Tasks:
# Database Setup:

# Create a PostgreSQL database named user_management.
# Inside the database, create a table named users with columns: 
# id (integer, primary key), username (varchar), email (varchar), and age (integer).

# Python Script:

# Write a Python script that connects to the user_management database.
# Implement functions to perform the following operations:
# View all users from the users table.
# Add a new user to the users table.
# Update a user's information based on their id.
# Delete a user from the users table based on their id.

# User Interaction:

# Create a simple command-line interface (CLI) to interact with your Python functions.
# The CLI should provide options to view, add, update, or delete users, 
# and take appropriate inputs from the user to perform these actions.

# Testing:

# Test your Python script by adding users, viewing all users, 
# updating user information, and deleting users.

import psycopg2
import os
from dotenv import load_dotenv

# Load variables from the .env file into the connect
load_dotenv()

# Retrieve database crendetials from env 

# db_name = os.getenv('DB_NAME')
# db_user = os.getenv('DB_USER')
# db_password = os.getenv('DB_PASS')
# db_host = os.getenv('DB_HOST')
# db_port = os.getenv('DB_PORT')

# Establish a connection
conn = psycopg2.connect(
    dbname=os.getenv('DB_NAME'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASS'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT')
)

# Create a cursur object to execute SQL queries
cur = conn.cursor()

# CRUD  - Create (insert) Read (select) Update (update) Delete (delete)

# Insert query
# insert_query = 'INSERT INTO products (name, price) VALUES (%s, %s)'
# data_to_insert = ('iKey', 750)
# # cur.execute(insert_query, data_to_insert)
# cur.execute('INSERT INTO products (name, price) VALUES (%s, %s)', ('iKey', 750))



# Update query
# update_query = 'UPDATE products SET name=%s, price=%s WHERE id= %s'
# new_value = ('iCar2024', 9999, 8)
# cur.execute(update_query, new_value)

# Delete query
# cur.execute('DELETE FROM products WHERE id=%s', ('5'))


# Commit the transaction
# conn.rollback()



# Execute a SELECT query
cur.execute('SELECT * FROM products')
rows = cur.fetchall()

for row in rows:
    print(row)


# Close the cursur and the connection
cur.close()
conn.close()