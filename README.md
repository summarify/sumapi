# SumAPI

<p align="center"><img src="https://raw.githubusercontent.com/summarify/sumapi/main/docs/sumapi_logo.png" width="200" height="200"></p>

**sumapi** is a python framework that makes it easy to use the api product developed by [summarify](https://summarify.io/). With the API product, solutions using cutting edge technology are presented to various NLP problems such as [sentiment analysis](https://en.wikipedia.org/wiki/Sentiment_analysis), [named entitity recognition](https://en.wikipedia.org/wiki/Named-entity_recognition), [question answering](https://en.wikipedia.org/wiki/Question_answering), [domain specific classification](https://en.wikipedia.org/wiki/Document_classification), [zero shot classification](https://en.wikipedia.org/wiki/Zero-shot_learning).


## Installation

You can install the sumapi on your computer by following the instructions below.

```bash
pip install sumapi
```

## Usage

**Authentication**

In order to use the API, you first need to get token with your unique username and password. If you do not have a username and want to test the API, please contact us at [info@summarify.io](mailto:info@summarify.io).

```python
from sumapi.auth import auth

token = auth(username='<your_username>', password='<your_password')
# {'access_token': 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX', 'token_type': 'bearer'}
```

**Sentiment Analysis**

```python
from sumapi.auth import auth
from sumapi.api import SumAPI

token = auth(username='<your_username>', password='<your_password')
api = SumAPI(token)

api.sentiment_analysis('Bu harika bir filmdi.', domain='general')
# {'body': 'Bu harika bir filmdi.', 'evaluation': {'label': 'positive', 'score': 0.983938992023468}}

```

**Named Entitity Recognition**

```python
from sumapi.auth import auth
from sumapi.api import SumAPI

token = auth(username='<your_username>', password='<your_password')
api = SumAPI(token)

api.named_entity_recognition("Mustafa Kemal Atatürk 19 Mayıs 1919'da Samsun'a ayak bastı.", domain='general')
#{'body': "Mustafa Kemal Atatürk 19 Mayıs 1919'da Samsun'a ayak bastı.", 'evaluation':
#                {'0': {'word': 'Mustafa',
#                   'score': 0.9938516616821289,
#                   'entity': 'B-PER',
#                   'index': 1},
#                  '1': {'word': 'Kemal',
#                   'score': 0.9881671071052551,
#                   'entity': 'I-PER',
#                   'index': 2},
#                  '2': {'word': 'Atatürk',
#                   'score': 0.9957979321479797,
#                   'entity': 'I-PER',
#                   'index': 3},
#                  '3': {'word': 'Samsun',
#                   'score': 0.9059983491897583,
#                   'entity': 'B-LOC',
#                   'index': 9}}} """
```

**Classification**

```python
from sumapi.auth import auth
from sumapi.api import SumAPI

token = auth(username='<your_username>', password='<your_password')
api = SumAPI(token)

api.classification("GPT-3, Elon Musk ve Sam Altman tarafından kurulan OpenAI'in üzerinde birkaç yıldır çalışma yürüttüğü bir yapay zekâ teknolojisi", domain='general')
# {'body': "GPT-3, Elon Musk ve Sam Altman tarafından kurulan OpenAI'in üzerinde birkaç yıldır çalışma yürüttüğü bir yapay zekâ teknolojisi", 'evaluation': {'label': 'technology', 'score': 0.9983301758766174}}

api.classification('Bankanızdan hiç memnun değilim, kredi ürününüz iyi çalışmıyor.', domain='finance')
# {'body': 'Bankanızdan hiç memnun değilim, kredi ürününüz iyi çalışmıyor.', 'evaluation': {'label': 'kredi'}}
```

**Zero Shot Classification**

```python
from sumapi.auth import auth
from sumapi.api import SumAPI

token = auth(username='<your_username>', password='<your_password')
api = SumAPI(token)

api.zero_shot_classification('Bu nasıl bir hizmet, gerçekten rezilsiniz.', categories='talep,şikayet,öneri')
# {'body': 'Bu nasıl bir hizmet, gerçekten rezilsiniz.', 'evaluation': {'sequence': 'Bu nasıl bir hizmet, gerçekten rezilsiniz.', 'labels': ['şikayet', 'öneri', 'talep'], 'scores': [0.97139573097229, 0.8201411962509155, 0.5891757011413574], 'label': 'şikayet'}}
```

**Question Answering**

```python
from sumapi.auth import auth
from sumapi.api import SumAPI

token = auth(username='<your_username>', password='<your_password')
api = SumAPI(token)

context = """ABASIYANIK, Sait Faik. Hikayeci (Adapazarı 23 Kasım 1906-İstanbul 11 Mayıs 1954). İlk öğrenimine Adapazarı’nda Rehber-i Terakki Mektebi’nde başladı. İki yıl kadar Adapazarı İdadisi’nde okudu. İstanbul Erkek Lisesi’nde devam ettiği orta öğrenimini Bursa Lisesi’nde tamamladı (1928). İstanbul Edebiyat Fakültesi’ne iki yıl devam ettikten sonra babasının isteği üzerine iktisat öğrenimi için İsviçre’ye gitti. Kısa süre sonra iktisat öğrenimini bırakarak Lozan’dan Grenoble’a geçti. Üç yıl başıboş bir edebiyat öğrenimi gördükten sonra babası tarafından geri çağrıldı (1933). Bir müddet Halıcıoğlu Ermeni Yetim Mektebi'nde Türkçe grup dersleri öğretmenliği yaptı. Ticarete atıldıysa da tutunamadı. Bir ay Haber gazetesinde adliye muhabirliği yaptı (1942). Babasının ölümü üzerine aileden kalan emlakin geliri ile avare bir hayata başladı. Evlenemedi. Yazları Burgaz adasındaki köşklerinde, kışları Şişli’deki apartmanlarında annesi ile beraber geçen bu fazla içkili bohem hayatı ömrünün sonuna kadar sürdü."""

api.question_answering(context=context, question="Sait Faik nerede doğdu?")
# {'body': 'Sait Faik nerede doğdu?', 'evaluation': {'score': 0.9611985087394714, 'answer': 'Adapazarı'}}
```

**Multi Argument**

```python
from sumapi.auth import auth
from sumapi.api import SumAPI
import pandas as pd

token = auth(username='<your_username>', password='<your_password')
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

print(df.head())

api.multi_request(data=df)
#{'evaluations': [{'body': 'Bu güzel bir filmdi.',
#   'evaluation': {'label': 'positive', 'score': 0.9714869260787964}},
#  {'body': "GPT-3, Elon Musk ve Sam Altman tarafından kurulan OpenAI'in üzerinde birkaç yıldır çalışma yürüttüğü bir yapay zekâ teknolojisi..",
#   'evaluation': {'label': 'technology', 'score': 0.9982953667640686}},
#  {'body': 'Bankanızdan hiç memnun değilim, kredi ürününüz iyi çalışmıyor.',
#   'evaluation': {'label': 'kredi'}},
#  {'body': 'Summarify, 2020 yılında istanbulda kurulmuş bir doğal dil işleme ve yapay zeka şirketidir..',
#   'evaluation': {'0': {'word': 'Sum',
#     'score': 0.6308539509773254,
#     'entity': 'B-ORG',
#     'index': 1},
#    '1': {'word': '##mar',
#     'score': 0.6408769488334656,
#     'entity': 'I-ORG',
#     'index': 2},
#    '2': {'word': '##if',
#     'score': 0.8179663419723511,
#     'entity': 'I-ORG',
#     'index': 3},
#    '3': {'word': '##y',
#     'score': 0.5688334703445435,
#     'entity': 'I-ORG',
#     'index': 4},
#    '4': {'word': 'istanbul',
#     'score': 0.9028254747390747,
#     'entity': 'B-LOC',
#     'index': 8}}}]}
```


## Licence

SumAPI is licensed under the MIT License - see [`LICENSE`](https://github.com/summarify/sumapi/blob/master/LICENSE) for more details.

[Logo](https://thenounproject.com/search/?q=api&i=719168/) is created by [mikicon](https://thenounproject.com/mikicon/). Licensed under [Creative Commons: By Attribution 3.0 License](https://creativecommons.org/licenses/by/3.0/).
