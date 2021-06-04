from django.views.generic import DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import CustomUser
from .forms import CustomUserChangeForm

from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView


class AccountDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = CustomUser
    template_name = "account/account_detail.html"
    context_object_name = "user"

    def test_func(self):
        return self.get_object() == self.request.user

    def handle_no_permission(self):
        return HttpResponseRedirect(reverse("home"))


class AccountUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    form_class = CustomUserChangeForm
    model = CustomUser
    template_name = "account/account_edit.html"

    def test_func(self):
        return self.get_object() == self.request.user

    def handle_no_permission(self):
        return HttpResponseRedirect(reverse("home"))

class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter
