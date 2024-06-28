from django.urls import path, include
from .views import BookListView, BookCreateView, UserRegistrationView

urlpatterns = [
    path('', BookListView.as_view(), name='book-list'),
    path('create-book/', BookCreateView.as_view(), name='create-book'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('users/', include('django.contrib.auth.urls')),

]
