import os
import sys

bind = 'unix:/root/SeniorProjectF23/app.sock'
workers = 3  # Number of Gunicorn worker processes
errorlog = os.path.join(os.getcwd(), 'gunicorn_error.log')
accesslog = os.path.join(os.getcwd(), 'gunicorn_access.log')


sys.path.append('/root/seniorProjectF23')
app = "app:app"