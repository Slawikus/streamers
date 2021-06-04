from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from events.models import Product


class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = "events/product_list.html"
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(user=self.request.user)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)

        products = self.get_queryset().all()

        context["products_qty"] = products.count()
        context["total_sold_qty"] = sum([product.qty_sold() for product in products])
        context["total_revenue"] = sum([product.revenue() for product in products])

        average_revenue_per_product = context["total_revenue"] / context["products_qty"] if context["products_qty"] > 0 else 0

        context["average_revenue_per_product"] = str(round(average_revenue_per_product, 2))

        return context
