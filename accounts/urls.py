from django.urls import path

from accounts import views

urlpatterns = [
    path("<int:pk>/", views.AccountDetailView.as_view(), name="account_detail"),
    path("<int:pk>/edit/", views.AccountUpdateView.as_view(), name="account_edit"),
]
