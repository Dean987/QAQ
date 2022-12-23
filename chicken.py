import requests
from bs4 import BeautifulSoup


import firebase_admin
from firebase_admin import credentials, firestore
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/GG")
def movie():
    url = "https://www.cheogajip.com.tw/menu/"
    Data = requests.get(url)
    Data.endcoding = "utf-8"
    sp = BeautifulSoup(Data.text, "html.parser")
    meals=sp.select(".rightBox .Txt ")
    for t in meals:
      name=t.find("a").get("title")
      say=t.find("p").text
      hyperlink=t.find("a").get("href")
      print(name + ":" + say)
      doc = {
          "name": name,
          "say": say,
          "hyperlink": hyperlink,

      }

      doc_ref = db.collection("chicken")
      doc_ref.set(doc)


@app.route("/search_GG", methods=["POST","GET"])
def search_GG():
    if request.method == "POST":
        GGTitle = request.form["GGTitle"]
        info = ""     
        collection_ref = db.collection("chicken")
        for doc in docs:
            if GG in doc.to_dict()["name"]: 
                info += "品名：<a target = _blank href=" + doc.to_dict()["hyperlink"] + ">" + doc.to_dict()["name"] + "</a>" + "<br>" 
                info += "產品介紹：" + doc.to_dict()["say"] + "<br><br>"
        if info == "":
            info += "抱歉，查無相關條件的產品資訊</a>" 
        return info
    else:  
        return render_template("search_GG.html")

@app.route("/")
def index():
    homepage = "<h1>起家雞 Python 網頁</h1>"
    homepage += "<a href=/search_GG target = _blank>GG查詢</a><br>"
    return homepage
