from dotenv import load_dotenv
import os

load_dotenv()


def get_env(variable_name, default=None):
    return os.getenv(variable_name, default)