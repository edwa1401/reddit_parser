from parser.report_processor import create_first_report_data, current_time_for_dict, create_posts_report, create_comments_report
from freezegun import freeze_time
import datetime
import pandas as pd


@freeze_time(datetime.datetime(2023, 6, 9, 17, 20, 48, 175067))
def test__current_time_for_dict__success(current_date):
    assert current_time_for_dict() == current_date


@freeze_time(datetime.datetime(2023, 6, 9, 17, 20, 48, 175067))
def test__create_first_report_data__success(first_report_date):
    assert create_first_report_data() == first_report_date


def test__create_posts_report_data__success(pandas_posts_report, first_report_date, current_date):

    dict_post_report = {'user1': 2, 'user14': 1, 'user15': 1, 'user5': 1, 'user7': 1}
    expected_result = f'top ten subreddit posts authors with number of posts\
        for last three days {dict_post_report}'

    post_report = create_posts_report(pandas_posts_report, first_report_date, current_date)

    assert post_report == expected_result


def test__create_comments_report_data__success(pandas_comments_report, first_report_date, current_date):

    dict_comments_report = {'user2': 3, 'user1': 1, 'user14': 1, 'user15': 1, 'user5': 1, 'user7': 1, 'user9': 1}
    expected_result = f'top ten subreddit commentators with number of comments for last three days\
     {dict_comments_report}'

    comments_report = create_comments_report(pandas_comments_report, first_report_date, current_date)

    assert comments_report == expected_result
