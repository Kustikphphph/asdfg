from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Author, BookInstance, Genre
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from catalog import views
from .forms import AuthorsForm, Form_add_author 
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from django.urls import reverse_lazy 
from django.views.generic import ListView, DetailView
from django import forms
from django.urls import reverse

# Create your views here.


def index(request):
    text_head = 'На нашем сайте вы можете получить книги в электронном виде'
    # Данные о книгах и их количестве
    books = Book.objects.all()
    num_books = Book.objects.all().count()
    # Данные об экземплярах книг в БД
    num_instances = BookInstance.objects.all().count()
    # Доступные книги (статус = 'На складе')
    num_instances_available = BookInstance.objects.filter(
        status__exact=2).count()
    # Данные об авторах книг
    authors = Author.objects
    num_authors = Author.objects.count()

    # Количество посещений этого view, подсчитанное в переменной session 
    num_visits = request.session.get('num_visits', 0) 
    request.session['num_visits'] = num_visits + 1

    # Словарь для передачи данных в шаблон index.html
    context = {'text_head': text_head,
            'books': books, 'num_books': num_books,
            'num_instances': num_instances,
            'num_instances_available': num_instances_available,
            'authors': authors, 'num_authors': num_authors,
            'num_visits': num_visits
            }
    # передача словаря context с данными в шаблон
    return render(request, 'catalog/index.html', context)


def about(request):
    text_head = 'Сведения о компании'
    name = 'ООО "Интеллектуальные информационные системы"'
    rab1 = 'Разработка приложений на основе' \
    ' систем искусственного интеллекта'
    rab2 = 'Распознавание объектов дорожной инфраструктуры'
    rab3 = 'Создание графических АРТ-объектов на основе' \
    ' систем искусственного интеллекта'
    rab4 = 'Создание цифровых интерактивных книг, учебных пособий' \
    ' автоматизированных обучающих систем'
    context = {'text_head': text_head, 'name': name,
    'rab1': rab1, 'rab2': rab2,
    'rab3': rab3, 'rab4': rab4}
    # передача словаря context с данными в шаблон
    return render(request, 'catalog/about.html', context)
def contact(request):
    text_head = 'Контакты'
    name = 'ООО "Интеллектуальные информационные системы"'
    address = 'Москва, ул. Планерная, д.20, к.1'
    tel = '495-345-45-45'
    email = 'iis_info@mail.ru'
    # Словарь для передачи данных в шаблон index.html
    context = {'text_head': text_head,
    'name': name, 'address': address,
    'tel': tel,
    'email': email}
    # передача словаря context с данными в шаблон
    return render(request, 'catalog/contact.html', context)



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

class BookListView(ListView):
    model = Book
    context_object_name = 'books'
    paginate_by = 3


class BookDetailView(DetailView):
    model = Book
    context_object_name = 'book'

class AuthorListView(ListView):
    model = Author
    paginate_by = 4

class AuthorDetailView(DetailView):
    model = Author

class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
    """
    Универсальный класс представления списка книг,
    находящихся в заказе у текущего пользователя.
    """
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10
    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='2').order_by('due_back')
    
# def authors_add(request):
#     author = Author.objects.all()
#     authorsform = AuthorsForm()
#     return render(request, "catalog/authors_add.html",
#     {"form": authorsform, "author": author})

def create(request):
    if request.method == "POST": 
        author = Author() 
        author.first_name = request.POST.get("first_name") 
        author.last_name = request.POST.get("last_name") 
        author.date_of_birth = request.POST.get("date_of_birth") 
        author.date_of_death = request.POST.get("date_of_death") 
        author.save() 
        return HttpResponseRedirect("/authors_add/")

# def delete(request, id): 
#     try: 
#         author = Author.objects.get(id=id) 
#         author.delete() 
#         return HttpResponseRedirect("/authors_add/") 
#     except Author.DoesNotExist: 
#         return HttpResponseNotFound("<h2>Автор не найден</h2>")

def edit1(request, id): 
    author = Author.objects.get(id=id) 
    if request.method == "POST": 
        author.first_name = request.POST.get("first_name") 
        author.last_name = request.POST.get("last_name") 
        author.date_of_birth = request.POST.get("date_of_birth") 
        author.date_of_death = request.POST.get("date_of_death") 
        author.save() 
        return HttpResponseRedirect("/authors_add/") 
    else: 
        return render(request, "edit1.html", {"author": author})

