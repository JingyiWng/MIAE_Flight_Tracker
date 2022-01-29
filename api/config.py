# To set up an environment file
from pydantic import BaseSettings

class Settings(BaseSettings):
    ROOT_URL: str

settings = Settings()  # this is a variable