from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinValueValidator(1),MaxValueValidator(5)])
    author = models.CharField(null = True, max_length=100)
    is_bestselling = models.BooleanField(default=False)
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

    