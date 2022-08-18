from testapp import db
from datetime import datetime
class Kakeibo(db.Model):
    __tablename__ = "kakeibo"
    id = db.Column(db.Integer, primary_key=True)  # システムで使う番号
    date = db.Column(db.String(255), index=True)  #日付
    is_money = db.Column(db.Boolean)#収入・支出
    title = db.Column(db.String(255))#費目
    number = db.Column(db.Integer, default=0)#金額
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)  # 作成日時
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)  # 更新日時


    