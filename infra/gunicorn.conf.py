import os

from dotenv import load_dotenv

bind = "localhost:8080"
workers = 4

environment = os.getenv("ENVIRONMENT")
print(environment)
env = os.path.join(os.getcwd(), f"{environment}.env")
print(env, "file_path")
if os.path.exists(env):
    load_dotenv(env)
