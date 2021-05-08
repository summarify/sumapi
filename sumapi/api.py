import requests
from tqdm import tqdm
import json
from json import JSONDecodeError
from .config import URL
import time

class SumAPI:
    def __init__(self, username, password):
        """
            In order to send requests in the API, you need to define your token in this class.

            Parameters
            ----------
            username : str
                Your API Username
            password : str"
                Your API Password

            Examples
            --------
            from sumapi.api import SumAPI

            api = SumAPI(username='<your_username>, password='<your_password>')
        """
        self.username = username
        self.password = password

        try:
            self.token =self._get_token()['access_token']
        except KeyError:
            raise KeyError("Error with Token, Try again by checking your username and password.")
        except TypeError:
            raise ConnectionError("Error with Connection, Check your Internet Connection or visit api.summarify.io/status for SumAPI Status")

        self.headers = {
            'accept': 'application/json',
            'Authorization': f'Bearer {self.token}',
            'Content-Type': 'application/json'}

    def _get_token(self):
        """
        Returns
        -------
        dict:
            access_token: str
                Your API Access Token
            token_type: str
                Your Token Type
        """
        login_data = {
            'username': self.username,
            'password': self.password
        }

        try:
            response = requests.post(URL["tokenURL"], data=login_data)
            response_json = response.json()
        except JSONDecodeError:
            return response
        except ConnectionError as e:
            raise ConnectionError("Error with Connection, Check your Internet Connection or visit api.summarify.io/status for SumAPI Status")

        if "detail" in response_json.keys():
            if response_json['detail'] == 'Incorrect username or password':
                raise ValueError("There is an error in the login information. Try again by checking your username and password.")

        return response_json

    def timeout_check(self, response_json):
        if "detail" in response_json.keys():
            if response_json['detail'] == 'Could not validate credentials':
                self.headers = {
                    'accept': 'application/json',
                    'Authorization': f"Bearer {self._get_token()['access_token']}",
                    'Content-Type': 'application/json'}
                return True
        else:
            return False

    def prepare_data(self, body=None, domain=None, categories=None, context=None, question=None, percentage=None, word_count=None):
        """
            Function to create json for queries.
        """
        if percentage != None or word_count != None:
            data = {
                'body': body,
                'percentage': percentage,
                'domain': domain,
                'word_count': word_count
            }
        elif categories != None:
            data = {
                'body': body,
                'categories': categories
            }
        elif question != None:
            data = {
                'context': context,
                'question': question
            }
        elif domain != None:
            data = {
                'body': body,
                'domain': domain
            }

        return data

    def sentiment_analysis(self, text, domain='general'):
        """
            It makes sentiment analysis prediction for the sentences / samples you send.

            Parameters
            ----------
            text : str
                Your sample text.
            domain: str
                Model Domain ['general']

            Returns
            -------
            dict:
                body: str
                    Your sample text.
                evaluation: dict
                    label: str
                        Predicted label positive/negative
                    score: float
                        Prediction probability

            Examples
            --------
            from sumapi.api import SumAPI

            api = SumAPI(username='<your_username>', password='<your_password')

            api.sentiment_analysis('Bu harika bir filmdi.', domain='general')
        """
        data = self.prepare_data(body=text, domain=domain)

        try:
            response = requests.post(URL['sentimentURL'], headers=self.headers, json=data)
            response_json = response.json()
            if self.timeout_check(response_json) == True:
                response = requests.post(URL['sentimentURL'], headers=self.headers, json=data)
                response_json = response.json()
                return response_json
        except JSONDecodeError:
            return response.content
        except ConnectionError:
            raise ConnectionError("Error with Connection, Check your Internet Connection or visit api.summarify.io/status for SumAPI Status")
        

        return response_json

    def named_entity_recognition(self, text, domain='general'):
        """
            It makes named entitity recognition prediction for the sentences / samples you send.

            Parameters
            ----------
            text : str
                Your sample text.
            domain: str
                Model Domain ['general']

            Returns
            -------
            dict:
                body: str
                    Your sample text.
                evaluation: dict
                    index_num: dict
                        word: str
                            Predicted word
                        score: float
                            Prediction probability
                        entitity: str
                            Predicted Entitity ['LOC','ORG','MISC','PERSON']
                        index: integer
                            The word's index in a sentence
            Examples
            --------
            from sumapi.api import SumAPI

            api = SumAPI(username='<your_username>', password='<your_password')

            api.named_entity_recognition("GPT-3, Elon Musk ve Sam Altman tarafından kurulan OpenAI'in üzerinde birkaç yıldır çalışma yürüttüğü bir yapay zekâ teknolojisi.", domain='general')
        """
        data = self.prepare_data(body=text, domain=domain)
        try:
            response = requests.post(URL['nerURL'], headers=self.headers, json=data)
            response_json = response.json()
            if self.timeout_check(response_json) == True:
                response = requests.post(URL['nerURL'], headers=self.headers, json=data)
                response_json = response.json()
                return response_json
        except JSONDecodeError:
            return response.content
        except ConnectionError:
            raise ConnectionError("Error with Connection, Check your Internet Connection or visit api.summarify.io/status for SumAPI Status")
        

        return response_json

    def classification(self, text, domain='general'):
        """
            It makes classification prediction for the sentences / samples you send.

            Parameters
            ----------
            text : str
                Your sample text.
            domain: str
                Model Domain ['general','finance']

            Returns
            -------
            dict:
                body: str
                    Your sample text.
                evaluation: dict
                    label: str
                        Predicted class / label
                    score: float
                        Prediction probability

            Examples
            --------
            from sumapi.api import SumAPI

            api = SumAPI(username='<your_username>', password='<your_password')

            api.classification("GPT-3, Elon Musk ve Sam Altman tarafından kurulan OpenAI'in üzerinde birkaç yıldır çalışma yürüttüğü bir yapay zekâ teknolojisi", domain='general')
            api.classification('Bankanızdan hiç memnun değilim, kredi ürününüz iyi çalışmıyor.', domain='finance')
        """
        data = self.prepare_data(body=text, domain=domain)

        try:
            response = requests.post(URL['classificationURL'], headers=self.headers, json=data)
            response_json = response.json()
            if self.timeout_check(response_json) == True:
                response = requests.post(URL['classificationURL'], headers=self.headers, json=data)
                response_json = response.json()
                return response_json
        except JSONDecodeError:
            return response.content
        except ConnectionError:
            raise ConnectionError("Error with Connection, Check your Internet Connection or visit api.summarify.io/status for SumAPI Status")
        

        return response_json

    def zero_shot_classification(self, text, categories):
        """
            It makes Zero Shot Classification prediction for the sentences / samples you send.

            Parameters
            ----------
            text : str
                Your sample text.
            categories: str
                Potential labels that may your sentence / sample be

            Returns
            -------
            dict:
                body: str
                    Your sample text.
                evaluation: dict
                    sequence: str
                        Your sample text.
                    labels: list
                        Potential labels you provide as input
                    scores: list
                        Prediction probabilities
                    label: str
                        Predicted label
            Examples
            --------
            from sumapi.api import SumAPI

            api = SumAPI(username='<your_username>', password='<your_password')

            api.zero_shot_classification('Bu nasıl bir hizmet, gerçekten rezilsiniz.', categories='talep,şikayet,öneri')
        """
        data = self.prepare_data(body=text, categories=categories)

        try:
            response = requests.post(URL['zeroshotURL'], headers=self.headers, json=data)
            response_json = response.json()
            if self.timeout_check(response_json) == True:
                response = requests.post(URL['zeroshotURL'], headers=self.headers, json=data)
                response_json = response.json()
                return response_json
        except JSONDecodeError:
            return response.content
        except ConnectionError:
            raise ConnectionError("Error with Connection, Check your Internet Connection or visit api.summarify.io/status for SumAPI Status")

        return response_json

    def question_answering(self, context, question):
        """
            It makes Question Answering with Context.

            Parameters
            ----------
            context : str
                The context for your question.
            question: str
                Your question.

            Returns
            -------
            dict:
                body: str
                    Your question.
                evaluation: dict
                    scores: str
                        Prediction probability
                    answer: str
                        Predicted Answer
            Examples
            --------
            from sumapi.api import SumAPI

            api = SumAPI(username='<your_username>', password='<your_password')

            context =
            ABASIYANIK, Sait Faik. Hikayeci (Adapazarı 23 Kasım 1906-İstanbul 11 Mayıs 1954). İlk öğrenimine Adapazarı’nda Rehber-i Terakki Mektebi’nde başladı. İki yıl kadar Adapazarı İdadisi’nde okudu. İstanbul Erkek Lisesi’nde devam ettiği orta öğrenimini Bursa Lisesi’nde tamamladı (1928). İstanbul Edebiyat Fakültesi’ne iki yıl devam ettikten sonra babasının isteği üzerine iktisat öğrenimi için İsviçre’ye gitti. Kısa süre sonra iktisat öğrenimini bırakarak Lozan’dan Grenoble’a geçti. Üç yıl başıboş bir edebiyat öğrenimi gördükten sonra babası tarafından geri çağrıldı (1933). Bir müddet Halıcıoğlu Ermeni Yetim Mektebi'nde Türkçe grup dersleri öğretmenliği yaptı. Ticarete atıldıysa da tutunamadı. Bir ay Haber gazetesinde adliye muhabirliği yaptı (1942). Babasının ölümü üzerine aileden kalan emlakin geliri ile avare bir hayata başladı. Evlenemedi. Yazları Burgaz adasındaki köşklerinde, kışları Şişli’deki apartmanlarında annesi ile beraber geçen bu fazla içkili bohem hayatı ömrünün sonuna kadar sürdü.


            api.question_answering(context=context, question="Sait Faik nerede doğdu?")
        """
        data = self.prepare_data(context=context, question=question)

        try:
            response = requests.post(URL['questionURL'], headers=self.headers, json=data)
            response_json = response.json()
            if self.timeout_check(response_json) == True:
                response = requests.post(URL['questionURL'], headers=self.headers, json=data)
                response_json = response.json()
                return response_json
        except JSONDecodeError:
            return response.content
        except ConnectionError:
            raise ConnectionError("Error with Connection, Check your Internet Connection or visit api.summarify.io/status for SumAPI Status")

        return response_json

    def summarization(self, text, percentage=None, word_count=None, domain='SumBasic'):
        """
            It makes Summarization for the sentences / samples you send.

            Parameters
            ----------
            text : str
                Your sample text.
            percentage: float
                Percentage of the text you want to summarize. It takes values between 0 and 1. 1 gives the shortest summary and 0 the longest summary.
            domain: str
                Model Domain ['SumBasic','SumComplex']
                    SumBasic: Extraction Based Summarization with Statistical Algorithms
                    SumComplex: Abstraction Based Summarization with Cutting Edge Algorithms

            Returns
            -------
            dict:
                body: str
                    Your sample text.
                evaluation: dict
                    summarized_text: str
                        Summarized Text
                    

            Examples
            --------
            from sumapi.api import SumAPI

            api = SumAPI(username='<your_username>', password='<your_password')
            
            sample_text = "First of all, numerous software patches must be conducted to keep systems up to date. Cyber ​​attackers that use malware are trying to infiltrate company networks via abusing some undetected vulnerabilities within their software. According to a survey by security company Tripwire, one in three IT professionals said their company was infiltrated through an unpatched vulnerability. Thus, the validity of the patches should be constantly in check. Secondly, the devices that are connected to the network should be frequently monitored. Recognizing requests from devices that are connected to the main network is one of the most important areas of protection against malware. If the monitoring is missed, an evil ransomware gang can detect some vulnerabilities of the remote access doors. The more preferable scenario is having ethical hackers discover those potentially infected computers. Moreover, the most important data should be determined and an effective backup strategy should be implemented. It is very important to operate backups of important data to protect it against cyber attackers. If crypto ransomware enters the system and captures some devices, the data can be restored thanks to a recent backup, and the related devices can become operational in a short time. Yet, the first move of a hacker is almost always to cut access to those backups, so strong protection of those backups is also essential."

            api.summarization(text=sample_text, percentage=0.5, domain='SumBasic')
            api.summarization(text=sample_text, percentage=0.5, domain='SumComplex')
            api.summarization(text=sample_text, word_count=100, domain='SumComplex')
        """
        data = self.prepare_data(body=text, domain=domain, percentage=percentage, word_count=word_count)

        try:
            response = requests.post(URL['summarizationURL'], headers=self.headers, json=data)
            response_json = response.json()
            if self.timeout_check(response_json) == True:
                response = requests.post(URL['summarizationURL'], headers=self.headers, json=data)
                response_json = response.json()
                return response_json
        except JSONDecodeError:
            return response.content
        except ConnectionError:
            raise ConnectionError("Error with Connection, Check your Internet Connection or visit api.summarify.io/status for SumAPI Status")
        

        return response_json
    
    def spell_check(self, text, domain='general'):
        """
            It makes spell checking for the sentences / samples you send.

            Parameters
            ----------
            text : str
                Your sample text.
            domain: str
                Model Domain ['general']

            Returns
            -------
            dict:
                body: str
                    Your sample text.
                evaluation: dict
                    evaluation: str
                        Spell Checked Sentence

            Examples
            --------
            from sumapi.api import SumAPI

            api = SumAPI(username='<your_username>', password='<your_password>')

            api.spell_check('bu hstali cumle duzelexek gibi dutuyor.', domain='general')
        """
        data = self.prepare_data(body=text, domain=domain)

        try:
            response = requests.post(URL['spellCheckURL'], headers=self.headers, json=data)
            response_json = response.json()
            if self.timeout_check(response_json) == True:
                response = requests.post(URL['spellCheckURL'], headers=self.headers, json=data)
                response_json = response.json()
                return response_json
        except JSONDecodeError:
            return response.content
        except ConnectionError:
            raise ConnectionError("Error with Connection, Check your Internet Connection or visit api.summarify.io/status for SumAPI Status")
        return response_json

    def multi_request(self, data, packet_size=250):
        """
            It allows you to make multiple queries to different products at the same time. We recommend this for large datasets.

            Parameters
            ----------
            data : pandas.dataframe
                Your requests dataframe, an example can be find on Examples page.
                body: str
                    Your sample text.
                model_name: str
                    the product you want to run ['sentiment', 'classification', 'ner']
                domain: str
                    Model Domain, It may differ depending on the product.
                        sentiment : ['general']
                        classification: ['general', 'finance']
                        ner: ['general']

            Returns
            -------
            evaluations: dict
                Outputs of all models are listed one by one. The output may vary depending on the product you use.


            Examples
            --------
            from sumapi.api import SumAPI
            import pandas as pd

            df = pd.DataFrame([
                {
                  "body": "Bu güzel bir filmdi.",
                  "model_name": "sentiment",
                  "domain": "general"
                },
                {
                  "body": "GPT-3, Elon Musk ve Sam Altman tarafından kurulan OpenAI'in üzerinde birkaç yıldır çalışma yürüttüğü bir yapay zekâ teknolojisi..",
                  "model_name": "classification",
                  "domain": "general"
                },
                {
                  "body": "Summarify, 2020 yılında istanbulda kurulmuş bir doğal dil işleme ve yapay zeka şirketidir..",
                  "model_name": "ner",
                  "domain": "general"
                }])

            print(df.head())

            api = SumAPI(username='<your_username>', password='<your_password')

            api.multi_request(data=df)
        """
        if len(data) > packet_size:
            packet_count = int(len(data) / packet_size)
            packet_odd = len(data) % packet_size
            evaluations = []
            try:
                for packet in tqdm(range(1,packet_count+1), desc=f'Packet:'):
                    if packet == packet_count:
                        try:
                            jdata = {"argList": json.loads(data[packet*packet_size-packet_size:packet*packet_size+packet_odd].to_json(orient='records'))}
                            try:
                                response = requests.post(URL['multirequestURL'], headers=self.headers, json=jdata, timeout=3600)
                                if response.json() == b'<html>\r\n<head><title>502 Bad Gateway</title></head>\r\n<body bgcolor="white">\r\n<center><h1>502 Bad Gateway</h1></center>\r\n<hr><center>nginx</center>\r\n</body>\r\n</html>\r\n':
                                    print('Something wrong with server, sleeping 10 mins.')
                                    time.sleep(600)
                                    response = requests.post(URL['multirequestURL'], headers=self.headers, json=jdata, timeout=3600)
                                    if self.timeout_check(response.json()) == True:
                                        response = requests.post(URL['multirequestURL'], headers=self.headers, json=jdata, timeout=3600)
                                        evaluations += response.json()['evaluations']
                                        continue
                                    evaluations += response.json()['evaluations']
                                    continue
                            except requests.exceptions.ConnectionError:
                                print('Something wrong with server, sleeping 10 mins.')
                                time.sleep(600)
                                response = requests.post(URL['multirequestURL'], headers=self.headers, json=jdata, timeout=3600)
                                if self.timeout_check(response.json()) == True:
                                    response = requests.post(URL['multirequestURL'], headers=self.headers, json=jdata, timeout=3600)
                                    evaluations += response.json()['evaluations']
                                    continue
                                evaluations += response.json()['evaluations']
                                continue
                            if self.timeout_check(response.json()) == True:
                                response = requests.post(URL['multirequestURL'], headers=self.headers, json=jdata, timeout=3600)
                                evaluations += response.json()['evaluations']
                                continue
                            evaluations += response.json()['evaluations']
                        except KeyError:
                            jdata = {"argList": json.loads(data[packet*packet_size-packet_size:packet*packet_size+packet_odd].to_json(orient='records'))}
                            try:
                                response = requests.post(URL['multirequestURL'], headers=self.headers, json=jdata, timeout=3600)
                                if response.json() == b'<html>\r\n<head><title>502 Bad Gateway</title></head>\r\n<body bgcolor="white">\r\n<center><h1>502 Bad Gateway</h1></center>\r\n<hr><center>nginx</center>\r\n</body>\r\n</html>\r\n':
                                    print('Something wrong with server, sleeping 10 mins.')
                                    time.sleep(600)
                                    response = requests.post(URL['multirequestURL'], headers=self.headers, json=jdata, timeout=3600)
                                    if self.timeout_check(response.json()) == True:
                                        response = requests.post(URL['multirequestURL'], headers=self.headers, json=jdata, timeout=3600)
                                        evaluations += response.json()['evaluations']
                                        continue
                                    evaluations += response.json()['evaluations']
                                    continue
                            except requests.exceptions.ConnectionError:
                                print('Something wrong with server, sleeping 10 mins.')
                                time.sleep(600)
                                response = requests.post(URL['multirequestURL'], headers=self.headers, json=jdata, timeout=3600)
                                if self.timeout_check(response.json()) == True:
                                    response = requests.post(URL['multirequestURL'], headers=self.headers, json=jdata, timeout=3600)
                                    evaluations += response.json()['evaluations']
                                    continue
                                evaluations += response.json()['evaluations']
                                continue
                            if self.timeout_check(response.json()) == True:
                                response = requests.post(URL['multirequestURL'], headers=self.headers, json=jdata, timeout=3600)
                                evaluations += response.json()['evaluations']
                                continue
                            evaluations += response.json()['evaluations']
                    else:
                        jdata = {"argList": json.loads(data[packet*packet_size-packet_size:packet*packet_size].to_json(orient='records'))}
                        try:
                            try:
                                response = requests.post(URL['multirequestURL'], headers=self.headers, json=jdata, timeout=3600)
                                if response.status_code == 502:
                                    print('Something wrong with server, sleeping 10 mins.')
                                    time.sleep(600)
                                    response = requests.post(URL['multirequestURL'], headers=self.headers, json=jdata, timeout=3600)
                                    if self.timeout_check(response.json()) == True:
                                        response = requests.post(URL['multirequestURL'], headers=self.headers, json=jdata, timeout=3600)
                                        evaluations += response.json()['evaluations']
                                        continue
                                    evaluations += response.json()['evaluations']
                                    continue
                            except requests.exceptions.ConnectionError:
                                print('Something wrong with server, sleeping 10 mins.')
                                time.sleep(600)
                                response = requests.post(URL['multirequestURL'], headers=self.headers, json=jdata, timeout=3600)
                                if self.timeout_check(response.json()) == True:
                                    response = requests.post(URL['multirequestURL'], headers=self.headers, json=jdata, timeout=3600)
                                    evaluations += response.json()['evaluations']
                                    continue
                                evaluations += response.json()['evaluations']
                                continue
                            if self.timeout_check(response.json()) == True:
                                response = requests.post(URL['multirequestURL'], headers=self.headers, json=jdata, timeout=3600)
                                evaluations += response.json()['evaluations']
                                continue
                            evaluations += response.json()['evaluations']
                        except KeyError:
                            try:
                                response = requests.post(URL['multirequestURL'], headers=self.headers, json=jdata, timeout=3600)
                                if response.status_code == 502:
                                    print('Something wrong with server, sleeping 10 mins.')
                                    time.sleep(600)
                                    response = requests.post(URL['multirequestURL'], headers=self.headers, json=jdata, timeout=3600)
                                    if self.timeout_check(response.json()) == True:
                                        response = requests.post(URL['multirequestURL'], headers=self.headers, json=jdata, timeout=3600)
                                        evaluations += response.json()['evaluations']
                                        continue
                                    evaluations += response.json()['evaluations']
                                    continue
                            except requests.exceptions.ConnectionError:
                                print('Something wrong with server, sleeping 10 mins.')
                                time.sleep(600)
                                response = requests.post(URL['multirequestURL'], headers=self.headers, json=jdata, timeout=3600)
                                if self.timeout_check(response.json()) == True:
                                    response = requests.post(URL['multirequestURL'], headers=self.headers, json=jdata, timeout=3600)
                                    evaluations += response.json()['evaluations']
                                    continue
                                evaluations += response.json()['evaluations']
                                continue
                            if self.timeout_check(response.json()) == True:
                                response = requests.post(URL['multirequestURL'], headers=self.headers, json=jdata, timeout=3600)
                                evaluations += response.json()['evaluations']
                                continue
                            evaluations += response.json()['evaluations']
                            
            except JSONDecodeError:
                return response.content
            except ConnectionError:
                raise ConnectionError("Error with Connection, Check your Internet Connection or visit api.summarify.io/status for SumAPI Status")
            
            return {'evaluations': evaluations}
        else:
            try:
                response = requests.post(URL['multirequestURL'], headers=self.headers, json={"argList":json.loads(data.to_json(orient='records'))})
                if response.status_code == 502:
                    print('Something wrong with server, sleeping 10 mins.')
                    time.sleep(600)
                    response = requests.post(URL['multirequestURL'], headers=self.headers, json={"argList":json.loads(data.to_json(orient='records'))})
                    response_json = response.json()
                    return response_json
                response_json = response.json()
                if self.timeout_check(response_json) == True:
                    response = requests.post(URL['multirequestURL'], headers=self.headers, json={"argList":json.loads(data.to_json(orient='records'))})
                    response_json = response.json()
                    return response_json
                return response_json
            except JSONDecodeError:
                return response.content
            except ConnectionError:
                raise ConnectionError("Error with Connection, Check your Internet Connection or visit api.summarify.io/status for SumAPI Status")


    