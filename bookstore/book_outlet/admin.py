from django.contrib import admin
from .models import Book, Author, Address, Country
# Register your models here.


class BookAdmin(admin.ModelAdmin):
# Dzięki tej klasie możesz dodać jakąś wartość z modelu,
#  żeby była wyświetlana w panelu administratora
# NIE DZIAŁA RAZEM Z PREPOPULATE_FIELDS
#   readonly_fields = ("slug",)
# dzięki temu mamy podgląd tej wartości w czasie rzeczywistym
#  (podczas usupełniania)
    prepopulated_fields = {"slug" : ("title",)}
# dadnie filtrowanie w panelu Admin
    list_filter = ("author","rating",)
# dadnie kolumn w panelu Admin
    list_display = ("title", "author",)



admin.site.register(Book,BookAdmin)
admin.site.register(Author)
admin.site.register(Address)
admin.site.register(Country)