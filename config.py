# this is almost similar to python.env file 
# but since it's associated with pydantic settings, it has an extra layer of built in validations
# for secret keys and all

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # tells to automatically load files from /env file 
    model_config = SettingsConfigDict(
        env_file = ".env",
        env_file_encoding= "utf-8"
    )

    secret_key : SecretStr
    algorithm : str = "HS256"
    access_token_expired_minutes : int = 30

settings = Settings()    #loaded from .env file