# Класс для создания в БД новой записи о книге 
class BookCreate(CreateView): 
    model = Book 
    fields = '__all__' 
    success_url = reverse_lazy('edit_books') 
    
# Класс для обновления в БД записи о книге 
class BookUpdate(UpdateView): 
    model = Book 
    fields = '__all__' 
    success_url = reverse_lazy('edit_books') 

# Класс для удаления из БД записи о книге 
class BookDelete(DeleteView): 
    model = Book 
    success_url = reverse_lazy('edit_books')


class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView): 
    # Универсальный класс представления списка книг, 
    # находящихся в заказе у текущего пользователя 
    model = BookInstance 
    template_name = 'catalog/bookinstance_list_borroved_user.html' 
    paginate_by = 10 
    def get_queryset(self): 
        return BookInstance.objects.filter( 
            borrower=self.request.user).filter( 
            status__exact='2').order_by('due_back')

class Form_edit_author(forms.ModelForm): 
    class Meta: 
        model = Author 
        fields = '__all__'


def edit_author(request, id): 
    author = Author.objects.get(id=id) 
    # author = get_object_or_404(Author, pk=id) 
    if request.method == "POST": 
        instance = Author.objects.get(pk=id) 
        form = Form_edit_author(request.POST, request.FILES, instance=instance) 
        if form.is_valid(): 
            form.save() 
        return HttpResponseRedirect("/edit_authors/") 
    else: 
        form = Form_edit_author(instance=author) 
        content = {"form": form} 
        return render(request, "catalog/edit_author.html", content) 



# вызов страницы для редактирования авторов 
def edit_authors(request): 
    author = Author.objects.all() 
    context = {'author': author} 
    return render(request, "catalog/edit_authors.html", context)


# Создание нового автора в БД 
def authors_add(request): 
    if request.method == 'POST': 
        form = Form_add_author(request.POST, request.FILES) 
        if form.is_valid(): 
            # получить данные из формы 
            first_name = form.cleaned_data.get("first_name") 
            last_name = form.cleaned_data.get("last_name") 
            date_of_birth = form.cleaned_data.get("date_of_birth") 
            about = form.cleaned_data.get("about") 
            photo = form.cleaned_data.get("photo") 
            # создать объект для записи в БД 
            obj = Author.objects.create( 
            first_name=first_name, 
            last_name=last_name, 
            date_of_birth=date_of_birth, 
            about=about, 
            photo=photo) 
            # сохранить полученные данные 
            obj.save() 
            # загрузить страницу со списком автором 
            return HttpResponseRedirect(reverse('authors-list')) 
    else: 
        form = Form_add_author()  
        context = {"form": form} 
        return render(request, "catalog/authors_add.html", context)


# удаление авторов из БД 
def delete(request, id): 
    try: 
        author = Author.objects.get(id=id) 
        author.delete() 
        return HttpResponseRedirect("/edit_authors/") 
    except: 
        return HttpResponseNotFound("<h2>Автор не найден</h2>")


# вызов страницы для редактирования книг 
def edit_books(request): 
    book = Book.objects.all() 
    context = {'book': book} 
    return render(request, "catalog/edit_books.html", context)





# def start1(request):
#     return render(request, "start1.html")
# def color_bg(request):
#     return render(request,"color_bg.html")
# def color_text(request):
#     return render(request,'color_text.html')
# def color_text_bg(request):
#     return render(request, 'color_text_bg.html')
# def space1(request):
#     return render(request, 'space1.html')
# def space2(request):
#     return render(request, 'space2.html')
# def space3(request):
#     return render(request,'space3.html')
# def alignment1(request):
#     return render(request, 'alignment1.html')
# def align2(request):
#     return render(request, 'alignment2.html')
# def border1(request):
#     return render(request,'border1.html')
# def border2(request):
#     return render(request,'border2.html')
# def border_color(request):
#     return render(request,'border_color.html')
# def border_radius(request):
#     return render(request,'border_radius.html')
# def border_radius1(request):
#     return render(request,'border_radius1.html')
# def start(request):
#     return render(request, "start.html")
# def start_1(request):
#     return render(request, "start_1.html")
# def table(request):
#     return render(request,'table.html')
# def table1(request):
#     return render(request,'table1.html')
