from django.urls import path
from . import views
app_name="superuser"

urlpatterns=[
    
    path('home/',views.home),
    path('login/',views.login_call),
    path('logout/',views.logout_call),
    path('service/',views.service),
    path('plan/',views.plan),
    path('plan_del/',views.plan_del),
    path('blog/',views.blog),
    
        
]