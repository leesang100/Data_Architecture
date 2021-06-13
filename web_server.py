from flask import Flask, render_template, redirect, request, url_for
from pymongo import MongoClient
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def hospital():
    """Flask를 이용한 서버구축. mongoDB에서 데이터를 불러와 화면서 출력하게 한다.
    :return: data in mongoDB
    :rtype: list
    """

    client = MongoClient('mongodb://localhost:27017/')
    db = client.Data_Architecture
    collection = db.Disease
    results = collection.find()
    client.close()
    return render_template('hospital.html', data=results)


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug = True)
