import os
import sys

bind = 'unix:/root/SeniorProjectF23/app.sock'
workers = 3  # Number of Gunicorn worker processes
errorlog = os.path.join(os.getcwd(), 'gunicorn_error.log')
accesslog = os.path.join(os.getcwd(), 'gunicorn_access.log')

sys.path.append('/root/seniorProjectF23')  # Ensure the correct path to your application

# Specify the module and the callable (Flask app instance)
module = "app"
callable = "app"

# Combine them as "module:callable" for Gunicorn
app = f"{module}:{callable}"
