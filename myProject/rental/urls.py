
from . import views
from django.urls import path


urlpatterns = [
    path('member/',views.member,name='member'),
    path('staff/',views.staff,name='staff')
]
