from sqlalchemy.ext.declarative import DeclarativeMeta
from app.handlers import db
from flask_seeder import Seeder, Faker, generator
from datetime import date
import json


class Assistant(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  firstname = db.Column(db.String(60), nullable=False)
  lastname = db.Column(db.String(60), nullable=False)
  email = db.Column(db.String(80), nullable=False)
  occupation = db.Column(db.Text, nullable=False)
  creationdate = db.Column(db.String(20), nullable=False)
  filename = db.Column(db.String(100))
  modificationdate = db.Column(db.String(30), nullable=True)


class DemoSeeder(Seeder):

    def run(self):
        today = date.today()
        faker = Faker(
          cls=Assistant,
          init={
            "id": generator.Sequence(),
            "firstname": generator.Name(),
            "lastname":generator.Name(),
            "email": generator.String(),
            "occupation":generator.String(),
            "creationdate":today,
            "filename":"default.png"
          }
        )

        for assistant in faker.create(5):
          print("Adding assistant: %s" % Assistant)
          self.db.session.add(assistant)


class AlchemyEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            # an SQLAlchemy class
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                data = obj.__getattribute__(field)
                try:
                    json.dumps(data)
                    fields[field] = data
                except TypeError:
                    fields[field] = None
            return fields

        return json.JSONEncoder.default(self, obj)