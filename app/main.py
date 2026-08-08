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

