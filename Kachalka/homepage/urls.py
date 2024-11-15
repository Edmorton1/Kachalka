from django.urls import path
from . import views

app_name = 'homepage'

urlpatterns = [
    path('', views.index, name='index'),
    path('records_add/', views.radd, name='radd'),
    path('<int:pk>/records_edit/', views.radd, name='edit'),
    path('<int:pk>/records_delete/', views.rdelete, name='rdelete'),
    path('statis_add/', views.sadd, name='sadd'),
    path('<int:pk>/statis_edit', views.sadd, name='sedit'),
    path('<int:pk>/statis_delete/', views.sdelete, name='sdelete'),
    path('<int:pk>/userhref_add/', views.userhref, name='userhref_add')
]
