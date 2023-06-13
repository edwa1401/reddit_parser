import praw
import prawcore
from typing import Any
from datetime import datetime
import pandas as pd
from config import load


def ask_subreddit() -> str:
    sub = ""
    if not sub:
        sub = input("Введите subreddit ")
    else:
        sub = sub
    return sub


def create_request_to_reddit() -> Any:
    config = load()

    reddit = praw.Reddit(
        client_id=config.client_id,
        client_secret=config.client_secret,
        user_agent=config.user_agent,
        username=config.username,
        password=config.password,
        )
    return reddit


def create_posts_dict() -> pd.DataFrame:

    sub = ask_subreddit()
    reddit = create_request_to_reddit()
    subreddit = reddit.subreddit(sub)

    post_dict: dict[str, list[str | str | datetime]] = {
        "posts_author": [],
        "post_id": [],
        "created_utc": [],
    }
    try:
        for submission in subreddit.top(time_filter="week"):
            post_dict["posts_author"].append(submission.author.name)
            post_dict["post_id"].append(submission.id)
            post_dict["created_utc"].append(datetime.fromtimestamp(submission.created_utc))
    except prawcore.exceptions.ServerError as error:
        print(str(error))

    post_data = pd.DataFrame(post_dict)

    return post_data


def create_comments_dict() -> pd.DataFrame:

    sub = ask_subreddit()
    reddit = create_request_to_reddit()
    subreddit = reddit.subreddit(sub)

    comments_dict: dict[str, list[Any]] = {
        "comments_author": [],
        "comment_id": [],
        "created_utc": [],
    }

    try:
        for submission in subreddit.top(time_filter="week"):
            submission.comments.replace_more(limit=None)
            for comment in submission.comments.list():
                if comment.author is None:
                    comments_dict["comments_author"].append("not_autorised_author")
                else:
                    comments_dict["comments_author"].append(comment.author.name)
                comments_dict["comment_id"].append(comment.id)
                comments_dict["created_utc"].append(datetime.fromtimestamp(comment.created_utc))
    except prawcore.exceptions.ServerError as error:
        print(str(error))

    post_comments = pd.DataFrame(comments_dict)
    return post_comments
