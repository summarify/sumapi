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
from sumapi.api import SumAPI

api = SumAPI(username='<your_username>', password='<your_password')
# {'access_token': 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX', 'token_type': 'bearer'}
```

**Sentiment Analysis**

```python
from sumapi.api import SumAPI

api = SumAPI(username='<your_username>', password='<your_password')

api.sentiment_analysis('Bu harika bir filmdi.', domain='general')
# {'body': 'Bu harika bir filmdi.', 'evaluation': {'label': 'positive', 'score': 0.983938992023468}}

```

**Named Entitity Recognition**

```python
from sumapi.api import SumAPI

api = SumAPI(username='<your_username>', password='<your_password')

api.named_entity_recognition("Mustafa Kemal Atatürk 19 Mayıs 1919'da Samsun'a ayak bastı.", domain='general')
#{
#  "body": "Mustafa Kemal Atatürk 19 Mayıs 1919'da Samsun'a ayak bastı.",
#  "evaluation": {
#    "text": "Mustafa Kemal Atatürk 19 Mayıs 1919 ' da Samsun ' a ayak bastı . ",
#    "labels": [
#      [
#        0,
#        7,
#        "B-Person",
#        0.9994454979896545
#      ],
#      [
#        8,
#        13,
#        "I-Person",
#        0.999332070350647
#      ],
#      [
#        14,
#        21,
#        "I-Person",
#        0.999338686466217
#      ],
#      [
#        22,
#        24,
#        "B-Date",
#        0.8490145802497864
#      ],
#      [
#        25,
#        30,
#        "I-Date",
#        0.8429246544837952
#      ],
#      [
#        31,
#        35,
#        "I-Date",
#        0.779156506061554
#      ],
#      [
#        41,
#        47,
#        "B-Location",
#        0.9813851118087769
#      ]
#    ]
#  }
#} """
```

**Classification**

```python
from sumapi.api import SumAPI

api = SumAPI(username='<your_username>', password='<your_password')

api.classification("GPT-3, Elon Musk ve Sam Altman tarafından kurulan OpenAI'in üzerinde birkaç yıldır çalışma yürüttüğü bir yapay zekâ teknolojisi", domain='general')
# {'body': "GPT-3, Elon Musk ve Sam Altman tarafından kurulan OpenAI'in üzerinde birkaç yıldır çalışma yürüttüğü bir yapay zekâ teknolojisi", 'evaluation': {'label': 'technology', 'score': 0.9983301758766174}}

api.classification('Bankanızdan hiç memnun değilim, kredi ürününüz iyi çalışmıyor.', domain='finance')
# {'body': 'Bankanızdan hiç memnun değilim, kredi ürününüz iyi çalışmıyor.', 'evaluation': {'label': 'kredi'}}
```

**Summarization**

```python
from sumapi.api import SumAPI

api = SumAPI(username='<your_username>', password='<your_password')

sample_text = "First of all, numerous software patches must be conducted to keep systems up to date. Cyber ​​attackers that use malware are trying to infiltrate company networks via abusing some undetected vulnerabilities within their software. According to a survey by security company Tripwire, one in three IT professionals said their company was infiltrated through an unpatched vulnerability. Thus, the validity of the patches should be constantly in check. Secondly, the devices that are connected to the network should be frequently monitored. Recognizing requests from devices that are connected to the main network is one of the most important areas of protection against malware. If the monitoring is missed, an evil ransomware gang can detect some vulnerabilities of the remote access doors. The more preferable scenario is having ethical hackers discover those potentially infected computers. Moreover, the most important data should be determined and an effective backup strategy should be implemented. It is very important to operate backups of important data to protect it against cyber attackers. If crypto ransomware enters the system and captures some devices, the data can be restored thanks to a recent backup, and the related devices can become operational in a short time. Yet, the first move of a hacker is almost always to cut access to those backups, so strong protection of those backups is also essential."

api.summarization(text=sample_text, percentage=0.5, domain='SumBasic')     
api.summarization(text=sample_text, percentage=0.5, domain='SumComplex')
api.summarization(text=sample_text, word_count=100, domain='SumDeep')
```

**Spell Check**

```python           
from sumapi.api import SumAPI

api = SumAPI(username='<your_username>', password='<your_password')

api.spell_check('bu hstali cumle duzelexek gibi dutuyor.', domain='general')
#{
#  "body": "bu hstali cumle duzelexek gibi dutuyor.",
#  "evaluation": {
#    "evaluation": "bu hatalı cümle düzelecek gibi duruyor "
#  }
#}
```

**Offensive Language Detection**
```python
from sumapi.api import SumAPI

api = SumAPI(username='<your_username>', password='<your_password')

api.offensive_lang_detection("hapisten çıkarsa gideceği tek yer musalla taşı olur tüm teröristlerle birlikte geber", domain='general')
# {'body': 'Bu harika bir filmdi.', 'evaluation': {'label': 'Ofansif', 'score': 0.99938481321}}
```

**Zero Shot Classification**

```python
from sumapi.api import SumAPI

api = SumAPI(username='<your_username>', password='<your_password')

api.zero_shot_classification('Bu nasıl bir hizmet, gerçekten rezilsiniz.', categories='talep,şikayet,öneri')
# {'body': 'Bu nasıl bir hizmet, gerçekten rezilsiniz.', 'evaluation': {'sequence': 'Bu nasıl bir hizmet, gerçekten rezilsiniz.', 'labels': ['şikayet', 'öneri', 'talep'], 'scores': [0.97139573097229, 0.8201411962509155, 0.5891757011413574], 'label': 'şikayet'}}
```

**Question Answering**

```python
from sumapi.api import SumAPI

api = SumAPI(username='<your_username>', password='<your_password')

context = """ABASIYANIK, Sait Faik. Hikayeci (Adapazarı 23 Kasım 1906-İstanbul 11 Mayıs 1954). İlk öğrenimine Adapazarı’nda Rehber-i Terakki Mektebi’nde başladı. İki yıl kadar Adapazarı İdadisi’nde okudu. İstanbul Erkek Lisesi’nde devam ettiği orta öğrenimini Bursa Lisesi’nde tamamladı (1928). İstanbul Edebiyat Fakültesi’ne iki yıl devam ettikten sonra babasının isteği üzerine iktisat öğrenimi için İsviçre’ye gitti. Kısa süre sonra iktisat öğrenimini bırakarak Lozan’dan Grenoble’a geçti. Üç yıl başıboş bir edebiyat öğrenimi gördükten sonra babası tarafından geri çağrıldı (1933). Bir müddet Halıcıoğlu Ermeni Yetim Mektebi'nde Türkçe grup dersleri öğretmenliği yaptı. Ticarete atıldıysa da tutunamadı. Bir ay Haber gazetesinde adliye muhabirliği yaptı (1942). Babasının ölümü üzerine aileden kalan emlakin geliri ile avare bir hayata başladı. Evlenemedi. Yazları Burgaz adasındaki köşklerinde, kışları Şişli’deki apartmanlarında annesi ile beraber geçen bu fazla içkili bohem hayatı ömrünün sonuna kadar sürdü."""

api.question_answering(context=context, question="Sait Faik nerede doğdu?")
# {'body': 'Sait Faik nerede doğdu?', 'evaluation': {'score': 0.9611985087394714, 'answer': 'Adapazarı'}}
```

**Multi Argument**

```python
from sumapi.api import SumAPI
import pandas as pd

api = SumAPI(username='<your_username>', password='<your_password')

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
            "domain": "content"
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
