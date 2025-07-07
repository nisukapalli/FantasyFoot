# from pydantic import BaseModel, EmailStr
# from typing import Optional
# from datetime import datetime

# class UserBase(BaseModel):
#     username: str
#     email: EmailStr

# class UserCreate(UserBase):
#     password: str

# class UserUpdate(BaseModel):
#     username: Optional[str] = None
#     email: Optional[EmailStr] = None
#     avatar_url: Optional[str] = None

# class UserLogin(BaseModel):
#     username: str
#     password: str

# class UserResponse(UserBase):
#     id: int
#     is_active: bool
#     is_admin: bool
#     created_at: datetime
#     last_login: Optional[datetime] = None
#     avatar_url: Optional[str] = None

#     class Config:
#         from_attributes = True