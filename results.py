import json
from slack_sdk.webhook import WebhookClient

with open("testResults/results.json") as file:
    stock = json.load(file)

total_tests = stock['run']['stats']['assertions']['total']
failed_tests = stock['run']['stats']['assertions']['failed']
passed_tests = total_tests - failed_tests

icon = ":white_check_mark:"

if failed_tests > 0:
    icon = ":exclamation:"

text = f"Postman collection results :\n" \
       f" {icon} total: {total_tests}, passed: {passed_tests}, failed: {failed_tests}\n " \
       f"<https://spirlhark.github.io/Postman_collection/| Allure-report>"


url = "https://hooks.slack.com/services/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"
webhook = WebhookClient(url)
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
