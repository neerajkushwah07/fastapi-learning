from fastapi import FastAPI

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

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"User ID": user_id}

@app.get("/products/{product_id}")
def get_product(product_id:int):
    return {"Product ID": product_id}

@app.get("/students/{student_id}/courses/{course_name}")
def student_info(student_id: int, course_name: str):
    return {
        "Student ID": student_id,
        "Course Name": course_name
    }


@app.get("/users")
def search_users(name: str):
    return {
        "search_name": name
    }

@app.get("/products")
def products(search: str | None = None):
    return {
        "search": search
    }

@app.get("/students")
def students(page: int = 1, limit: int = 10):
    return {
        "page": page,
        "limit": limit
    }

@app.get("/products")
def product_list(
    search: str | None = None,
    category: str | None = None,
    page: int = 1,
    limit: int = 10
):
    return {
        "search": search,
        "category": category,
        "page": page,
        "limit": limit
    }