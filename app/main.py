from fastapi import FastAPI, Path
from enum import Enum

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello, FastAPI!"}

@app.get("/about")
def about():
    return {
    "name": "Your Name",
    "role": "Backend Developer Student"
}

@app.get("/contact")
def contact():
    return {"email": "neeraj@gmail.com"}

# @app.get("/users/{user_id}")
# def get_user(user_id: int = Path(gt=0)):
#     return {
#         "user_id": user_id
#         }

# @app.get("/products/{product_id}")
# def get_product(product_id:int):
#     return {"Product ID": product_id}

# @app.get("/students/{student_id}/courses/{course_name}")
# def student_info(student_id: int, course_name: str):
#     return {
#         "Student ID": student_id,
#         "Course Name": course_name
#     }


# @app.get("/users")
# def search_users(name: str):
#     return {
#         "search_name": name
#     }

# @app.get("/products")
# def products(search: str | None = None):
#     return {
#         "search": search
#     }

# @app.get("/students")
# def students(page: int = 1, limit: int = 10):
#     return {
#         "page": page,
#         "limit": limit
#     }

# @app.get("/products")
# def product_list(
#     search: str | None = None,
#     category: str | None = None,
#     page: int = 1,
#     limit: int = 10
# ):
#     return {
#         "search": search,
#         "category": category,
#         "page": page,
#         "limit": limit
#     }

# @app.get("/users/{username}")
# def get_user(
#     username:str = Path(min_length=3, max_length=20)
# ):
#     return {
#         "username":username
#     }



# @app.get("/products/{price}")
# def get_product(price: float):
#     return {
#         "price": price
#     }

# @app.get("/status/{active}")
# def status(active: bool):
#     return {
#         "active": active
#     } 

# @app.get("/users/{user_id}/orders/{order_id}")
# def get_order(user_id: int, order_id: int):
#     return {
#         "user_id": user_id,
#         "order_id": order_id
#     }

# @app.get("/users/{user_id}")
# def get_user(user_id: int = Path(
#     title= "Users",
#     gt=0,
#     description= "User Id Must be an integer"
# )):
#     return {
#         "user_id": user_id
#     }

# @app.get("/products/{product_id}")
# def get_product(product_id: int = Path(
#     gt=1,
#     lt=100000,
#     title= "Products",
#     description= "Product Id Must be an Integer"
# )):
#     return {
#         "product_id": product_id
#     }



# @app.get("/username/{username}")
# def get_username(username: str = Path(
#     min_length=3,
#     max_length=20,
#     title= "Username",
#     description= "Username Must be string"
# )):
#     return {
#         "username": username
#     }

# @app.get("/users/{user_id}/orders/{order_id}")
# def get_user_order(
#     user_id: int = Path(gt=0, title= "User ID"),
#     order_id: int = Path(gt=0, title="Order ID"),
# ):
#     return {
#         "user_id": user_id,
#         "order_id": order_id
#     }

# "Enum Usage"

# class UserRole(str, Enum):
#     admin= "admin"
#     manager = "manager"
#     customer = "customer"

# @app.get("/users/role/{role}")
# def get_user_role(
#     role: UserRole = Path(
#         title= "Role",
#         description= "User Role"
#     )
# ):
#     return {
#         "role": role
#     }

# class PaymentStatus(str, Enum):
#     pending = "pending"
#     paid = "paid"
#     failed = "failed"
#     refunded = "refunded"

# @app.get("/payments/{status}")
# def payment_status(
#     status: PaymentStatus = Path(
#         title= "Payment Status",
#         description= "Current Payment Status"
#     )
# ):
#     return {
#         "payment_status": status
#     }

from uuid import UUID

@app.get("/users/{user_id}")
def get_user(user_id: UUID):
    return {
        "user_id": user_id
    }


@app.get("/orders/{order_id}")
def get_user_order(order_id: UUID = Path(
    title="Order ID",
    description="Unique UUID of the order"
)):
    return {
        "order_id": order_id
    }

