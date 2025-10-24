from typing import Optional
from fastapi import Body, FastAPI, Response, status, HTTPException
from pydantic import BaseModel
app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = False
    rating: Optional[int] = None


my_post = [{"title": "first post", "content": "this is my first post", "published": True, "rating": 4, 'id': 1},
           {"title": "second post", "content": "this is my second post",
               "published": False, "id": 2},
           {"title": "mt third post", "content": "Happy to share my post", "published": True, "id": 3}]


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/posts")
async def get_posts():
    return {"data": my_post}


@app.post("/posts", status_code=status.HTTP_201_CREATED)
async def create_post(payload: Post):
    obj = payload.model_dump()
    obj['id'] = len(my_post) + 1
    my_post.append(obj)
    return {'success': True, "message": "Post created", "data": obj}


@app.get("/posts/{id}")
async def get_post(id: int):
    for post in my_post:
        if post['id'] == id:
            return post
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Post with {id} not found")

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(id: int):
    for index, post in enumerate(my_post):
        if post['id'] == id:
            my_post.pop(index)
            return Response(status_code=status.HTTP_204_NO_CONTENT)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Post with {id} not found")