web: gunicorn project_resume.wsgi:application --chdir src
web: python src/manage.py collectstatic --noinput && gunicorn project_resume.wsgi:application --chdir src --log-file -