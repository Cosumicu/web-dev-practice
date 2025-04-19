from .base import *

DATABASES = {
    "default": {
        "ENGINE": env.str("POSTGRES_ENGINE"),
        "NAME": env.str("POSTGRES_DB"),
        "USER": env.str("POSTGRES_USER"),
        "PASSWORD": env.str("POSTGRES_PASSWORD"),
        "HOST": env.str("PG_HOST"),
        "PORT": env.int("PG_PORT"),  # Convert port to integer
    }
}