# -*- coding: utf-8 -*-
import sys
from functools import lru_cache
from pydantic import model_validator
from pydantic_settings import BaseSettings


class CommonConfig(BaseSettings):
    """
    Common Config
    """

    # jwt stuff
    SECRET_KEY: str = "26c73810b8dc1a0451137549e5e74f6ce5f7d82b49d3582c9407bdff66e8488a"
    ALGORITHM: str = "HS256"
    # database
    SQLALCHEMY_DATABASE_URL: str = ""
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_HOST: str
    POSTGRES_PORT: str

    class Config:
        env_file = "././.env"
        from_attributes = True
        extra = "allow"

    @model_validator(mode="after")
    def validate_database(cls, values):
        values.SQLALCHEMY_DATABASE_URL = f"postgresql://{values.POSTGRES_USER}:{values.POSTGRES_PASSWORD}@{values.POSTGRES_HOST}:{values.POSTGRES_PORT}/{values.POSTGRES_DB}"  # NoQa


class TestConfig(CommonConfig):
    """
    Testing config
    """

    # database
    SQLALCHEMY_DATABASE_URL: str = "sqlite:///./video_catalog.db"

    @model_validator(mode="after")
    def validate_database(cls, values):
        pass


@lru_cache()
def get_config_based_on_environment():
    """
    Get app configurations for different environments
    """
    if "pytest" in sys.modules:
        return TestConfig()
    return CommonConfig()


config = get_config_based_on_environment()
