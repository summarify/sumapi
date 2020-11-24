import requests
from .config import URL


class SumAPI:
    def __init__(self, auth):
        """
            In order to send requests in the API, you need to define your token in this class.

            Parameters
            ----------
            auth : dict
                Must contain your access_token and token_type, you can get this with Auth function.

            Examples
            --------
            from sumapi.auth import auth
            from sumapi.api import SumAPI

            token = auth(username='<your_username>', password='<your_password')
            api = SumAPI(token)
        """
        try:
            self.token = auth['access_token']
        except KeyError:
            return "Error with Token, Check your auth and try again."

        self.headers = {
            'accept': 'application/json',
            'Authorization': f'Bearer {self.token}',
            'Content-Type': 'application/json'}

    def prepare_data(self, body=None, domain=None, categories=None, context=None, question=None):
        """
            Function to create json for queries.
        """
        if domain != None:
            data = {
                'body': body,
                'domain': domain
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
            from sumapi.auth import auth
            from sumapi.api import SumAPI

            token = auth(username='<your_username>', password='<your_password')
            api = SumAPI(token)

            api.sentiment_analysis('Bu harika bir filmdi.', domain='general')
        """
        data = self.prepare_data(body=text, domain=domain)

        try:
            response = requests.post(URL['sentimentURL'], headers=self.headers, json=data).json()
        except (ConnectionError) as e:
            raise ConnectionError("Error with Connection, Check your Internet Connection or visit api.summarify.io/status for SumAPI Status")


        return response

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
            from sumapi.auth import auth
            from sumapi.api import SumAPI

            token = auth(username='<your_username>', password='<your_password')
            api = SumAPI(token)

            api.named_entity_recognition('GPT-3, Elon Musk ve Sam Altman tarafından kurulan OpenAI'in üzerinde birkaç yıldır çalışma yürüttüğü bir yapay zekâ teknolojisi.', domain='general')
        """
        data = self.prepare_data(body=text, domain=domain)
        try:
            response = requests.post(URL['nerURL'], headers=self.headers, json=data).json()
        except (ConnectionError) as e:
            raise ConnectionError("Error with Connection, Check your Internet Connection or visit api.summarify.io/status for SumAPI Status")


        return response

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
            from sumapi.auth import auth
            from sumapi.api import SumAPI

            token = auth(username='<your_username>', password='<your_password')
            api = SumAPI(token)

            api.classification("GPT-3, Elon Musk ve Sam Altman tarafından kurulan OpenAI'in üzerinde birkaç yıldır çalışma yürüttüğü bir yapay zekâ teknolojisi", domain='general')
            api.classification('Bankanızdan hiç memnun değilim, kredi ürününüz iyi çalışmıyor.', domain='finance')
        """
        data = self.prepare_data(body=text, domain=domain)

        try:
            response = requests.post(URL['classificationURL'], headers=self.headers, json=data).json()
        except (ConnectionError) as e:
            raise ConnectionError("Error with Connection, Check your Internet Connection or visit api.summarify.io/status for SumAPI Status")

        return response

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
            from sumapi.auth import auth
            from sumapi.api import SumAPI

            token = auth(username='<your_username>', password='<your_password')
            api = SumAPI(token)

            api.zero_shot_classification('Bu nasıl bir hizmet, gerçekten rezilsiniz.', categories='talep,şikayet,öneri')
        """
        data = self.prepare_data(body=text, categories=categories)

        try:
            response = requests.post(URL['zeroshotURL'], headers=self.headers, json=data).json()
        except (ConnectionError) as e:
            raise ConnectionError("Error with Connection, Check your Internet Connection or visit api.summarify.io/status for SumAPI Status")


        return response

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
            from sumapi.auth import auth
            from sumapi.api import SumAPI

            token = auth(username='<your_username>', password='<your_password')
            api = SumAPI(token)

            context =
            ABASIYANIK, Sait Faik. Hikayeci (Adapazarı 23 Kasım 1906-İstanbul 11 Mayıs 1954). İlk öğrenimine Adapazarı’nda Rehber-i Terakki Mektebi’nde başladı. İki yıl kadar Adapazarı İdadisi’nde okudu. İstanbul Erkek Lisesi’nde devam ettiği orta öğrenimini Bursa Lisesi’nde tamamladı (1928). İstanbul Edebiyat Fakültesi’ne iki yıl devam ettikten sonra babasının isteği üzerine iktisat öğrenimi için İsviçre’ye gitti. Kısa süre sonra iktisat öğrenimini bırakarak Lozan’dan Grenoble’a geçti. Üç yıl başıboş bir edebiyat öğrenimi gördükten sonra babası tarafından geri çağrıldı (1933). Bir müddet Halıcıoğlu Ermeni Yetim Mektebi'nde Türkçe grup dersleri öğretmenliği yaptı. Ticarete atıldıysa da tutunamadı. Bir ay Haber gazetesinde adliye muhabirliği yaptı (1942). Babasının ölümü üzerine aileden kalan emlakin geliri ile avare bir hayata başladı. Evlenemedi. Yazları Burgaz adasındaki köşklerinde, kışları Şişli’deki apartmanlarında annesi ile beraber geçen bu fazla içkili bohem hayatı ömrünün sonuna kadar sürdü.


            api.question_answering(context=context, question="Sait Faik nerede doğdu?")
        """
        data = self.prepare_data(context=context, question=question)

        try:
            response = requests.post(URL['questionURL'], headers=self.headers, json=data).json()
        except (ConnectionError) as e:
            raise ConnectionError("Error with Connection, Check your Internet Connection or visit api.summarify.io/status for SumAPI Status")


        return response
