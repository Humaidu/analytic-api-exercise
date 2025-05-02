from fastapi import APIRouter, Depends
from app.database import get_session
from app.models import Customer, Order, OrderItem, Product
from sqlmodel import Session, select
from typing import List
from sqlalchemy import text

 

router = APIRouter()

# FastAPI Routes
# @router.get("/customers", response_model=List[Customer])
# def get_customers(session: Session = Depends(get_session)):
#     return session.exec(select(Customer)).all()

# @router.get("/products", response_model=List[Product])
# def get_products(session: Session = Depends(get_session)):
#     return session.exec(select(Product)).all()

# @router.get("/customers/{customer_id}/orders", response_model=List[Order])
# def get_customer_orders(customer_id: int, session: Session = Depends(get_session)):
#     return session.exec(select(Order).where(Order.customer_id == customer_id)).all()

# @router.get("/order-items", response_model=List[OrderItem])
# def get_order_items(session: Session = Depends(get_session)):
#     return session.exec(select(OrderItem)).all()

@router.get("/analytics/top-customers", summary="Top Customers by Spending", description="Returns the top 5 customers ranked by total spending on orders.", response_model=List[dict])
def get_top_customers(session: Session = Depends(get_session)):
    query = """
        SELECT c.customer_id, c.name, SUM(oi.quantity * oi.unit_price) AS total_spent
        FROM customers c
        JOIN orders o ON c.customer_id = o.customer_id
        JOIN order_items oi ON o.order_id = oi.order_id
        GROUP BY c.customer_id, c.name
        ORDER BY total_spent DESC
        LIMIT 5;
    """
    results = session.exec(text(query)).mappings().all()
    return results


@router.get("/analytics/monthly-sales", summary="Monthly Sales Report", description="Shows monthly sales totals for only 'Shipped' or 'Delivered' orders.", response_model=List[dict])
def get_monthly_sales(session: Session = Depends(get_session)):
    query = """
        SELECT 
            DATE_FORMAT(o.order_date, '%Y-%m') AS month,
            SUM(oi.quantity * oi.unit_price) AS total_sales
        FROM orders o
        JOIN order_items oi ON o.order_id = oi.order_id
        WHERE o.status IN ('Shipped', 'Delivered')
        GROUP BY month
        ORDER BY month;
    """
    results = session.exec(text(query)).mappings().all()
    return results


@router.get("/analytics/unsold-products", summary="Products Never Ordered", description="Lists products that have never been included in any order.", response_model=List[dict])
def get_unsold_products(session: Session = Depends(get_session)):
    query = """
        SELECT p.product_id, p.name
        FROM products p
        LEFT JOIN order_items oi ON p.product_id = oi.product_id
        WHERE oi.product_id IS NULL;
    """
    results = session.exec(text(query)).mappings().all()
    return results


@router.get("/analytics/average-order-value", summary="Average Order Value by Country", description="Calculates the average order value grouped by customer country.", response_model=List[dict])
def get_avg_order_value_by_country(session: Session = Depends(get_session)):
    query = """
        SELECT order_totals.country, AVG(order_totals.order_total) AS avg_order_value
        FROM (
            SELECT o.order_id, c.customer_id, c.country, 
                   SUM(oi.quantity * oi.unit_price) AS order_total
            FROM customers c
            JOIN orders o ON c.customer_id = o.customer_id
            JOIN order_items oi ON o.order_id = oi.order_id
            GROUP BY o.order_id, c.customer_id, c.country
        ) AS order_totals
        GROUP BY order_totals.country;
    """
    results = session.exec(text(query)).mappings().all()
    return results


@router.get("/analytics/frequent-buyers", summary="Frequent Buyers", description="Lists customers who have placed more than one order.", response_model=List[dict])
def get_frequent_buyers(session: Session = Depends(get_session)):
    query = """
        SELECT c.customer_id, c.name, COUNT(o.order_id) AS total_orders
        FROM customers c
        JOIN orders o ON c.customer_id = o.customer_id
        GROUP BY c.customer_id, c.name
        HAVING total_orders > 1
        ORDER BY total_orders DESC;
    """
    results = session.exec(text(query)).mappings().all()
    # return [dict(row) for row in results]
    return results
