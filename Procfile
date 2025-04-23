web: gunicorn project_resume.wsgi:application --chdir src
web: python manage.py collectstatic --noinput && gunicorn project_resume.wsgi:application --log-file -