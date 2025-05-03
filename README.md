# 📦 E-commerce Analytics API

This project is a **FastAPI-based REST API** that performs **analytical queries** on an RDS MySQL database. It provides endpoints to help analyze customer behavior, product trends, and order data.

Designed with clarity and maintainability in mind, the API follows good practices in structure and modularization.

Here is the schema for the database

```
Using AWS RDS create a simple mysql database with the following SQL commands:

-- Drop tables if they exist
DROP TABLE IF EXISTS order_items;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS customers;

-- Customers table
CREATE TABLE customers (
customer_id INT PRIMARY KEY,
name VARCHAR(100) NOT NULL,
email VARCHAR(100) UNIQUE NOT NULL,
country VARCHAR(50)
);

-- Products table
CREATE TABLE products (
product_id INT PRIMARY KEY,
name VARCHAR(100) NOT NULL,
category VARCHAR(50),
price DECIMAL(10,2)
);

-- Orders table
CREATE TABLE orders (
order_id INT PRIMARY KEY,
customer_id INT,
order_date DATE,
status VARCHAR(20),
FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- Order Items table
CREATE TABLE order_items (
order_item_id INT PRIMARY KEY,
order_id INT,
product_id INT,
quantity INT,
unit_price DECIMAL(10,2),
FOREIGN KEY (order_id) REFERENCES orders(order_id),
FOREIGN KEY (product_id) REFERENCES products(product_id)
);

Insert data into your database using the following script:

-- Customers
INSERT INTO customers VALUES
(1, 'Alice Smith', 'alice@example.com', 'USA'),
(2, 'Bob Jones', 'bob@example.com', 'Canada'),
(3, 'Charlie Zhang', 'charlie@example.com', 'UK');

-- Products
INSERT INTO products VALUES
(1, 'Laptop', 'Electronics', 1200.00),
(2, 'Smartphone', 'Electronics', 800.00),
(3, 'Desk Chair', 'Furniture', 150.00),
(4, 'Coffee Maker', 'Appliances', 85.50);'

-- Orders
INSERT INTO orders VALUES
(1, 1, '2023-11-15', 'Shipped'),
(2, 2, '2023-11-20', 'Pending'),
(3, 1, '2023-12-01', 'Delivered'),
(4, 3, '2023-12-03', 'Cancelled');

-- Order Items
INSERT INTO order_items VALUES
(1, 1, 1, 1, 1200.00), -- Laptop
(2, 1, 4, 2, 85.50), -- Coffee Maker
(3, 2, 2, 1, 800.00), -- Smartphone
(4, 3, 3, 2, 150.00), -- Desk Chair
(5, 4, 1, 1, 1200.00); -- Laptop

```
---

## 🧰 Features

This API supports:

- ✅ Listing customers and products
- 💰 Identifying top customers by spending
- 📈 Monthly sales report (filtered by shipped/delivered status)
- 📦 Products that have never been ordered
- 🌍 Average order value by customer country
- 🔁 Finding customers with multiple orders (frequent buyers)

---

## 📁 Project Structure

```plaintext
ecommerce_api/
│
├── app/
│   ├── __init__.py
│   ├── main.py               # FastAPI app instance and startup logic
│   ├── database.py           # SQLModel database engine and session
│   ├── models.py             # ORM models using SQLModel
│   └── routers/
│       └── queries.py        # Endpoints (simple + analytical queries)
│
├── requirements.txt          # Project dependencies
└── README.md                 # Project documentation

---

## ⚙️ Tech Stack

- **FastAPI** – High-performance web framework  
- **SQLModel** – SQLAlchemy + Pydantic ORM layer  
- **MySQL** – Relational database backend (local or AWS RDS)  
- **Uvicorn** – ASGI server  

---

## 🌐 API Documentation

Once the application is running, you can access the interactive documentation:

- [Swagger UI](http://127.0.0.1:8000/docs) – `/docs`
- [ReDoc UI](http://127.0.0.1:8000/redoc) – `/redoc`

---

## 📊 Analytical Endpoints

These endpoints provide insights and reports from the database:

| Endpoint                             | Description                                               |
|--------------------------------------|-----------------------------------------------------------|
| `/analytics/top-customers`          | List top customers by total spending                     |
| `/analytics/monthly-sales`          | Sales totals by month (shipped/delivered orders only)    |
| `/analytics/products-never-ordered` | Products with no associated orders                       |
| `/analytics/average-order-value`    | Average order value grouped by customer country          |
| `/analytics/frequent-buyers`        | Customers with more than one order                       |


