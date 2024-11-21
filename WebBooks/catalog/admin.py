"""

from django.contrib import admin

# Register your models here.
from.models import Author, Book, Genre, Language, Status, BookInstance, Publisher
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Publisher)
admin.site.register(Status)
admin.site.register(BookInstance)
#admin.site.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'photo')
    fields = ['first_name', 'last_name',
            ('date_of_birth', 'date_of_death')]
# admin.site.register(Author, AuthorAdmin)

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance

#admin.site.register(Book)
# @admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'language', 'display_author')
    list_filter = ('genre', 'author')
    inlines = [BooksInstanceInline]

# admin.site.register(Genre)
# admin.site.register(Language)
# admin.site.register(Status)
#admin.site.register(BookInstance)
# @admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None, {
        'fields': ('book', 'imprint', 'inv_nom')
        }),
        ('Availability', {
        'fields': ('status', 'due_back', 'borrower')
        }),
    )   
    def my_queryset(self, request):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='2').order_by('due_back')

"""




from django.contrib import admin
from django.utils.html import format_html

from.models import Author, Book, Genre, Language, Publisher, Status, BookInstance
# Определяем класс AuthorAdmin для авторов книг
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'photo', 'show_photo')
    fields = ['last_name', 'first_name', ('date_of_birth', 'photo')]
    readonly_fields = ["show_photo"]
    
    def show_photo(self, obj):
        return format_html(f'<img src="{obj.photo.url}" style="max-height: 100px;">')
    show_photo.short_description = 'Фото'
# admin.site.register(Author)
# Регистрируем класс AuthorAdmin для авторов книг
admin.site.register(Author, AuthorAdmin)
# admin.site.register(Book)
# Регистрируем класс BookAdmin для книг

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'language', 'display_author', 'photo', 'show_photo')
    list_filter = ('genre', 'author')
    inlines = [BooksInstanceInline]
    readonly_fields = ["show_photo"]
    def show_photo(self, obj):
        return format_html(f'<img src="{obj.photo.url}" style="max-height: 100px;">')
    show_photo.short_description = 'Обложка'
# admin.site.register(BookInstance)
# Регистрируем класс BookInstanceAdmin для экземпляров книг
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('book', 'status')
    fieldsets = (
        ('Экземпляр книги', {
            'fields': ('book', 'inv_nom')}),
            ('Статус и окончание его действия', {
                'fields': ('status', 'due_back', 'borrower')}),
    )
admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Publisher)
admin.site.register(Status)