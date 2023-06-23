import datetime
from parser.data_parser import (
    count_number_of_comments_by_authors,
    count_number_of_posts_by_authors,
    report_period
)
from random import randint

from faker import Faker
from freezegun import freeze_time


@freeze_time(datetime.datetime(2023, 6, 9, 17, 20, 48, 175067))
def test__report_period__success(first_report_date):
    assert report_period(3) == first_report_date


def test__count_number_of_posts_by_authors_success(make_posts, make_comments, make_top_posts_authors):
    top_posts_authors = make_top_posts_authors()
    assert count_number_of_posts_by_authors(make_posts(make_comments())) == top_posts_authors

# TODO add forking test for comments with faker and rand, add mock test for get_latests_post

# def test__count_number_of_comments_by_authors_success(make_posts, make_comments, make_top_comments_authors):
#     fake = Faker()
#     comment_author = fake.profile()["username"]
#     top_comments_authors = make_top_comments_authors()
#     assert count_number_of_comments_by_authors(make_comments()) == top_comments_authors
