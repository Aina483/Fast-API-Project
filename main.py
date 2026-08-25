from fastapi import FastAPI
from fastapi.responses import HTMLResponse
app = FastAPI()


users = [{
    "name" : "Aina",
    "age" : 23,
    "occupation" : "Software Engineer"
},
{
    "name" : "Armaan",
    "age" : 19,
    "occupation" : "Student"
}
]


@app.get('/')
def home():
    return {"message" : "Hello world!"}

@app.get('/user' , response_class=HTMLResponse)
def get_user():
    return f"<h1> I'm {users[0]['name']} and my age is {users[0]['age']} and I'm a {users[0]['occupation']} </h1>"



print(app.routes)