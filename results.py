import json
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

text = f"Postman collection results :\n" \
       f" {icon} total: {total_tests}, passed: {passed_tests}, failed: {failed_tests}\n " \
       f"<https://spirlhark.github.io/Postman_collection/| Allure-report>"


# url = "https://hooks.slack.com/services/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"
# url = "https://hooks.slack.com/services/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"
# url = secrets.SLACK_WEBHOOK_URL
url = ${{ secrets.SLACK_WEBHOOK_URL }}
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
