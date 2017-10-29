from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$',
        views.MainView.as_view(), name="main-view"),
    url(r'^login/',
        views.UserLoginView.as_view(), name="user-login"),
    url(r'^logout/',
        views.UserLogoutView.as_view(), name="user-logout"),
]
