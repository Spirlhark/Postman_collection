import json
import os
import requests

url_slack = os.environ.get('SLACK_WEBHOOK_URL2')
text1 = os.environ.get('GITHUB_REPOSITORY')
text3 = os.environ['GITHUB_REF_NAME'] 


with open("./testResults/results.json") as file:
    stock = json.load(file)

total_tests = (stock['run']['stats']['assertions']['total'])
failed_tests = (stock['run']['stats']['assertions']['failed'])

passed_tests = total_tests - failed_tests
print(total_tests)
print(failed_tests)
print(passed_tests)

icon = ":white_check_mark:"

if failed_tests > 0:
    icon = ":x:"

text = f"Postman collection results_[{text3}]: \n" \
       f" [{text1}] \n" \
       f" {icon} total: {total_tests}, passed: {passed_tests}, failed: {failed_tests}\n " \
       f"<https://spirlhark.github.io/Postman_collection/| Allure-report>"

header = {'Content-type': 'application/json'}
data_body = {
    "blocks": [
        {
        "type": "section",
        "text": {
            "type": "mrkdwn", 
            "text": text
            }
        }]
}

response = requests.post(url_slack, json=data_body, headers=header)