import os
from dotenv import load_dotenv

load_dotenv()

user_phone_number = os.getenv("user_phone_no")
user_password = os.getenv("user_password")