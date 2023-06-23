
from parser.config import load
from parser.data_parser import (
    RedditClient,
    ask_subreddit,
    count_number_of_comments_by_authors,
    count_number_of_posts_by_authors
)


def main() -> None:

    report = RedditClient(config=load())
    report_days = 3
    reddit = ask_subreddit()
    posts = report.get_latest_posts(report_days, reddit, True)
    print(f'Top authors by number of posts: {count_number_of_posts_by_authors(posts)}')
    print(f'Top authors by number of comments: {count_number_of_comments_by_authors(posts)}')


if __name__ == "__main__":
    main()
