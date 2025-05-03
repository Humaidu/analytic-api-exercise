from sqlmodel import Field, SQLModel

# Define Models (SQLAlchemy + SQLModel) for your tables
class Customer(SQLModel, table=True):
    __tablename__ = "customers"

    customer_id: int = Field(primary_key=True)
    name: str
    email: str
    country: str

class Product(SQLModel, table=True):
    __tablename__ = "products"

    product_id: int = Field(primary_key=True)
    name: str
    category: str
    price: float

class Order(SQLModel, table=True):
    __tablename__ = "orders"

    order_id: int = Field(primary_key=True)
    customer_id: int
    order_date: str
    status: str

class OrderItem(SQLModel, table=True):
    __tablename__ = "order_items"

    order_item_id: int = Field(primary_key=True)
    order_id: int
    product_id: int
    quantity: int
    unit_price: float
