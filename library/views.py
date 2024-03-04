from django.shortcuts import render
from .models import Book

def library_view(request):
    data = Book.objects.all()
    contex = {"book": data}
    return render(request, "library/library_page.html", contex=contex)

# Create your views here.
