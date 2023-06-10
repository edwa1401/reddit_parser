import pandas as pd
from datetime import datetime, timedelta, date


def create_first_report_data() -> date:
    first_reports_date = datetime.now() - timedelta(days=3)
    return first_reports_date


def current_time_for_dict() -> date:
    current_date = datetime.now()
    return current_date


def create_posts_report(
    post_data: pd.DataFrame,
    first_reports_date: date,
    current_date: date,
) -> pd.DataFrame:
    posts_for_free_days = post_data.loc[(post_data["created_utc"] > first_reports_date)
                                        & (post_data["created_utc"] <= current_date)]

    posts_grouped_by_autors = posts_for_free_days.groupby('posts_author').size()
    top_posts_authors = posts_grouped_by_autors.sort_values(ascending=False)
    top_ten_posts_authors = top_posts_authors[:10]
    top_ten_posts_authors = top_ten_posts_authors.to_dict()

    return f'top ten subreddit posts authors with number of posts\
        for last three days {top_ten_posts_authors}'


def create_comments_report(
    post_comments: pd.DataFrame,
    first_reports_date: date,
    current_date: date,
) -> pd.DataFrame:
    comments_for_free_days = post_comments.loc[(post_comments["created_utc"] > first_reports_date)
                                               & (post_comments["created_utc"] <= current_date)]

    comments_grouped_by_authors = comments_for_free_days.groupby('comments_author').size()
    top_commentators = comments_grouped_by_authors.sort_values(ascending=False)
    top_ten_commentators = top_commentators[:10]
    top_ten_commentators = top_ten_commentators.to_dict()

    return f'top ten subreddit commentators with number of comments for last three days \
    {top_ten_commentators}'
