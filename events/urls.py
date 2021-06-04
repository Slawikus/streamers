from django.urls import path
from events import views

urlpatterns = [
    path("", views.EventListView.as_view(), name="event_list"),
    path("past/", views.MyEventListView.as_view(), name="my_events"),
    path(
        "share/<uuid:shareable_id>/",
        views.EventPublicDetailView.as_view(),
        name="public_event_detail_view",
    ),
    path("new/", views.EventCreateView.as_view(), name="event_new"),
    path("<int:pk>/", views.EventDetailView.as_view(), name="event_detail"),
    path("<int:pk>/edit/", views.EventUpdateView.as_view(), name="event_edit"),
    path("<int:pk>/delete/", views.EventDeleteView.as_view(), name="event_delete"),
    path("products/new/", views.ProductCreateView.as_view(), name="product_create"),
    path("products/", views.ProductListView.as_view(), name="product_list"),
    path("<int:pk>/product/delete/", views.ProductDeleteView.as_view(), name="product_delete"),
    path("<int:pk>/product/edit/", views.ProductUpdateView.as_view(), name="product_update"),
    path("payment-success/", views.PaymentSuccessView.as_view(), name="payment_success"),
    path("orders/", views.OrderListView.as_view(), name="order_list"),
    path("dashboard/", views.DashboardListView.as_view(), name="dashboard_list"),

]
