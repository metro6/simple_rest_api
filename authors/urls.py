from django.urls import path
from . import views


urlpatterns = [
    path('', views.AuthorView.as_view()),
    path('<int:id>/', views.get_authors),
]