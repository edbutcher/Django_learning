from django.conf.urls import url, include
from django.contrib import admin
from basic_app import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view()),
    url(r'^admin/', admin.site.urls),
    url(r'^basic_app/', include('basic_app.urls', namespace='basic_app')),
]
