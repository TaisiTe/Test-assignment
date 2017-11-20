from django.contrib import admin

from .models import Tellimus
from .models import Toode

admin.site.register(Toode)
admin.site.register(Tellimus)
