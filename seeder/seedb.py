from app.handlers import db
from app.handlers.models import Assistant
import json
import requests
from datetime import date, datetime
import random


class Seeder:
    def __init__(self, number_of_inserts):
        self.number_of_inserts = number_of_inserts

    def get_random_date(self):

    # try to get a date
        try:
            return datetime.strptime('{} {}'.format(random.randint(1, 366), 2020), '%j %Y')

        # if the value happens to be in the leap year range, try again
        except ValueError:
            get_random_date(2020)


    def seed_database(self):
        url = 'http://api.dataatwork.org/v1/jobs'
        response = requests.get(url).text
        parse_json = json.loads(response)

        listOfJobs = []
        for job in parse_json:
            try:
                listOfJobs.append(job['title'])
            except:
                break

        data = {
            'fname': ['Aleksandra', 'Monika', 'Kasia', 'Anna', 'Cathrine', 'Kayle', 'Chris', 'Antek', 'Mambo', 'Krystian', 'Dominik', 'Patrycja'],
            'lname':['Marine', 'Zebra', 'Obra', 'Myśliwiec', 'Antoninek', 'Karoliewicz', 'Smith', 'Swayze'],
            'filename':['default.png', 'another.jpg']
        }



        for i in range(self.number_of_inserts):
            random_fname = random.choice(data['fname'])
            random_lname = random.choice(data['lname'])
            random_filename = random.choice(data['filename'])
            mail = f"{random_fname}.{random_lname}@gmail.com"
            jobs = random.choice(listOfJobs)
            date = self.get_random_date()
            insert_data = Assistant(firstname=random_fname, lastname=random_lname, email=mail, occupation=jobs, creationdate=date, filename=random_filename)
            db.session.add(insert_data)
            db.session.commit()



seeder = Seeder(5)
seeder.seed_database()