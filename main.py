from fastapi import FastAPI, HTTPException, Depends, Query
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List, Optional
import uvicorn

from database import SessionLocal, engine, Base
from models import User
from schemas import UserCreate, UserUpdate, UserResponse
import crud

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="User CRUD API",
    description="A simple FastAPI application for user management with CRUD operations",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def root():
    return {"message": "Welcome to User CRUD API"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.post("/users/", response_model=UserResponse, status_code=201)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    """Create a new user"""
    # Check if user with email already exists
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    return crud.create_user(db=db, user=user)

@app.get("/users/", response_model=List[UserResponse])
async def read_users(
    skip: int = Query(0, ge=0, description="Number of users to skip"),
    limit: int = Query(100, ge=1, le=1000, description="Number of users to return"),
    search: Optional[str] = Query(None, description="Search users by name or email"),
    db: Session = Depends(get_db)
):
    """Get all users with optional search and pagination"""
    users = crud.get_users(db, skip=skip, limit=limit, search=search)
    return users

@app.get("/users/{user_id}", response_model=UserResponse)
async def read_user(user_id: int, db: Session = Depends(get_db)):
    """Get a specific user by ID"""
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.put("/users/{user_id}", response_model=UserResponse)
async def update_user(user_id: int, user_update: UserUpdate, db: Session = Depends(get_db)):
    """Update a specific user"""
    # Check if user exists
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Check if email is being updated and if it's already taken
    if user_update.email and user_update.email != db_user.email:
        existing_user = crud.get_user_by_email(db, email=user_update.email)
        if existing_user:
            raise HTTPException(status_code=400, detail="Email already registered")
    
    updated_user = crud.update_user(db=db, user_id=user_id, user_update=user_update)
    return updated_user

@app.delete("/users/{user_id}")
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    """Delete a specific user"""
    success = crud.delete_user(db=db, user_id=user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}

@app.get("/users/stats/count")
async def get_users_count(db: Session = Depends(get_db)):
    """Get total count of users"""
    count = crud.get_users_count(db)
    return {"total_users": count}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
