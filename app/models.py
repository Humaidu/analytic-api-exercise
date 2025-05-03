from sqlmodel import Field, SQLModel

# Defining Models (SQLAlchemy + SQLModel) for my tables

# Customer Table: Stores customer information such as name, email, and country.
class Customer(SQLModel, table=True):
    __tablename__ = "customers"

    customer_id: int = Field(primary_key=True)
    name: str
    email: str
    country: str


# Product Table: Contains information about products available for purchase.
class Product(SQLModel, table=True):
    __tablename__ = "products"

    product_id: int = Field(primary_key=True)
    name: str
    category: str
    price: float


# Order Table: Tracks individual orders placed by customers.
class Order(SQLModel, table=True):
    __tablename__ = "orders"

    order_id: int = Field(primary_key=True)
    customer_id: int
    order_date: str
    status: str


# OrderItem Table: Represents items within a specific order (an order can have multiple items).
class OrderItem(SQLModel, table=True):
    __tablename__ = "order_items"

    order_item_id: int = Field(primary_key=True)
    order_id: int
    product_id: int
    quantity: int
    unit_price: float
