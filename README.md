# 📦 Analytics API

This project is a **FastAPI-based REST API** that performs **analytical queries** on an RDS MySQL database. It provides endpoints to help analyze customer behavior, product trends, and order data.

Designed with clarity and maintainability in mind, the API follows good practices in structure and modularization.

Here is the schema for the database


### Using AWS RDS create a simple mysql database with the following SQL commands:

```
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

### Queries to execute:
• Top Customers by Spending
• Monthly Sales Report (Only Shipped/Delivered)
• Products Never Ordered
• Average Order Value by Country
• Frequent Buyers (More Than One Order)
Hint: These are complex queries.

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
```
---

## ⚙️ Tech Stack

- **FastAPI** – High-performance web framework  
- **SQLModel** – SQLAlchemy + Pydantic ORM layer  
- **MySQL** – Relational database backend (local or AWS RDS)  
- **Uvicorn** – ASGI server  

---

## 🌐 API Documentation

Once the application is running, you can access the interactive documentation:

- [Swagger UI](http://34.247.79.34/docs) – `/docs`
- [ReDoc UI](http://34.247.79.34/docs) – `/redoc`

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

---

## Setting Up AWS RDS (MySQL) and Deploying FastAPI to EC2

### Set Up AWS RDS (MySQL)
*Step 1: Create RDS Database*
- Go to the RDS Console → Create Database → Choose MySQL
- Set DB identifier and master credentials
- Choose `db.t3.micro` for Free Tier eligibility
- Under Connectivity:
    - Enable Public access = Yes (or configure private VPC properly)
    - Add a new Security Group with the following rule:
        - *Type*: MySQL/Aurora
        - *Protocol*: TCP
        - *Port*: 3306
        - *Source*: Custom / EC2 Group

*Step 2: Connect to RDS and Populate DB*
- Once created, get the RDS endpoint and connect using MySQL Workbench or CLI
- Run `sql/schema.sql` and `sql/seed_data.sql` to populate the DB

### Test RDS Database Connection
After deploying or before running the FastAPI app, you can test your RDS MySQL connection directly from your EC2 instance to ensure the database is reachable.

*Use the MySQL CLI (Recommended for Simple Tests)*

*Step 1: Install MySQL Client*
Install MySQL client (if not already installed):
```
sudo apt install mysql-client -y

```

*Step 2: Connect to RDS Instance*
Connect to your RDS instance:
```
mysql -h <rds-endpoint> -u <username> -p

```
When prompted, enter your RDS password.

*Step 3: Test the Connection*
Once inside the MySQL shell, test it:
```
SHOW DATABASES;
USE <your-db-name>;
SHOW TABLES;

```
This will help you verify that your RDS instance is reachable and that your database is set up correctly.

### Deploy FastAPI to EC2

*Step 1: Launch EC2 Instance*
- Launch an EC2 Ubuntu Instance
- SSH into it:
 ```
ssh -i your-key.pem ubuntu@<your-ec2-ip>

 ```

*Step 2: Install Requirements*
- Install requirements:
```
sudo apt update
sudo apt install -y python3-pip python3-venv git
git clone https://github.com/your-username/ecommerce_api.git
cd ecommerce_api
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt

```

*Step 3: Update DATABASE_URL*
- Update the `DATABASE_URL` in `app/database.py` with your RDS endpoint:
```
DATABASE_URL = "mysql+mysqlconnector://<username>:<password>@<rds-endpoint>:3306/<db_name>"
```

*Step 4: Run the API*
- Run the API:
```
uvicorn app.main:app --host 0.0.0.0 --port 80

```

*Step 5: Configure EC2 Security Group*
- In EC2 Security Group, add:
    - *Inbound Rule*:
        - *Type*: HTTP
        - *Port*: 80
        - *Source*: 0.0.0.0/0

*Step 6: Access Your API*
- Access your API:
```
http://<your-ec2-ip>/docs

```
---

## 🔧 Production Deployment (EC2 + Nginx + systemd)

### Create a `systemd` Service

Create a service file at `/etc/systemd/system/fastapi.service`:

```ini
[Unit]
Description=FastAPI application with Uvicorn
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/analytic-api-exercise
Environment="PATH=/home/ubuntu/analytic-api-exercise/env/bin"
ExecStart=/home/ubuntu/analytic-api-exercise/env/bin/uvicorn app.main:app --host 0.0.0.0 --port 8000

Restart=always

[Install]
WantedBy=multi-user.target

*Then run:*
```
sudo systemctl daemon-reload
sudo systemctl enable fastapi
sudo systemctl start fastapi
sudo systemctl status fastapi

```

### Configure Nginx as a Reverse Proxy

Install Nginx:
```
sudo apt update
sudo apt install nginx

```

Create a config file for your app at /etc/nginx/sites-available/fastapi:
```
server {
    listen 80;
    server_name your_domain_or_ip;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}

```

Enable the config:
```
sudo ln -s /etc/nginx/sites-available/fastapi /etc/nginx/sites-enabled
sudo nginx -t
sudo systemctl restart nginx

```
Now your FastAPI app should be served publicly on port 80 via Nginx.



