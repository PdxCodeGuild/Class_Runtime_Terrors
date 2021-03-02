import braintree
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from orders.models import Order
from .tasks import payment_completed
from online_shop.models import Product

gateway = braintree.BraintreeGateway(settings.BRAINTREE_CONF)

def payment_process(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id = order_id)
    total_cost = order.get_total_cost()

    if request.method == 'POST':
        nonce = request.POST.get('payment_method_nonce', None)
        result = gateway.transaction.sale({
            'amount': f'{total_cost:.2f}',
            'payment_method_nonce': nonce,
            'options':{
                'submit_for_settlement': True
            }
        })

        if result.is_success:
            order.paid = True
            order.braintree_id = result.transaction.id
            order.save()
            payment_completed(order.id)
            return redirect('payment:done')
        else:
            return redirect('payment:canceled')
    else:
        print(request)
        client_token = gateway.client_token.generate()
        return render(
            request,
            'payment/process.html',
            {'order': order,
             'client_token': client_token}
        )

def payment_done(request):
    return render(request, 'payment/done.html')

def payment_canceled(request):
    return render(request, 'payment/canceled.html')
