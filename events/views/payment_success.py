from django.views.generic import TemplateView


class PaymentSuccessView(TemplateView):
    template_name = 'events/payment_success.html'
