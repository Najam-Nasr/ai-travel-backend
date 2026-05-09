import os
from dotenv import load_dotenv

load_dotenv()   # this line reads your .env file automatically

class Config:
    SECRET_KEY          = os.getenv("SECRET_KEY", "dev-secret-123")
    OPENAI_API_KEY      = os.getenv("OPENAI_API_KEY", "")
    OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY", "")
    GOOGLE_MAPS_API_KEY = os.getenv("GOOGLE_MAPS_API_KEY", "")
    MONGO_URI           = os.getenv("MONGO_URI", "mongodb://localhost:27017/travel_planner")
    DEBUG               = os.getenv("FLASK_DEBUG", "true").lower() == "true"