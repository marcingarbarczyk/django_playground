# Django playground project

Run project Django with all basic components. Ready for training and testing.

Features:

* Docker
* Node modules support
* SCSS compiler
* CSS / JS minifier
* Elastic Search
* Redis
* Postgres
* Crispy forms
* Django extensions
* User model extended

1. Build images for django and celery. Go to folder dev and run command: ./build.sh
2. Go back and just run docker-compose up -d
3. Go to http://localhost:81
4. Run: docker exec -it django-playground bash
5. Run: python manage.py createsuperuser
6. Run: python manage.py seed blog --number=1000
7. Run: python manage.py seed books --number=1000
8. Run: python manage.py seed shop --number=1000