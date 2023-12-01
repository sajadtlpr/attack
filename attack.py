import requests
import time
from random import randint
import argparse

def report_instagram_account(username, report_type):
    # Send a fake report to Instagram
    response = requests.post(
        "https://www.instagram.com/users/report/",
        data={"username": username, "report_type": report_type},
    )

    # Check if the report was successful
    if response.status_code == 200:
        print(f"Reported {username} for {report_type} successfully!")
    else:
        print(f"Report failed for {username}. Error: {response.text}")

def main():
    parser = argparse.ArgumentParser(description='Instagram Account Reporting Tool')
    parser.add_argument('username', type=str, help='Target Instagram username')
    parser.add_argument('report_type', type=str, choices=['Hate_Speech', 'Impersonation', 'Nudity', 'Violence'],
                        help='Type of report to file (choose from Hate_Speech, Impersonation, Nudity, Violence)')

    args = parser.parse_args()

    # Craft your fake reports
    fake_reports = ["Hate_Speech", "Impersonation", "Nudity", "Violence"]

    # Loop through the reports
    for report in fake_reports:
        # Simulate human-like delays
        time.sleep(randint(2, 5))

        # Send a fake report to Instagram
        report_instagram_account(args.username, args.report_type)

if __name__ == "__main__":
    main()
