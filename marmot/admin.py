from django.contrib import admin
from .models import User, Movies, Watched,Genres,Reviews,Service

# Register your models here.
admin.site.register(Movies)
admin.site.register(User)
admin.site.register(Watched)
admin.site.register(Genres)
admin.site.register(Reviews)
admin.site.register(Service)
