from django.contrib import admin
from .models.models import TrainStation, Train, TrainSection, Person, ICE, Railjets, Platform


class TrainStationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


class TrainAdmin(admin.ModelAdmin):
    list_display = ('id',)
    search_fields = ('id',)


class TrainSectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    search_fields = ('first_name',)


class ICEAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('id', 'name')


class RailjetsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('id', 'name')


class PlatformAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


admin.site.register(TrainStation, TrainStationAdmin)
admin.site.register(Train, TrainAdmin)
admin.site.register(TrainSection, TrainSectionAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(ICE, ICEAdmin)
admin.site.register(Railjets, RailjetsAdmin)
admin.site.register(Platform, PlatformAdmin)