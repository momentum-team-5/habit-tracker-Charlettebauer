"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from core import views as core_views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("registration.backends.simple.urls")),
    path("habits/list", core_views.habits_list, name="habits_list"),
    path("habits/<int:pk>", core_views.habit_details, name="habit_details"),
    path("habits/add", core_views.habit_add, name="habit_add"),
    path("habits/edit", core_views.habit_edit, name="habit_edit"),
    path("habits/<int:pk>/delete", core_views.habit_delete, name="habit_delete"),
    path("record/<int:pk>/<str:date>", core_views.record_add, name="record_add"),
    path(
        "record/habit/<int:habit_pk>/<str:date>",
        core_views.records_list,
        name="records_list",
    ),
    path("record/edit/<int:habit_pk>", core_views.record_edit, name="record_edit"),
    path("", core_views.welcome, name="welcome"),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
