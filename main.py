from re import T
from uuid import UUID, uuid4
from fastapi import FastAPI,HTTPException
from typing import List
from models import Gender, Resources, Role, User, UserUpdate
app = FastAPI()

db: List[User] = [
    User(
        id = uuid4(),
        first_name="Mohammed",
        last_name="Mudassir",
        gender=Gender.male,
        roles= [Role.admin],
        resources=[Resources.r1,Resources.r2]
    ),
    User(
        id = uuid4(),
        first_name="Mohammed",
        last_name="Fatir",
        gender=Gender.male,
        roles= [Role.user,Role.admin],
        resources=[Resources.r2,Resources.r3]
    )
]

@app.get('/users')
def get_all_users():
    return db
    

@app.post('/users')
def add_user(user:User):
    db.append(user)
    return {"id": user.id}


@app.delete('/users/{user_id}')
def delete_user(user_id:UUID):
    for user in db:
        if user.id==user_id:
            db.remove(user)
            return {"delete":"success"}
    raise HTTPException(
        status_code  = 404,
        detail = f"user with id : {user_id} does not exists"
    )

@app.put("/users/{user_id}")
def update_user(user_update:UserUpdate,user_id:UUID):
    for user in db:
        if user.id==user_id:
            if user_update.first_name is not None:
                user.first_name=user_update.first_name
            if user_update.last_name is not None:
                user.last_name=user_update.last_name
            if user_update.roles is not None:
                user.roles=user_update.roles
            if user_update.resources is not None:
                user.resources=user_update.resources
            return
    raise HTTPException(
        status_code  = 404,
        detail = f"user with id : {user_id} does not exists"
    )

@app.get('/users/{user_id}')
def get_user_by_id(user_id:UUID):
    for user in db:
        if user.id==user_id:
            return user
        
    raise HTTPException(
        status_code  = 404,
        detail = f"user with id : {user_id} does not exists"
    )

@app.get('/users/resources/{resource}')
def get_users_by_resource(resource:Resources):

    temp:List[User]=[]

    for user in db:
        if resource in user.resources:
            temp.append(user)
    return temp