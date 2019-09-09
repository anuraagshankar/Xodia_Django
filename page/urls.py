from django.conf.urls import url
from django.contrib import admin
from . import views

app_name = 'page'

urlpatterns = [
    # .../page/
    url(r'^$', views.Index.as_view(), name='Index'),
    # .../page/signup/
    url(r'^signup/', views.Signup.as_view(), name='Signup'),
    # .../page/login/
    url(r'^login/', views.Login.as_view(), name='Login'),

    url(r'^admin/', admin.site.urls),
]
