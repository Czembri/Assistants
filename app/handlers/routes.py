from app.handlers import app, db
from flask import render_template, url_for, request, flash, redirect, jsonify, session
from werkzeug.utils import secure_filename
from app.handlers.models import Assistant
import requests
import json
from datetime import date, datetime
from seeder.seedb import Seeder
import base64
import os
from app.handlers.logger import log
from PIL import Image
from app.handlers.models import AlchemyEncoder


def checkRows():
    rows = db.session.query(Assistant).count()
    message = f"""Checking for number of rows in database:
    ['Table':Assistant;
    'Rows:{rows}'] """
    log(message=message, category='debug')
    if rows > 5:
        log(message="No seed needed.", category='info')
    elif rows < 5:
        seed = Seeder(5)
        seed.seed_database()
        log(message="Seeding database with count of rows 5.", category='info')


def getRequest():
    url = 'http://api.dataatwork.org/v1/jobs'
    response = requests.get(url)
    message_request = f"""Sending request to:
    ['url':'{url}';
    'response':'{response}']"""
    log(message=message_request, category='debug')
    parse_json = json.loads(response.text)
    log(message="Parsing json data...", category="info")
    list_of_jobs = []
    for job in parse_json:
        try:
            list_of_jobs.append(job['title'])
        except:
            break
    return set(list_of_jobs)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        try:
            checkRows()
            session.clear()
        except AttributeError as err:
            log(message=f"Could not seed database: ['Error':'{err}']", category='error')

        log(message="Request for: ['Form':'index']", category="debug")
        log(message="Request: ['status':'OK']", category='info')
        table = Assistant.query.all()
    return render_template('index.html', table=table)


@app.route('/create', methods=['POST', 'GET'])
def createAssistant():
    log(message="Request for: ['Form':'createAssistant']", category="debug")
    list_of_jobs = getRequest()

    if request.method == 'POST':
        try:
            first_name = request.form['fname']
            last_name = request.form['lname']
            email = request.form['email']
            occupation = request.form['occupation']
            now = datetime.now()
            date_to_string = now.strftime("%d-%m-%Y %H:%M:%S")

            message_form_request = f"""Sending request for:
            ['firstname':'{first_name}';
            'lastname':'{last_name}';
            'email':'{email}';
            'occupation':'{occupation}';
            'creationdate':'{date_to_string}']"""
            log(message=message_form_request, category='debug')
        except requests.exceptions.RequestException as e:
            flash(f'Error message: {e}', 'error')
            log(f'Error occured: [{e}]', 'error')
            return redirect(request.url)

        # handling files
        file = request.files['file']
        if file.filename == '':
            log(message='File for user not attached.', category='warning')
            unique_file_name = 'default.png'
            file_request_message_1 = f"""Adding default file:
            ['UniqueFileName':'{unique_file_name}']"""
            log(message=file_request_message_1, category='debug')

        else:
            filename = secure_filename(file.filename)
            unique_file_name = f"{first_name}-{last_name}-{filename}"
            file_request_message_2 = f"""Saving file:
            ['Filename':'{filename}';
            'UniqueFileName':'{unique_file_name}']"""
            log(message=file_request_message_2, category='debug')

            try:
                # I am aware of pep8 issue plcaed here
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], unique_file_name))
                image = Image.open(f"{app.config['UPLOAD_FOLDER']}/{unique_file_name}")
                MAX_SIZE = (100, 100)
                image.thumbnail(MAX_SIZE)
                image.save(f"{app.config['UPLOAD_FOLDER']}/{unique_file_name}")
                log(message=f"File saved.", category="info")
            except IOError as e:
                io_file_message = f"""File could not be saved:
                ['Error':{e}]"""
                log(message=io_file_message, category="fatal")

        # saving to database
        # I am aware of pep8 issue plcaed here
        data = Assistant(firstname=first_name, lastname=last_name, email=email, occupation=occupation, creationdate=date_to_string, filename=unique_file_name)
        db.session.add(data)
        db.session.commit()

        save_data_message = f"""Saving data to database.\nData:
        ['firstname':'{first_name}';
        'lastname':'{last_name}';
        'email':'{email}';
        'occupation':'{occupation}';
        'creationdate':'{date_to_string}']"""

        log(message=save_data_message, category="debug")

        flash('The assistant created!', 'success')
        log(message="Assistant created.", category='info')
        return redirect(url_for('index'))

    return render_template('create_assistant.html', jobs=list_of_jobs)


@app.route('/assistant/<int:assistant_id>')
def assistant(assistant_id):
    assistant = Assistant.query.get_or_404(assistant_id)
    return render_template('assistant.html', ass_id=assistant.id, firstname=assistant.firstname, lastname=assistant.lastname, filename=assistant.filename, email=assistant.email, occupation=assistant.occupation, creationdate=assistant.creationdate)


@app.route('/assistant/<int:assistant_id>/edit', methods=['PUT', 'POST', 'GET'])
def editAssistant(assistant_id):
    assistant = Assistant.query.get_or_404(assistant_id)
    now = datetime.now()
    date_to_string = now.strftime("%d-%m-%Y %H:%M:%S")
    list_of_jobs = getRequest()

    log(message="Getting info about an assistant.", category="info")
    info_assistant_message = f"""\nData:
    ['firstname':'{assistant.firstname}';
    'lastname':'{assistant.lastname}';
    'email':'{assistant.email}';
    'occupation':'{assistant.occupation}';
    'creationdate':'{assistant.creationdate}';
    'modificationdate':'{assistant.modificationdate}']"""
    log(message=info_assistant_message, category='debug')
    if request.method == 'POST' or request.method == 'PUT':
        assistant.firstname = request.form['fname']
        assistant.lastname = request.form['lname']
        assistant.email = request.form['email']
        assistant.occupation = request.form['occupation']
        assistant.modificationdate = date_to_string
        db.session.commit()

        log(message='Saving changes to database', category='info')
        flash('Assistant updated', 'success')
        return redirect(url_for('assistant', assistant_id=assistant.id))

    return render_template('editassistant.html', jobs=list_of_jobs, firstname=assistant.firstname, lastname=assistant.lastname, filename=assistant.filename, email=assistant.email, occupation=assistant.occupation, creationdate=assistant.creationdate)


@app.route('/assistant/<int:assistant_id>/delete', methods=['POST'])
def deleteAssistant(assistant_id):
    assistant = Assistant.query.get_or_404(assistant_id)
    db.session.delete(assistant)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/redirect/main')
def redirectToMain():
    return redirect(url_for('index'))


# errors' handlers section
@app.errorhandler(404)
def pageNotFound(e):
    return render_template('404.html'), 404


@app.errorhandler(400)
def badRequest(e):
    return render_template('400.html'), 400


@app.errorhandler(500)
def fail(e):
    return render_template('500.html'), 500
    