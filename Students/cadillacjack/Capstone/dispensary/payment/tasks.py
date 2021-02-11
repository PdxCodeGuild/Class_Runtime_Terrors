from io import BytesIO
from celery import task
import weasyprint
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from orders.models import Order

@task
def payment_completed(order_id):
    order = Order.objects.get(id=order_id)

    #generate invoice email
    subject = f'Your CannaSource - EE Invoice Number: {order.id}'
    message = "Attached below is the invoice for you recent purchase from Your CannaSource"
    email = EmailMessage(
        subject,
        message,
        'cadillacjackproductions@gmail.com',
        [order.email],
    )
    #generate PDF
    html = render_to_string('orders/order/pdf.html', {'order': order})
    out = BytesIO()
    
    weasyprint.HTML(string = html).write_pdf(out)

    #attach PDF file
    email.attach(f'order_{order.id}.pdf', out.getvalue(), 'application/pdf')

    #send Email
    email.send()