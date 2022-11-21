from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=80)
    code = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.name} - {self.code} "

    class Meta:
        verbose_name_plural = "Counties"

class Address(models.Model):
    street = models.CharField(max_length=80)
    postal_code = models.CharField(max_length=5)
    city = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.city} - {self.street} "

    class Meta:
        verbose_name_plural = "Address Entries"

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null = True) # OnetoOne - przy relecjach jeden do jednego

    # Ta funkcja determinuje jak klasa będzie wyświetlana jako string (np. w panelu administratora)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinValueValidator(1),MaxValueValidator(5)])
        #reprezentuje inny model (ForeignKey) CASCADE - usunięcie np. Authora usówa też książkę któą napisał
        #inna opcja to PROTECT, która nie usówa książki mimo ze autor został usunięty. SET_NULL - zostawia pustę po usunieeciu authora
    author = models.ForeignKey(Author, on_delete = models.CASCADE, null = True) # ForeignKey - przy relecjach wiele do jednego
    is_bestselling = models.BooleanField(default=False)
    published_country = models.ManyToManyField(Country) # ManyToManyField - przy relecjach wiele do wielu
    slug = models.SlugField(default="", blank =True, null=False, db_index=True) # Harry Potter 1 => harry-potter-1
     #blank = True - dzięki temu nie musisz wpisywać niczego przy
     #  dodawaniu książki w panelu administratora w Django
     #  -slug doda się automatycznie ponieważ dodałeś self.slug = slugify(self.title)
    # Alternatywnie możesz wpisać editable = False - wtedy to pole nie pokaże się w 
    # cale podczas tworzenie pozycji w Django administration
    # nie działa z classą BookAdmin(admin.ModelAdmin): w pliku admin.py
    def get_absolute_url(self):
        return reverse("book-detail", args=[self.slug])
    
    # ta funkcja automatycznie zapisuje slug klasy Book jako tytuł
    """ def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args,**kwargs)
    """
    def __str__(self):
        return f"{self.title} ({self.rating})"

    