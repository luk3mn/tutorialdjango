from django.urls import path

from . import views

# Para referenciar as urls do arquivo
app_name = "blog"

# lista padrão de urls
urlpatterns = [
    path("", views.PostListView.as_view(), name="list"),
    path("<slug:slug>/", views.PostDetailView.as_view(), name="detail"),
]