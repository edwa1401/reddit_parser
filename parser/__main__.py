
from parser.report_processor import create_posts_report, create_comments_report
from parser.report_processor import current_time_for_dict, create_first_report_data
from parser.data_parser import create_posts_dict, create_comments_dict


def main() -> None:

    top_post_authors = create_posts_report(
        post_data=create_posts_dict(),
        first_reports_date=create_first_report_data(),
        current_date=current_time_for_dict(),
        )

    top_comments_authors = create_comments_report(
        post_comments=create_comments_dict(),
        first_reports_date=create_first_report_data(),
        current_date=current_time_for_dict(),
        )
    print(top_post_authors)
    print(top_comments_authors)


if __name__ == "__main__":
    main()
