from flask import *
from testapp import app,db
from testapp.models.kakeibo import Kakeibo
import numpy as np
import json
from datetime import datetime
from sqlalchemy.sql import func
@app.route('/')
def index():
    my_dict = {
        'insert_something1': 'views.pyのinsert_something1部分です。',
        'insert_something2': 'views.pyのinsert_something2部分です。',
        'test_titles': ['title1', 'title2', 'title3']
    }
    return render_template('testapp/index.html', my_dict=my_dict)

@app.route("/test")
def other1():
    return "テストページ"

@app.route('/sampleform', methods=['GET', 'POST'])
def sample_form():
    if request.method == 'GET':
        return render_template('testapp/sampleform.html')
    if request.method == 'POST':
        req1 = request.form['data1']
        req2 = request.form['data2']
        int_req1 = int(req1)
        int_req2 = int(req2)
        ans = int_req1 + int_req2
        return_json={
            "ans": request.form["ans"]
        }
        return jsonify(values=json.dumps(return_json))

@app.route("/list")
def list():
    kakeibos=Kakeibo.query.all()
    summary = db.session.query(func.sum(Kakeibo.number)).first()[0]
    insum=0
    outsum=0
    for data in kakeibos:
        if data.is_money:
            insum += data.number
        else:
            outsum += data.number
    print(insum)
    print(outsum)
    print(summary)
    data = {
        "kakeibos": kakeibos,
        "insum": insum,
        "summary": summary,
        "outsum": outsum
    }
    return render_template("testapp/list.html", data=data)

@app.route("/add", methods=["GET","POST"])
def add():
    if request.method == "GET":
        return render_template("testapp/add.html")
    if request.method == "POST":
        form_date = request.form.get('date')
        print(form_date)
        form_is_money = request.form.get('is_money', default=False, type=bool)
        # form_is_money = convert_to_bool(request.args.get("is_money"),False)
        form_title = request.form.get('title')
        if form_is_money:
            form_number = request.form.get('number', default=0, type=int) 
        else:
            form_number = request.form.get('number', default=0, type=int) 
            form_number *= -1
            print(form_number)
        kakeibo = Kakeibo(
            date=form_date,
            is_money=form_is_money,
            title=form_title,
            number=form_number,
        )        
        db.session.add(kakeibo)
        db.session.commit()
        return redirect(url_for("list"))
        

@app.route("/kakeibo/<int:id>")
def detail(id):
    kakeibo = Kakeibo.query.get(id)
    return render_template("testapp/detail.html", kakeibo=kakeibo)

@app.route("/kakeibo/<int:id>/edit")
def edit(id):
    kakeibo = Kakeibo.query.get(id)
    return render_template("testapp/edit.html", kakeibo=kakeibo)

@app.route("/kakeibo/<int:id>/update", methods=["POST"])
def update(id):
    kakeibo=Kakeibo.query.get(id)
    kakeibo.date=request.form.get("date")
    kakeibo.is_money=request.form.get("is_money",type=bool)
    kakeibo.title=request.form.get("title")
    kakeibo.number=request.form.get("number")
    db.session.merge(kakeibo)
    db.session.commit()
    return redirect(url_for("list"))

@app.route("/kakeibos/<int:id>/delete", methods=["POST"])

def delete(id):
    kakeibo=Kakeibo.query.get(id)
    db.session.delete(kakeibo)
    db.session.commit()
    return redirect(url_for("list"))