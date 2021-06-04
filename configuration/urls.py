from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from dj_rest_auth.registration.views import ConfirmEmailView

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from accounts.views import FacebookLogin
urlpatterns = [
    path("i18n/", include("django.conf.urls.i18n")),
    path("admin/", admin.site.urls),
]
urlpatterns += (
    i18n_patterns(
        path("", TemplateView.as_view(template_name="home.html"), name="home"),
        path("accounts/", include("accounts.urls")),
        path("accounts/", include("allauth.urls")),
        path("streams/", include("events.urls")),
        path('accounts/login/callback', include('social_django.urls', namespace='social')),
        path("api/v1/auth/", include("dj_rest_auth.urls")),
        path(
            "api/v1/auth/registration/account-confirm-email/<str:key>/",
            ConfirmEmailView.as_view(),
            name="account_confirm",
        ),
        path("api/v1/auth/registration/", include("dj_rest_auth.registration.urls")),
        path('api/v1/auth/facebook/', FacebookLogin.as_view(), name='fb_login'),
        prefix_default_language=False,
    )
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)
