from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.intervs , name='interventions'),
    path('interv/<int:id_interv>', views.detail_interv, name='intervention'),
    path('interimaires/', views.interms , name='interimaires'),
    path('interm/<int:id_interm>', views.detail_interm, name='interimaire'),

    path('candidats/', views.candidats , name='candidats'),
    path('candidat/<int:id_candidat>', views.detail_candidat, name='candidat'),

    path('disposition/', views.disposition , name='disposition'),
    path('contrat/', views.contrat , name='generateContrat'),
]
