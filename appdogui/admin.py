from django.contrib import admin
from .models import Instruments, Musics, Bands

admin.site.register(Instruments)
admin.site.register(Musics)
admin.site.register(Bands)

# Register your models here.