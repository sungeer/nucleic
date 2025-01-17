from typing import Optional

from pydantic import BaseModel


# 定义Token的响应模型
class Token(BaseModel):
    access_token: str
    token_type: str


# 定义用户模型基类
class UserBase(BaseModel):
    id: Optional[int]
    username: str


# 定义创建用户的请求模型
class UserCreate(UserBase):
    password: str


# 定义返回用户信息的响应模型
class User(UserBase):
    class Config:
        orm_mode = True