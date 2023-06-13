import os
from dataclasses import dataclass


@dataclass
class Config:
    client_id: str
    client_secret: str
    user_agent: str
    username: str
    password: str


def load() -> Config:
    return Config(
        client_id=os.environ['REDDIT_PARSER_CLIENT_ID'],
        client_secret=os.environ['REDDIT_PARSER_CLIENT_SECRET'],
        user_agent=os.environ['REDDIT_PARSER_USER_AGENT'],
        username=os.environ['REDDIT_USER_NAME'],
        password=os.environ['REDDIT_PASSWORD'],
    )
