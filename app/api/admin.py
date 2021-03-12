from django.contrib import admin
from api import models

admin.site.site_header = 'api.openspacedata.org'

admin.site.register(models.UserProfile)

class IndiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'accr', 'satellite_to_use')
    list_filter = ('satellite_to_use', )
    search_fields = ('name', 'accr', 'decription')
admin.site.register(models.Indice, IndiceAdmin)

class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'indice_to_use')
    search_fields = ('name', 'indice_to_use', 'decription')
admin.site.register(models.Application, ApplicationAdmin)

class BandsInline(admin.StackedInline):
    model = models.Band
    show_change_link = True

class SatelliteAdmin(admin.ModelAdmin):
    list_display = ('name', 'accr', 'operator')
    inlines = [BandsInline]

admin.site.register(models.Satellite, SatelliteAdmin)

class BandAdmin(admin.ModelAdmin):
    list_display = ('in_satellite', 'band', 'description', 'wavelength', 'resolution',)
    list_filter = ('in_satellite', )
    search_fields = ('description', 'wavelength', 'resolution',)
admin.site.register(models.Band, BandAdmin)