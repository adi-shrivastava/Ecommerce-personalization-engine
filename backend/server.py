from fastapi import FastAPI
app=FastAPI()
@app.get("/")
def home():
    return{"message": "Hello World"}
@app.get("/recommend")
def recommend():
    return{"message": "This is the recommendation endpoint"}