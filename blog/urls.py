from django.urls import path
from . import views#will import views from . i.e the blogs folder
app_name='blog'
urlpatterns = [
    
    path('', views.all_blogs, name='all_blogs'),
    path('<int:blog_id>/', views.detail, name='detail'),
    
]
