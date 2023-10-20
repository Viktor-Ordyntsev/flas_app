import os
from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import requests

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://root:root@postgres_db:5432/question_db'
db = SQLAlchemy(app)


class Questions(db.Model):
    __tablename__ = 'Questions'
    ID = db.Column(db.Integer, primary_key=True)
    id_question = db.Column(db.Integer)
    question = db.Column(db.String(1024))
    answer = db.Column(db.String(1024))
    date_create = db.Column(db.DateTime)

with app.app_context():
    db.create_all()


@app.route("/", methods=['GET'])
def main_page():
    return render_template('index.html')

@app.route("/success", methods=['GET', 'POST'])
def page():
    if request.method == 'POST':
        questions_num = int(request.form['questions_num'])
        answer = requests.get(f"https://jservice.io/api/random?count={questions_num}").json()
        for answer_json in answer:
            id = answer_json["id"]
            que = answer_json["question"]
            answ = answer_json["answer"]
            date_cr = answer_json["created_at"]

            exists = db.session.query(Questions.ID).filter_by(ID=id).first() is not None
            if not exists:
                question_test = Questions(id_question=id, question=que, answer=answ, date_create=date_cr)
                db.session.add(question_test)
                db.session.commit()
            else: 
                while exists:
                    answer_w = requests.get(f"https://jservice.io/api/random?count=1").json()[0]
                    id_w = answer_w["id"]
                    que_w = answer_w["question"]
                    answ_w = answer_w["answer"]
                    date_cr_w = answer_w["created_at"]

                    exists = db.session.query(Questions.ID).filter_by(ID=id_w).first() is not None
                else:
                    question_w = Questions(ID=id_w, question=que_w, answer=answ_w, date_create=date_cr_w)
                    db.session.add(question_w)
                    db.session.commit()

    answer_on_query = db.session.query(Questions).order_by(Questions.ID.desc()).first()           
    flash(f"Вопрос:\n{answer_on_query.question}? \nОтвет:\n{answer_on_query.answer} \nДата создания:\n{answer_on_query.date_create}", category="info")
    return redirect(url_for('main_page'))

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
