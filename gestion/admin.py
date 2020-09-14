from django.contrib import admin
from .models import *


class IntermAdmin(admin.ModelAdmin):
    list_display = ('prenom', 'nom', 'mail', 'portable', 'date_naissance')
    list_display_links = ('prenom',)
    search_fields = ('prenom', 'portable', 'mail')


admin.site.register(Interimaire, IntermAdmin)
admin.site.register(Entreprise)


class CandidatAdmin(admin.ModelAdmin):
    list_display = ('prenom', 'nom', 'mail', 'telephone', 'date_naissance')
    list_display_links = ('prenom',)
    search_fields = ('telephone', 'prenom', 'mail')


admin.site.register(Candidat, CandidatAdmin)


class IntervAdmin(admin.ModelAdmin):
    list_display = ('nom_intervention',  'nom_client', 'tel_client', 'adresse_client', 'date', 'pourcentage_ssp')
    list_display_links = ('nom_intervention',)
    search_fields = ('nom_intervention', 'tel_client', 'interimaire')


admin.site.register(Intervention, IntervAdmin)


class DisposionAdmin(admin.ModelAdmin):
    list_display = ('id', 'candidat', 'entreprise', 'date_de_debut', 'date_de_fin', 'montant_client', 'salaire_emp')
    list_display_links = ('id',)
    search_fields = ('id', 'client', 'candidat')


admin.site.register(MiseADisposition, DisposionAdmin)
admin.site.register(Client)
