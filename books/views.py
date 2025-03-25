
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from .models import Book
from .forms import BookForm
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView
from .serializer import BookSerializer



class BookListView(View):
    template_name = 'books/book_list.html'

    def get(self, request):
        query = request.GET.get('q')
        if query:
            books = Book.objects.filter(title__icontains=query)
        else:
            books = Book.objects.all()
        return render(request, self.template_name, {'books': books})


class BookAPIListView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookAPICreateView(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookAPIDeleteView(DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookDetailView(View):
    template_name = 'books/book_detail.html'

    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        return render(request, self.template_name, {'book': book})

class BookCreateView(View):
    template_name = 'books/book_form.html'
    success_url = reverse_lazy('book_list')

    def get(self, request):
        form = BookForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(self.success_url)
        return render(request, self.template_name, {'form': form})

class BookUpdateView(View):
    template_name = 'books/book_form.html'
    success_url = reverse_lazy('book_list')

    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        form = BookForm(instance=book)
        return render(request, self.template_name, {'form': form})

    def post(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect(self.success_url)
        return render(request, self.template_name, {'form': form})

class BookDeleteView(View):
    template_name = 'books/book_confirm_delete.html'
    success_url = reverse_lazy('book_list')

    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        return render(request, self.template_name, {'book': book})

    def post(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        book.delete()
        return redirect(self.success_url)


