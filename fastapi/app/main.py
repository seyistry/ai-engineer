from typing import Optional, Annotated
from fastapi import Body, FastAPI, Response, status, HTTPException, Depends, Query
from pydantic import BaseModel
import psycopg
from psycopg.rows import dict_row
from .database import Session, get_session

SessionDep = Annotated[Session, Depends(get_session)]

app = FastAPI()

# # Connect to an existing database
# try:
#     conn = psycopg.connect(
#         "host=localhost dbname=fastapi user=postgres password=dracula11@", row_factory=dict_row)
#     cur = conn.cursor()
#     print("Database connection was successful")

# except Exception as error:
#     print(f"Database connection not successful:")
#     print(f"Error: {error}")


# class Post(BaseModel):
#     title: str
#     content: str
#     published: bool = False


# my_post = [{"title": "first post", "content": "this is my first post", "published": True, "rating": 4, 'id': 1},
#            {"title": "second post", "content": "this is my second post",
#                "published": False, "id": 2},
#            {"title": "mt third post", "content": "Happy to share my post", "published": True, "id": 3}]


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/sqlmodel")
async def test_sqlmodel(session: SessionDep):
    return {"status": "success"}



# @app.get("/posts")
# async def get_posts():
#     cur.execute(""" SELECT * FROM posts """)
#     posts = cur.fetchall()
#     return {"data": posts}


# @app.post("/posts", status_code=status.HTTP_201_CREATED)
# async def create_post(payload: Post):
#     cur.execute("""INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING *""",
#                 ((payload.title, payload.content, payload.published)))
#     new_post = cur.fetchone()
#     if new_post:
#         conn.commit()
#         return {'success': True, "message": "Post created", "data": new_post}
#     raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
#                         detail=f"Could not save new post")


# @app.get("/posts/{id}")
# async def get_post(id: int):
#     cur.execute("""SELECT * FROM posts WHERE id = %s""", (id,))
#     post = cur.fetchone()
#     if (post):
#         return {'status': True, "data": post}
#     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                         detail=f"Post with {id} not found")


# @app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
# async def delete_post(id: int):
#     cur.execute("""DELETE FROM posts WHERE id = %s RETURNING *""", (id,))
#     deleted_post = cur.fetchone()
#     if deleted_post:
#         conn.commit()
#         return Response(status_code=status.HTTP_204_NO_CONTENT)
#     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                         detail=f"Could not find post with {id}")


# @app.put("/posts/{id}")
# async def update_post(id: int, payload: Post):
#     cur.execute("""UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *""",
#                 (payload.title, payload.content, payload.published, id))
#     updated_post = cur.fetchone()
#     if updated_post:
#         conn.commit()
#         return {'success': True, "message": "Post updated", "data": updated_post}
#     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                         detail=f"Could not find post with {id}")

# @app.patch("/posts/{id}")
# async def patch_post(id: int, payload: Post):
#     cur.execute("""SELECT * FROM posts WHERE id = %s""", (id,))
#     post = cur.fetchone()
#     if not post:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"Could not find post with {id}")
    
#     updated_title = payload.title if payload.title is not None else post['title']
#     updated_content = payload.content if payload.content is not None else post['content']
#     updated_published = payload.published if payload.published is not None else post['published']
    
#     cur.execute("""UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *""",
#                 (updated_title, updated_content, updated_published, id))
#     updated_post = cur.fetchone()
#     conn.commit()
#     return {'success': True, "message": "Post patched", "data": updated_post}
