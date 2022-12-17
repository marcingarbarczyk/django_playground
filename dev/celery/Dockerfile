FROM django_playground:latest

RUN chmod 777 /home/app/django/dev/celery/entrypoint.sh

USER app
CMD ["/bin/bash", "-c", "/home/app/django/dev/celery/entrypoint.sh"]