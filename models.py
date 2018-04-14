import datetime
import uuid
from peewee import *

db = PostgresqlDatabase('postgres', user='dev', password='dev', host='localhost')


class Ticker(Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4())
    last = FloatField()
    bid = FloatField()
    ask = FloatField()
    high = FloatField()
    low = FloatField()
    volume = FloatField()
    timestamp = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db

class Candle(Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4())


db.create_tables([Ticker], True)
