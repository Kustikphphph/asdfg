from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Author, BookInstance, Genre
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from catalog import views
from .forms import AuthorsForm
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from django.urls import reverse_lazy 
from .models import Book

# Create your views here.



# def index(request):
#     num_books = Book.objects.all().count()
#     num_instances = BookInstance.objects.all().count()
#     num_instances_available = BookInstance.objects.filter(status__exact=2).count()
#     num_authors = Author.objects.count()
#     num_visits = request.session.get('num_visits', 0)
#     request.session['num_visits'] = num_visits + 1

#     return render(request, 'index.html', context={
#                     'num_books': num_books,
#                     'num_instances': num_instances,
#                     'num_instances_available': num_instances_available,
#                     'num_authors': num_authors,
#                     'num_visits': num_visits},)
# class BookListView(generic.ListView):
#     model = Book
#     paginate_by = 3

# class BookDetailView(generic.DetailView):
#     model = Book

# class AuthorListView(generic.ListView):
#     model = Author
#     paginate_by = 4

# class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
#     """
#     Универсальный класс представления списка книг,
#     находящихся в заказе у текущего пользователя.
#     """
#     model = BookInstance
#     template_name = 'catalog/bookinstance_list_borrowed_user.html'
#     paginate_by = 10
#     def get_queryset(self):
#         return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='2').order_by('due_back')
    
# def authors_add(request):
#     author = Author.objects.all()
#     authorsform = AuthorsForm()
#     return render(request, "catalog/authors_add.html",
#     {"form": authorsform, "author": author})

# def create(request):
#     if request.method == "POST": 
#         author = Author() 
#         author.first_name = request.POST.get("first_name") 
#         author.last_name = request.POST.get("last_name") 
#         author.date_of_birth = request.POST.get("date_of_birth") 
#         author.date_of_death = request.POST.get("date_of_death") 
#         author.save() 
#         return HttpResponseRedirect("/authors_add/")

# def delete(request, id): 
#     try: 
#         author = Author.objects.get(id=id) 
#         author.delete() 
#         return HttpResponseRedirect("/authors_add/") 
#     except Author.DoesNotExist: 
#         return HttpResponseNotFound("<h2>Автор не найден</h2>")

# def edit1(request, id): 
#     author = Author.objects.get(id=id) 
#     if request.method == "POST": 
#         author.first_name = request.POST.get("first_name") 
#         author.last_name = request.POST.get("last_name") 
#         author.date_of_birth = request.POST.get("date_of_birth") 
#         author.date_of_death = request.POST.get("date_of_death") 
#         author.save() 
#         return HttpResponseRedirect("/authors_add/") 
#     else: 
#         return render(request, "edit1.html", {"author": author})

# class BookCreate(CreateView): 
#     model = Book 
#     fields = '__all__' 
#     success_url = reverse_lazy('books')

# class BookUpdate(UpdateView): 
#     model = Book 
#     fields = '__all__' 
#     success_url = reverse_lazy('books')

# class BookDelete(DeleteView): 
#     model = Book 
#     success_url = reverse_lazy('books')
def start1(request):
    return render(request, "start1.html")
def color_bg(request):
    return render(request,"color_bg.html")
def color_text(request):
    return render(request,'color_text.html')
def color_text_bg(request):
    return render(request, 'color_text_bg.html')
def space1(request):
    return render(request, 'space1.html')
def space2(request):
    return render(request, 'space2.html')
def space3(request):
    return render(request,'space3.html')
def alignment1(request):
    return render(request, 'alignment1.html')
def align2(request):
    return render(request, 'alignment2.html')
def border1(request):
    return render(request,'border1.html')
def border2(request):
    return render(request,'border2.html')
def border_color(request):
    return render(request,'border_color.html')
def border_radius(request):
    return render(request,'border_radius.html')
def border_radius1(request):
    return render(request,'border_radius1.html')
def start(request):
    return render(request, "start.html")
def start_1(request):
    return render(request, "start_1.html")
def table(request):
    return render(request,'table.html')
def table1(request):
    return render(request,'table1.html')