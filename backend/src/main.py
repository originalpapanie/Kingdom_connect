from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthCredentials
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime, timedelta
import jwt
import os
from typing import Optional

app = FastAPI(title="KingdomConnect API", version="0.1.0")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://kingdomconnect.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Security
security = HTTPBearer()
SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key-change-in-production")
ALGORITHM = "HS256"

# Pydantic models
class User(BaseModel):
    id: int
    email: str
    name: str
    role: str

class LoginRequest(BaseModel):
    email: str
    password: str

class LoginResponse(BaseModel):
    access_token: str
    token_type: str
    user: User

# Demo users database (in production, use a real database)
DEMO_USERS = {
    "admin@kingdomconnect.com": {
        "id": 1,
        "email": "admin@kingdomconnect.com",
        "name": "Admin User",
        "password": "admin123",
        "role": "admin"
    },
    "pastor@kingdomconnect.com": {
        "id": 2,
        "email": "pastor@kingdomconnect.com",
        "name": "Pastor John",
        "password": "pastor123",
        "role": "pastor"
    },
    "member@kingdomconnect.com": {
        "id": 3,
        "email": "member@kingdomconnect.com",
        "name": "Church Member",
        "password": "member123",
        "role": "member"
    },
    "volunteer@kingdomconnect.com": {
        "id": 4,
        "email": "volunteer@kingdomconnect.com",
        "name": "Volunteer Helper",
        "password": "volunteer123",
        "role": "volunteer"
    }
}

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(hours=24)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(credentials: HTTPAuthCredentials = Depends(security)):
    try:
        payload = jwt.decode(credentials.credentials, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
        return email
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

@app.post("/api/auth/login", response_model=LoginResponse)
async def login(request: LoginRequest):
    """Login endpoint for demo users"""
    user_data = DEMO_USERS.get(request.email)
    
    if not user_data or user_data["password"] != request.password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )
    
    access_token = create_access_token(data={"sub": user_data["email"]})
    
    return LoginResponse(
        access_token=access_token,
        token_type="bearer",
        user=User(**{k: v for k, v in user_data.items() if k != "password"})
    )

@app.get("/api/auth/me", response_model=User)
async def get_current_user(email: str = Depends(verify_token)):
    """Get current authenticated user"""
    user_data = DEMO_USERS.get(email)
    if not user_data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return User(**{k: v for k, v in user_data.items() if k != "password"})

@app.get("/api/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "timestamp": datetime.utcnow().isoformat()}

@app.get("/api/demo/users")
async def get_demo_users():
    """Get list of demo users (for development only)"""
    return {
        "demo_users": [
            {
                "email": email,
                "password": user["password"],
                "role": user["role"],
                "name": user["name"]
            }
            for email, user in DEMO_USERS.items()
        ]
    }

@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Welcome to KingdomConnect API",
        "version": "0.1.0",
        "docs": "/docs"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
