from flask import render_template
from app import app, mail, logger
from flask_mail import Message
import os

APP_NAME = os.environ.get("APP_NAME")
LOGO_URL = os.environ.get("PROD_APP_LOGO_URL")
APP_SUPPORT_EMAIL = os.environ.get("APP_SUPPORT_EMAIL")

def confirmation_email(email, user_name, verification_link_app):
    with app.app_context():
        try:
            print(verification_link_app)
            subject = f'Hi {user_name}, please verify your {APP_NAME} account'
            html_body = render_template('verification_email.html', user_name=user_name, verification_link=verification_link_app,
                                        logo=LOGO_URL, support_email=APP_SUPPORT_EMAIL, app_name=APP_NAME)
            msg = Message(subject, recipients=[email], html=html_body)
            mail.send(msg)
            logger.info(f"Verification email to - {email} sent successfully")
        except Exception as e:
            mail.send(e)
            logger.error(f'Error sending email: {e}')


def welcome_email(email, user_name, app_link):
    with app.app_context():
        try:
            subject = f'Welcome to {APP_NAME}!'
            html_body = render_template('welcome_email.html', user_name=user_name, app_link=app_link,
                                        logo=LOGO_URL, support_email=APP_SUPPORT_EMAIL, app_name=APP_NAME)
            msg = Message(subject, recipients=[email], html=html_body)
            mail.send(msg)
            logger.info(f"Welcome email to - {email} sent successfully")
        except Exception as e:
            logger.error(f'Error sending email: {e}')


def reset_password_email(email, user_name, verification_link):
    with app.app_context():
        try:
            subject = 'Aipixy Password Reset Request'
            html_body = render_template('reset_password_email.html', user_name=user_name, verification_link=verification_link,
                                        logo=f'{os.environ.get("PROD_APP_LOGO_URL")}')
            msg = Message(subject, recipients=[email], html=html_body)
            mail.send(msg)
            logger.info(f"Rest password email to - {email} sent successfully")
        except Exception as e:
            logger.error(f'Error sending email: {e}')


def password_change_email(email, user_name, change_password_url):
    with app.app_context():
        try:
            subject = f'{user_name}, your password was successfully reset'
            html_body = render_template('password_changed_email.html', user_name=user_name,
                                        logo=f'{os.environ.get("PROD_APP_LOGO_URL")}', change_password_url=change_password_url)
            msg = Message(subject, recipients=[email], html=html_body)
            mail.send(msg)
            logger.info(f"Password changed email to - {email} sent successfully")
        except Exception as e:
            logger.error(f'Error sending email: {e}')