from django.urls import path
from .views import *

urlpatterns =[
    path('',Home.as_view(),name='home'),
    path('signup',Signup.as_view(),name="signup"),
    path('login/',Login.as_view(),name="login"),
    path('logout',Logout.as_view(),name='logout'),
    path('inbox',Inbox.as_view(),name="inbox"),
    path('sent',Sent.as_view(),name="sent"),
    path('massege',Masseges.as_view(),name='massege'),
    path('msgdetail/<int:pk>',DetailsMsg.as_view(),name="msgdetail"),

]