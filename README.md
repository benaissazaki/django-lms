# Learning management system using django web framework

Feature-rich learning management system. Let's enhance the project by contributing! 👩‍💻👩‍💻

- Demo video: https://youtu.be/KKIeRXwZ-Sw *Please note that the video does not showcase the latest updates on UI design and backend functionality.*
- Setup video: https://youtu.be/gMJfENDEyUs

![Screenshot from 2023-12-31 17-36-31](https://github.com/adilmohak/django-lms/assets/60693922/e7fb628a-6275-4160-ae0f-ab27099ab3ca)

Current features
----------------
* News And Events
* The admin can Add Students
* The admin can Add Lecturers
* Students can Add and Drop courses
* Lecturers submit students score (Attendance, Mid exam, Final exam, assignment)
* The system calculat students Total, Avarage, point, and grade automaticaly
* Also, the system tells the student whether he/she pass, fail or pass with a warning
* Assessment result
* Grade result
* Upload video and documentations for each course
* PDF generator for students registration slip and grade result
* Storing of quiz results under each user
* Question order randomisation
* Previous quiz scores can be viewed on category page
* Correct answers can be shown after each question or all at once at the end
* Logged in users can return to an incomplete quiz to finish it and non-logged in users can complete a quiz if their session persists
* The quiz can be limited to one attempt per user
* Questions can be given a category
* Success rate for each category can be monitored on a progress page
* Explanation for each question result can be given
* Pass marks can be set
* Multiple choice question type
* True/False question type
* Essay question type
* Custom message displayed for those that pass or fail a quiz
* Custom permission (view_sittings) added, allowing users with that permission to view quiz results from users
* A marking page which lists completed quizzes, can be filtered by quiz or user, and is used to mark essay questions

# Pre-requisites:

> The following programs are required to run the project

- [Python3.8+](https://www.python.org/downloads/)
- [PostgreSQL database](https://www.postgresql.org/download/)

# Installation

- Clone the repo with

```bash
git clone https://github.com/adilmohak/django-lms.git
```

- Create and activate a python virtual environment

```bash
pip install -r requirements.txt
```

- Create `.env` file inside the root directory and include the following variables

```bash
DB_NAME=[YOUR_DB_NAME]
DB_USER=[DB_ADMIN_NAME]
DB_PASSWORD=[DB_ADMIN_PASSWORD]
DB_HOST=localhost
DB_PORT=[YOUR_POSTGRES_PORT default is 5432]
USER_EMAIL=[YOUR_EMAIL]
USER_PASSWORD=[EMAIL_PASSWORD]
DEBUG=True
SECRET_KEY=[YOUR_SECRET_KEY]
```

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

```bash
python manage.py runserver
```

Last but not least, go to this address http://127.0.0.1:8000

### References
- Quiz part: https://github.com/tomwalker/django_quiz

# Connect with me

<div>
<a href="https://www.linkedin.com/in/adilmohak" target="_blank">
<img src=https://img.shields.io/badge/linkedin-%231E77B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white alt=linkedin style="margin-bottom: 5px;" />
</a>
<a href="https://github.com/adilmohak" target="_blank">
<img src=https://img.shields.io/badge/github-%2324292e.svg?&style=for-the-badge&logo=github&logoColor=white alt=github style="margin-bottom: 5px;" />
</a>
<a href="https://stackoverflow.com/users/12872688/adil-mohak" target="_blank">
<img src=https://img.shields.io/badge/stackoverflow-%23F28032.svg?&style=for-the-badge&logo=stackoverflow&logoColor=white alt=stackoverflow style="margin-bottom: 5px;" />
</a>
<a href="https://www.facebook.com/adilmohak1" target="_blank">
<img src=https://img.shields.io/badge/facebook-%232E87FB.svg?&style=for-the-badge&logo=facebook&logoColor=white alt=facebook style="margin-bottom: 5px;" />
</a>
</div>

### Show your support by ⭐️ this project!
