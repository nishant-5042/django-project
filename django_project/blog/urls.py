from django.urls import path
from . import views #since we are using view to display  

urlpatterns = [
    # path('admin/', admin.site.urls),
     path('', views.home, name='blog-home'),
     path('about/', views.about, name='blog-about'),
]