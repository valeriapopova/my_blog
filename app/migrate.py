from flask_migrate import Migrate
from models import Post, Tag
from app import app, db

migrate = Migrate(app, db)
