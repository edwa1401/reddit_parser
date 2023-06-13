import pytest
import datetime
from datetime import timedelta
import pandas as pd


@pytest.fixture
def current_date():
    current_date = datetime.datetime(2023, 6, 9, 17, 20, 48, 175067)
    return current_date


@pytest.fixture
def first_report_date(current_date):
    first_report_date = current_date - datetime.timedelta(days=3)
    return first_report_date


@pytest.fixture
def create_user():
    pass
# TODO list 20 записей: for item in range(21) user+randin от 1 до 20)


@pytest.fixture
def create_id():
    pass
# TODO randint букв и цифр


@pytest.fixture
def create_date():
    pass
# TODO год и месяц фикс, число от current date до недели, время рандом от 0 до 60


@pytest.fixture
def pandas_posts_report():
    posts = {
        'posts_author': [
            'user1', 'user2', 'user3', 'user4', 'user5', 'user6', 'user7', 'user8',
            'user9', 'user1', 'user2', 'user1', 'user2', 'user14', 'user15', 'user16'
            ],
        'post_id': [
            '1434dxo', '1424s7m', '13z53lo', '140emza', '144d5hm', '140iopx', '144vqsz', '1410vib',
            '141jly8', '13yrcl9', '13yj5tf', '13zkinu', '13zw527', '143p39s', '143v676', '13zkg86',
            ],
        'created_utc': [
            datetime.datetime(2023, 6, 7, 8, 29, 21), datetime.datetime(2023, 6, 6, 8, 21, 42),
            datetime.datetime(2023, 6, 3, 10, 47, 37), datetime.datetime(2023, 6, 4, 17, 24, 30),
            datetime.datetime(2023, 6, 8, 19, 1, 17), datetime.datetime(2023, 6, 4, 19, 46, 2),
            datetime.datetime(2023, 6, 9, 7, 58, 26), datetime.datetime(2023, 6, 5, 6, 35, 33),
            datetime.datetime(2023, 6, 5, 19, 15, 54), datetime.datetime(2023, 6, 7, 1, 16, 49),
            datetime.datetime(2023, 6, 2, 20, 36, 9), datetime.datetime(2023, 6, 3, 21, 4, 11),
            datetime.datetime(2023, 6, 4, 4, 9, 19), datetime.datetime(2023, 6, 8, 0, 9, 9),
            datetime.datetime(2023, 6, 8, 4, 18, 48), datetime.datetime(2023, 6, 3, 21, 1, 50),
            ]
            }
    return pd.DataFrame(posts)


@pytest.fixture
def pandas_comments_report():
    comments = {
        'comments_author': [
            'user1', 'user2', 'user3', 'user4', 'user5', 'user6', 'user7', 'user8',
            'user9', 'user2', 'user2', 'user2', 'user3', 'user14', 'user15', 'user16',
            ],
        'comment_id': [
            'jn7y22q', 'jn7ygz9', 'jn83qo3', 'jn7yjga', 'jn7xsl2', 'jn7z4t6', 'jn7ybal', 'jn7yora',
            'jn7yvo1', 'jn7z4a3', 'jna8zgh', 'jn7z9rt', 'jn83fvb', 'jn84frj', 'jn85gv2', 'jn81tzr',
            ],
        'created_utc': [
            datetime.datetime(2023, 6, 7, 8, 29, 21), datetime.datetime(2023, 6, 7, 8, 21, 42),
            datetime.datetime(2023, 6, 3, 10, 47, 37), datetime.datetime(2023, 6, 4, 17, 24, 30),
            datetime.datetime(2023, 6, 8, 19, 1, 17), datetime.datetime(2023, 6, 4, 19, 46, 2),
            datetime.datetime(2023, 6, 9, 7, 58, 26), datetime.datetime(2023, 6, 5, 6, 35, 33),
            datetime.datetime(2023, 6, 7, 19, 15, 54), datetime.datetime(2023, 6, 7, 1, 16, 49),
            datetime.datetime(2023, 6, 7, 20, 36, 9), datetime.datetime(2023, 6, 3, 21, 4, 11),
            datetime.datetime(2023, 6, 4, 4, 9, 19), datetime.datetime(2023, 6, 8, 0, 9, 9),
            datetime.datetime(2023, 6, 8, 4, 18, 48), datetime.datetime(2023, 6, 3, 21, 1, 50),
            ]}
    return pd.DataFrame(comments)
