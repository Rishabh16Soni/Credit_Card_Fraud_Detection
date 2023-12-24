import pymongo
import os
from dotenv import load_dotenv


load_dotenv()  # Load environment variables from .env file


class EnvironmentVariable:
    access_key = os.getenv("MONGODB_ACCESS_KEY")


env_var = EnvironmentVariable()
mongo_client = pymongo.MongoClient(f"mongodb+srv://aayush29142:aayush2914@cluster0.allf9ww.mongodb.net/")
TARGET_COLUMN = "default.payment.next.month"
