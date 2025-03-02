from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Mock data storage
users = {
    2: {
        "id": 2,
        "email": "janet.weaver@reqres.in",
        "first_name": "Janet",
        "last_name": "Weaver",
        "avatar": "https://reqres.in/img/faces/2-image.jpg"
    },
    3: {
        "id": 3,
        "email": "janet2.weaver@reqres.in",
        "first_name": "Janet2",
        "last_name": "Weaver2",
        "avatar": "https://reqres2.in/img/faces/2-image.jpg"
    }
}


class User(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: str


class UserResponse(BaseModel):
    data: User


@app.get("/api/user/{user_id}", response_model=UserResponse)
def get_user(user_id: int):
    user_data = users.get(user_id)

    if not user_data:
        raise HTTPException(status_code=404, detail="User not found")

    user = User(**user_data)

    return UserResponse(data=user)
