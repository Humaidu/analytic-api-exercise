## 📊 API Documentation — Analytics Endpoints

Base URL: [http://34.247.79.34](http://34.247.79.34)  
Swagger Docs: [http://34.247.79.34/docs](http://34.247.79.34/docs)

---

### 🔝 Top Customers by Spending
**GET** `/analytics/top-customers`  
Returns a list of customers who have spent the most on orders.

**Example Response:**
```json
[
  {
    "customer_id": 1,
    "name": "Alice Smith",
    "total_spent": 2371.00
  },
  ...
]
```

---

### Monthly Sales Report (Shipped/Delivered Orders Only)
**GET** `/analytics/monthly-sales`  
Provides total sales grouped by month, excluding cancelled/pending orders.

**Example Response:**
```json
[
  {
    "month": "2023-11",
    "total_sales": 1371
  },
  {
    "month": "2023-12",
    "total_sales": 300
  }
]
```
---

### Products Never Ordered
**GET** `/analytics/unsold-products`  
Lists all products that have never appeared in any order.

**Example Response:**
```json
[]
```

---

### Average Order Value by Country
**GET** `/analytics/average-order-value`  
Returns the average total value of each customer's order grouped by country.

**Example Response:**
```json
[
  {
    "country": "USA",
    "avg_order_value": 835.5
  },
  {
    "country": "Canada",
    "avg_order_value": 800
  },
  {
    "country": "UK",
    "avg_order_value": 1200
  }
]
```

---

### Frequent Buyers (More Than One Order)
**GET** `/analytics/frequent-buyers`  
Returns customers who have placed more than one order.

**Example Response:**
```json
[
  {
    "customer_id": 1,
    "name": "Alice Smith",
    "total_orders": 2
  }
]
```

---
