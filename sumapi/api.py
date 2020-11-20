import requests
from .config import URL


class SumAPI:
    def __init__(self, auth):
        try:
            self.token = auth['access_token']
        except KeyError:
            return "Error with Token, Check your auth and try again."

        self.headers = {
            'accept': 'application/json',
            'Authorization': f'Bearer {self.token}',
            'Content-Type': 'application/json'}

    def prepare_data(self, body=None, domain=None, categories=None):
        if categories == None:
            data = {
                'body': body,
                'domain': domain
            }
        elif categories != None:
            data = {
                'body': body,
                'categories': categories
            }
        return data

    def sentiment_analysis(self, text, domain='general'):
        data = self.prepare_data(body=text, domain=domain)

        response = requests.post(URL['sentimentURL'], headers=self.headers, json=data).json()

        return response

    def named_entity_recognition(self, text, domain='general'):
        data = self.prepare_data(body=text, domain=domain)

        response = requests.post(URL['nerURL'], headers=self.headers, json=data).json()

        return response

    def classification(self, text, domain='general'):
        data = self.prepare_data(body=text, domain=domain)

        response = requests.post(URL['classificationURL'], headers=self.headers, json=data).json()

        return response

    def zero_shot_classification(self, text, categories):
        data = self.prepare_data(body=text, categories=categories)

        response = requests.post(URL['zeroshotURL'], headers=self.headers, json=data).json()

        return response

    def question_answering(self, context, question):
        data = {
        'context': context,
        'question': question
            }

        response = requests.post(URL['questionURL'], headers=self.headers, json=data).json()

        return response
