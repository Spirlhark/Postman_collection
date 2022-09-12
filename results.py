import json
import os
from slack_sdk.webhook import WebhookClient

with open("./testResults/results.json") as file:
# with open("./Postman_collection/testResults/results.json") as file:
# with open("testResults/results.json") as file:
    stock = json.load(file)

total_tests = stock['run']['stats']['assertions']['total']
failed_tests = stock['run']['stats']['assertions']['failed']
passed_tests = total_tests - failed_tests
print(total_tests)
print(failed_tests)
print(passed_tests)

icon = ":white_check_mark:"

if failed_tests > 0:
    icon = ":exclamation:"
text1 = os.environ.get('GITHUB_REPOSITORY')
text2 = os.environ['GITHUB_REPOSITORY']
text3 = os.environ['GITHUB_REF_NAME']
print(text1)
print(text2)
print(text3)
text = f"Postman collection results: \n" \
       f" {text1} \n" \
       f" {icon} total: {total_tests}, passed: {passed_tests}, failed: {failed_tests}\n " \
       f"<https://spirlhark.github.io/Postman_collection/| Allure-report>"


url = os.environ["SLACK_WEBHOOK_URL"]
webhook = WebhookClient(url)
print(111)
response = webhook.send(
    text="fallback",
    blocks=[
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": text
            }
        }
    ])
print(222)

