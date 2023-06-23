from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import datetime, timedelta
from parser.config import Config
from typing import Any

import praw


def ask_subreddit() -> str:
    return input("Введите subreddit ")


@dataclass
class Comment:
    created_at: datetime
    author: str


@dataclass
class Post:
    created_at: datetime
    author: str
    post_id: str
    comments: list[Comment]


class RedditClient:
    def __init__(self, config: Config) -> None:
        self.reddit = praw.Reddit(
            client_id=config.client_id,
            client_secret=config.client_secret,
            user_agent=config.user_agent,
            username=config.username,
            password=config.password,
            )

    def get_post_comments(self, post_id: str) -> list[Comment]:
        submission = self.reddit.submission(post_id)
        submission.comments.replace_more(limit=None)
        comments = [convert_comments(comment) for comment in submission.comments.list()]
        return comments

    def get_latest_posts(self, days: int, sub: str, load_comments: bool) -> list[Post]:
        subreddit = self.reddit.subreddit(sub)
        posts = [convert_post(submission) for submission in subreddit.top(time_filter="week") if
                 convert_post(submission).created_at >= report_period(days)]
        if load_comments:
            for post in posts:
                post.comments = self.get_post_comments(post_id=post.post_id)
        return posts


def report_period(days: int) -> datetime:
    return datetime.now() - timedelta(days)


def convert_comments(comment: Any) -> Comment:
    author = "not_autorised_author" if comment.author.name is None else comment.author.name
    return Comment(
        created_at=datetime.fromtimestamp(comment.created_utc),
        author=author,
    )


def convert_post(submission: Any) -> Post:
    return Post(
        created_at=datetime.fromtimestamp(submission.created_utc),
        author=submission.author.name,
        post_id=submission.id,
        comments=[],
    )

# TODO except prawcore.exceptions.ServerError


def count_number_of_posts_by_authors(posts: list[Post]) -> list[tuple[str, int]]:
    count_of_posts_by_authors = Counter([post.author for post in posts])
    return count_of_posts_by_authors.most_common(n=20)


def count_number_of_comments_by_authors(posts: list[Post]) -> list[tuple[str, int]]:
    count_of_comments_by_authors: defaultdict[str, int] = defaultdict(int)
    for post in posts:
        for comment in post.comments:
            count_of_comments_by_authors[comment.author] += 1
    number_of_comments = sorted(
        count_of_comments_by_authors.items(), key=lambda count: count[1], reverse=True
        )
    return number_of_comments
