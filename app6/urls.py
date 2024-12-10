from django.urls import path
from .import views
urlpatterns=[path("",views.myform,name="myform"),
             path("path2",views.welcome,name="welcome"),
             path("path1/",views.login_view,name="login_view"),
             path("path3/",views.card,name="card")
]