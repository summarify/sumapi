from sumapi.auth import auth
from sumapi.api import SumAPI
import unittest
import os
import pandas as pd

class TestAPI(unittest.TestCase):
    def test_successful_auth(self):
        token = auth(username=os.environ.get('sum_api_username'), password=os.environ.get('sum_api_password'))
        self.assertEqual(token['token_type'], 'bearer')

    def test_sentiment_analysis(self):
        token = auth(username=os.environ.get('sum_api_username'), password=os.environ.get('sum_api_password'))
        api = SumAPI(token)

        response = api.sentiment_analysis('Bu film harikaydı.')
        self.assertEqual(response['evaluation']['label'], 'positive')

    def test_named_entity_recognition(self):
        token = auth(username=os.environ.get('sum_api_username'), password=os.environ.get('sum_api_password'))
        api = SumAPI(token)

        response = api.named_entity_recognition("Atatürk, 19 Mayıs 1919'da Samsuna çıktı")
        self.assertEqual(response['evaluation']['0']['entity'], 'B-PER')

    def test_general_classification(self):
        token = auth(username=os.environ.get('sum_api_username'), password=os.environ.get('sum_api_password'))
        api = SumAPI(token)

        response = api.classification("GPT-3, Elon Musk ve Sam Altman tarafından kurulan OpenAI'in üzerinde birkaç yıldır çalışma yürüttüğü bir yapay zekâ teknolojisi.")
        self.assertEqual(response['evaluation']['label'], 'technology')

    def test_finance_classification(self):
        token = auth(username=os.environ.get('sum_api_username'), password=os.environ.get('sum_api_password'))
        api = SumAPI(token)

        response = api.classification("Kredi kartımın şifresini kaybettim ancak size ulaşamıyorum. Gerçekten nasıl bir hizmet veriyorsunuz?", domain='finance')
        self.assertEqual(response['evaluation']['label'], 'kredi-karti')

    def test_zero_shot(self):
        token = auth(username=os.environ.get('sum_api_username'), password=os.environ.get('sum_api_password'))
        api = SumAPI(token)

        response = api.zero_shot_classification('Bu nasıl bir hizmet, gerçekten rezilsiniz.', categories='talep,şikayet,öneri')
        self.assertEqual(response['evaluation']['label'], 'şikayet')

    def test_question_answering(self):
        token = auth(username=os.environ.get('sum_api_username'), password=os.environ.get('sum_api_password'))
        api = SumAPI(token)

        context = """
        ABASIYANIK, Sait Faik. Hikayeci (Adapazarı 23 Kasım 1906-İstanbul 11 Mayıs 1954). İlk öğrenimine Adapazarı’nda Rehber-i Terakki Mektebi’nde başladı. İki yıl kadar Adapazarı İdadisi’nde okudu. İstanbul Erkek Lisesi’nde devam ettiği orta öğrenimini Bursa Lisesi’nde tamamladı (1928). İstanbul Edebiyat Fakültesi’ne iki yıl devam ettikten sonra babasının isteği üzerine iktisat öğrenimi için İsviçre’ye gitti. Kısa süre sonra iktisat öğrenimini bırakarak Lozan’dan Grenoble’a geçti. Üç yıl başıboş bir edebiyat öğrenimi gördükten sonra babası tarafından geri çağrıldı (1933). Bir müddet Halıcıoğlu Ermeni Yetim Mektebi'nde Türkçe grup dersleri öğretmenliği yaptı. Ticarete atıldıysa da tutunamadı. Bir ay Haber gazetesinde adliye muhabirliği yaptı (1942). Babasının ölümü üzerine aileden kalan emlakin geliri ile avare bir hayata başladı. Evlenemedi. Yazları Burgaz adasındaki köşklerinde, kışları Şişli’deki apartmanlarında annesi ile beraber geçen bu fazla içkili bohem hayatı ömrünün sonuna kadar sürdü.
        """

        response = api.question_answering(context=context, question="Sait Faik nerede doğdu?")
        self.assertEqual(response['evaluation']['answer'], '(Adapazarı')

    def test_multi_request(self):
        token = auth(username=os.environ.get('sum_api_username'), password=os.environ.get('sum_api_password'))
        api = SumAPI(token)

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
              "body": "Bankanızdan hiç memnun değilim, kredi ürününüz iyi çalışmıyor.",
              "model_name": "classification",
              "domain": "finance"
            },
            {
              "body": "Summarify, 2020 yılında istanbulda kurulmuş bir doğal dil işleme ve yapay zeka şirketidir..",
              "model_name": "ner",
              "domain": "general"
            }])

        response = api.multi_request(df)
        self.assertEqual(response['evaluations'][0]['evaluation']['label'], 'positive')


if __name__ == '__main__':
    unittest.main()
