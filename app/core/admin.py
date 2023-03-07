from django.contrib import admin
from .models import TypeOfUser, Place, TypeOfStatus, Status, StatusChangeLog, Incidence, Franchise, Store
# Register your models here.

admin.site.register(TypeOfUser)
admin.site.register(Place)
admin.site.register(TypeOfStatus)
admin.site.register(Status)
admin.site.register(StatusChangeLog)
admin.site.register(Incidence)
admin.site.register(Franchise)
admin.site.register(Store)