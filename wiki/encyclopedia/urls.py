from django.urls import path

from . import views
app_name="encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("search", views.search, name="search"),
    path("add_entry", views.add_entry, name="add_entry"),
    path("random_page", views.random_page, name="random_page"),
    path('edit_entry/<str:title>/', views.edit_entry, name='edit_entry'),
    path("<str:title>", views.entry_page, name="entry_page"),

]
