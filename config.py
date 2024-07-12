import os

from dotenv import load_dotenv
load_dotenv() 

class RedisConfig:
    HOST = os.environ.get("REDIS_HOST", None)
    PORT = os.environ.get("REDIS_PORT", None)