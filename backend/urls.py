"""
URL configuration for arb_spotter_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import re_path

from django.contrib import admin
from django.urls import path

from arb_spotter_app import views

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Arb-spotter",
        default_version="v1",
        description="Arb-spotter API documentation",
        license=openapi.License(name="MIT License"),
    ),
    public=True,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/tokens", views.tokens, name="tokens"),
    path("api/v1/tokens/<str:token_id>", views.token_details, name="token details"),
    re_path(r"^api/v1/history/$", views.history, name="ohlcv"),
    re_path(
        r"api/v1/doc",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]
