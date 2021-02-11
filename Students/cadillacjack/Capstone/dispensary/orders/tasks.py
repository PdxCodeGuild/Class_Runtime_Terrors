from celery import task
from django.core.mail import send_mail
from .models import Order
import os
from dotenv import load_dotenv

@task
def order_created(order_id):
    order = Order.objects.get(id=order_id)
    subject = f'Your order is being processed. Order number: {order.id}'
    message = f'''
    Congratulations {order.first_name},\n\n \
    Your order has been successfully submitted. \
    Your order ID is {order.id}.
    '''
    host_email = os.getenv('EMAIL_HOST_USER')
    mail_sent = send_mail(
        subject,
        message,
        host_email,
        [order.email],
        fail_silently=False
    )

    return mail_sent
