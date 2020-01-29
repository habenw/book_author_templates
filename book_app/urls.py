from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('create_book',views.create_book),
    path('books/<int:book_id>', views.show_books),
    path('add_author/<int:book_id>', views.add_author),
    path('author',views.author),
    path('create_author', views.create_author), 
    path('author/<int:author_id>',views.show_authors),
    path('add_book/<int:author_id>',views.add_book)  
]