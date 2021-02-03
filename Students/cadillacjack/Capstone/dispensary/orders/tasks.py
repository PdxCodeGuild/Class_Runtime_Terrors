from celery import task
from django.core.mail import send_mail
from .models import Order

@task
def order_created(order_id):
    order = Order.objects.get(id=order_id)
    subject = f'Your order is bein processed. Order number: {order.id}'
    message = f'''
    Congratulations {order.first_name},\n\n \
    Your order has been successfully submitted. \
    Your order ID is {order.id}.
    '''

    mail_sent = send_mail(
        subject,
        message,
        'admin@dispensary.com',
        [order.email]
    )

    return mail_sent
