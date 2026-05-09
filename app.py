"""
AI Travel Planner - Main Flask Application
==========================================
Entry point. Registers all API blueprints and configures the app.
"""

from flask import Flask
from flask_cors import CORS
from config import Config
from routes.planner import planner_bp
from routes.weather import weather_bp
from routes.ai_recommend import ai_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app)  # Allow React frontend to call this backend

    # Register route blueprints
    app.register_blueprint(planner_bp, url_prefix="/api/planner")
    app.register_blueprint(weather_bp, url_prefix="/api/weather")
    app.register_blueprint(ai_bp,      url_prefix="/api/ai")

    @app.get("/")
    def health():
        return {"status": "AI Travel Planner backend is running ✅"}

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=5000)
