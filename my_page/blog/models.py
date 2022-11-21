from django.db import models
from django.core.validators import MinLengthValidator
import datetime

# Create your models here.

class Tag(models.Model):
    caption = models.CharField(max_length=25)

    def __str__(self):
        return f"{self.caption}"

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} "


class Post(models.Model):
    title = models.CharField(max_length=100)
    image = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete = models.PROTECT, null = False)
    date = models.DateField( auto_now=False, auto_now_add=True)
    slug = models.SlugField(null=False,unique = True, db_index=True)
    excerpt = models.CharField(max_length=350)
    content = models.TextField(validators=[MinLengthValidator(10)])
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f"{self.date}, {self.author} - {self.title}"