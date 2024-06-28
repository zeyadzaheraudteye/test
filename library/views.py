from django.views.generic import ListView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .models import Book
from .forms import BookForm


class BookListView(ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'library/index.html'
    context_object_name = 'books'

class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'library/create.html'
    success_url = reverse_lazy('book-list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UserRegistrationView(CreateView):
    form_class = UserCreationForm
    template_name = 'library/register.html'
    success_url = reverse_lazy('book-list')
