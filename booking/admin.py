from django.contrib import admin

from . import models
from . models import book,Branch

# Register your models here.
#admin.site.register(book)
myModels = [models.book, models.Branch,]  # iterable list
admin.site.register(myModels)

