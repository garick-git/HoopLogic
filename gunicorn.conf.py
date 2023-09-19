import os

bind = '0.0.0.0:8000'  # Your binding address
workers = 3  # Number of Gunicorn worker processes
errorlog = os.path.join(os.getcwd(), 'gunicorn_error.log')
accesslog = os.path.join(os.getcwd(), 'gunicorn_access.log')


app = "app:app"