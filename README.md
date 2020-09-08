# Assistants

<i>Web Application for assistants' managment</i>

* Store all your assistants in one place :+1:

* You decide what you want to do with them :sparkles:

* Add an avatar for your assistant, for better reckognization :sweat_smile:

## Here, you can get info about: 

- App description
- build status
- issues 
- technological stack
- projet news
- partners
- manual
- downloads
- personal contact to the Author
- license
- etc.

> Table of contents

- [Setup](#Setup)
- [Features](#features)
- [Contributing](#contributing)
- [Team](#team)
- [FAQ](#faq)
- [Support](#support)
- [License](#license)


## Functional documentation

### The Application is ready for testing. While you launch it, custom Seeder, seeds database. __More in programming documentation__

* here you find all your assistants

* from this level, you have no access to assistants' edition - to get this access you need to follow instructions contained on the photo down below

![Alt main site](https://user-images.githubusercontent.com/57504533/92333594-1746f980-f087-11ea-9a48-0f9387a058b9.png?raw=true "Title")

* If you choose <b>show details</b> option instead of <b>Create an assistant</b>, your eyes'd see this view

* Let's see what we have here. Hmmm... :cloud: <b>Delete</b> option is obvious, I believe. So we should take care about <b>Edit</b> option. We're gonna talk about it in the next step. :sunny:

![Alt assistant profile](https://user-images.githubusercontent.com/57504533/92333677-b8ce4b00-f087-11ea-80cd-1628c1fe07b3.png?raw=true "Title")

* <b>Edit</b> section allows you to edit your assitant. As you can see, you have a preview for data that is already inserted to database. If you make any changes in textboxes and click <b>Submit</b>, it will cause changes in the database.

![Alt edit assistant](https://user-images.githubusercontent.com/57504533/92333785-7d804c00-f088-11ea-89eb-15e3d885a3ef.png?raw=true "Title")

* And finnaly, we have <b>Create an assistant</b> page. Here you can create your own assistant.

![Alt create assistant](https://user-images.githubusercontent.com/57504533/92333876-27f86f00-f089-11ea-9974-d932b2d72dd4.png?raw=true "Title")





--------

Blank space for updates

--------

## Setup

- Clone this repo to your local machine by using `https://github.com/Czembri/ItSerwis_Merge.git`

- setup your virtual environment by using *python -m venv [name of your virtualenv]*

- install requirements by using *python -m pip install -r requirements.txt*

- run application - *python run.py*

### The application runs at 127.0.0.1:5000

## Addresses

> *'/'* - displays main site - methods = ['GET']

> */create* - displays assistant's addition site - methods = ['GET', 'POST']

> */assistant/<id>* - displays the assistant's details selected by **id** - methods=['GET']
  
> */assistant/<id>/edit* - displays the assistant's edition site - methods=['GET', 'POST']
  
> /assistant/<id>/delete - deletes the assistant selected by **id** - methods=['POST']


## Features

- [x] Complete logging added at */app/log/monitservice.log :camel:

- [x] Some functionality tested

- [x] Added custom seeder - also standard one :dancers:


## Programming documentation

### App folder tree

![Alt tree](https://user-images.githubusercontent.com/57504533/92334222-5297f700-f08c-11ea-9b1d-df5b21e1fcdb.png?raw=true "Title")

> */configuration/config.json* - contains database and files storage settings

> */handlers/static* and */handlers/templates* -contains .html and .css files

> */handlers/__init__.py* - contains **Flask** and **SQLAlchemy** initialization, setups app configuratuon

> */handlers/logger.py* - custom logger

> */handlers/models.py* - database model

> */handlers/routes.py* - contains routes 

* checkRows() - function that counts rows in Assistants table and checks if the count of rows is equal or less than 1; If it s then seed database.

* getRequest() - function that retreive data from *http://api.dataatwork.org/v1/jobs*

* index() - displays main site with generated data from the database

* createAssistant() - displays create assistant's form, inserts new assistant to the database

* assistant() - displays assistant's details - the variable assistant_id is transferred from index form

* editAssistant() - simmilar to **createAssistant()** function with one exception. Textboxes as a value takes inserted data from database.

* deleteAssistant() - deletes an assistant

### Logs

> */log/monitservice.log* - application logs are saved here


### Seeder

> */Seeder/seedb.py* - custom seeder, the file contains class Seeder with one constructor, the class has two methods = ['get_random_date', 'seed_database'] 

* get_random_date(): generates random date for **creationdate** column

* seed_database(): contains all needed data to seed database, adds and commits changes. It takes as a parameter number of assistants, that you want to create.

### Tests

> */Tests/config.py* - the way I have tested JSON strings

> */Tests/response.py* - Retreive data from: http://api.dataatwork.org/v1/jobs

> */Tests/tests.py* - unitests

> */Tests/selenium_tests.py* - Automatic routes testing

## Contributing

> To get started...

### Step 1

- **Option 1**
    - 🍴 Fork this repo!

- **Option 2**
    - 👯 Clone this repo to your local machine using `https://github.com/Czembri/Assistants.git`

### Step 2

- **HACK AWAY!** 🔨🔨🔨

### Step 3

- 🔃 Create a new pull request 

---

## Team

Just me @Czembri 

---

## FAQ

- Not needed yet.
    

---

## Support

Reach out to me at one of the following places!

- via E-mail: <b><a href="" target="_blank">czembri@gmail.com<a></b>
- Facebook at <a href="https://www.facebook.com/ola.czembrowska/" target="_blank">@ola.czembrowska</a>

---

## Donations (Optional)

- Gonna think about it.

---

## License

- This profile owns the application.

