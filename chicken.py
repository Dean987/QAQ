import firebase_admin
from firebase_admin import credentials, firestore
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()


import requests
from bs4 import BeautifulSoup
url = "https://www.cheogajip.com.tw/menu/"
Data = requests.get(url)
Data.endcoding = "utf-8"
sp = BeautifulSoup(Data.text, "html.parser")
meals=sp.select(".rightBox .Txt ")
for t in meals:
      name=t.find("a").get("title")
      say=t.find("p").text
      taste=t.find("p").text
      hyperlink=t.find("a").get("href")
      print(name + ":" + say)
      if "辣" in say:
         taste ="辣"
      else:
         taste = "不辣"

      doc = {
          "name": name,
          "say": say,
          "hyperlink": hyperlink,
          "taste": taste,

      }

      doc_ref = db.collection("chicken1")
      doc_ref.set(doc)


