from celery import task
from django.core.mail import send_mail
from .models import Order

#celery task
#task is suppose to send an email to user for order confirmation
#suppose to run asynchronously with the application
#if it doesn't run asynchronously the app would lag and will not
#load the next page until the command is completed
#hence, why it was necessary for this function to run asynchronously

@task
def order_created(order_id):
    """
    Task to send an e-mail notification when an order is successfully created.
    """
    order = Order.objects.get(id=order_id)
    subject = 'Order nr. {}'.format(order.id)
    message = 'Dear {},\n\nYou have successfully placed an order. Your order id is {}.'.format(order.first_name,
                                                                             order.id)
    mail_sent = send_mail(subject, message, 'admin@build.r.io', [order.email])
    return mail_sent
