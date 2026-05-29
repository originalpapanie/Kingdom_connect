import os
from datetime import timedelta

class Config:
    """Base configuration"""
    SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key-change-in-production")
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 24 * 60
    
    # CORS
    CORS_ORIGINS = [
        "http://localhost:3000",
        "http://localhost:8000",
        "https://kingdomconnect.com",
    ]
    
    # Database
    DATABASE_URL = os.getenv(
        "DATABASE_URL",
        "postgresql://user:password@localhost/kingdom_connect"
    )
    
    class Config:
        env_file = ".env"

class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    TESTING = False

class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    TESTING = False

class TestingConfig(Config):
    """Testing configuration"""
    DEBUG = True
    TESTING = True
    DATABASE_URL = "sqlite:///./test.db"

def get_config():
    env = os.getenv("ENVIRONMENT", "development")
    if env == "production":
        return ProductionConfig()
    elif env == "testing":
        return TestingConfig()
    return DevelopmentConfig()
