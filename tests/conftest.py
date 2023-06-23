import datetime
from parser.data_parser import Comment, Post

import pytest


@pytest.fixture
def current_date():
    current_date = datetime.datetime(2023, 6, 9, 17, 20, 48, 175067)
    return current_date


@pytest.fixture
def first_report_date(current_date):
    first_report_date = current_date - datetime.timedelta(days=3)
    return first_report_date


@pytest.fixture
def make_comments():
    def inner(created_at: datetime.datetime | None = None, author: str | None = None):
        num_of_comments = 2
        return [Comment(
            created_at=created_at or datetime.datetime(2023, 6, 6, 6, 59, 59),
            author=author or "user1",
            )
            for _ in range(num_of_comments)
        ]
    return inner

@pytest.fixture
def make_posts(make_comments):
    def inner(created_at: datetime.datetime | None = None, author: str | None = None, post_id: str | None = None):
        num_of_posts_authors = 2
        posts = [Post(
            created_at=created_at or datetime.datetime(2023, 6, 6, 6, 59, 59),
            author=author or "user1",
            post_id=post_id or "1111222",
            comments=make_comments,
            )
            for _ in range(num_of_posts_authors)
        ]
        return posts
    return inner


@pytest.fixture
def make_top_posts_authors():
    def inner(author: str | None = None, count_posts: int | None = None):
        num_of_posts_authors = 2
        top_posts_authors = []
        for _ in range(num_of_posts_authors):
            line = (author or "user1", count_posts or 2)
        top_posts_authors.append(line)
        return top_posts_authors
    return inner


@pytest.fixture
def make_top_comments_authors():
    def inner(author: str | None = None, count_comments: int | None = None):
        num_of_authors = 1
        top_comments_authors = [(author or "user1",
                                 count_comments or 2) for _ in range(num_of_authors)]
        return top_comments_authors
    return inner

