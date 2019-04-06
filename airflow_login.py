import airflow
import os
from airflow import models, settings
from airflow.contrib.auth.backends.password_auth import PasswordUser
user = PasswordUser(models.User())
user.username = os.environ['ADMIN_USER']
user.email = os.environ['ADMIN_EMAIL']
user.password = os.environ['ADMIN_PWD']
session = settings.Session()
session.add(user)
session.commit()
session.close()
exit()
