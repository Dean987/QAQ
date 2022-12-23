firebase_admin.initialize_app(cred)
db = firestore.client()

from flask import Flask, render_template, request
from flask import Flask, render_template, request,make_response, jsonify

app = Flask(__name__)

@app.route("/GG")
@@ -34,6 +35,20 @@ def movie():
      doc_ref.set(doc)


@app.route("/webhook", methods=["POST"])
def webhook():
    # build a request object
    req = request.get_json(force=True)
    # fetch queryResult from json
    action =  req.get("queryResult").get("action")
    msg =  req.get("queryResult").get("queryText")
    info = "動作：" + action + "； 查詢內容：" + msg
    return make_response(jsonify({"fulfillmentText": info}))





@app.route("/search_GG", methods=["POST","GET"])
def search_GG():
    if request.method == "POST":
        GGTitle = request.form["GGTitle"]
        info = ""     
        collection_ref = db.collection("chicken")
        for doc in docs:
            if GGTitle in doc.to_dict()["name"]: 
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