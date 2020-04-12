
from django.urls import path

from . import views
app_name='blog'
urlpatterns = [
    
    path('', views.all_blogs,name='all_blogs'),
    path('<int:blog_id>/', views.detail,name='detail'), # irst argument say that if anyone pass a integer a
    #fter blog i want to represent integer with blog_id and pass it forward to detail
 ]
#urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)