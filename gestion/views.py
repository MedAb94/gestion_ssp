from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import *


@login_required()
def intervs(request):
    context = {
        'inter': Intervention.objects.all()
    }
    return render(request, 'pages/intervs.html', context)


@login_required()
def detail_interv(request, id_interv):
    context = {
        "interv": get_object_or_404(Intervention, pk=id_interv),
    }
    return render(request, 'pages/detail_interv.html', context)


@login_required()
def interms(request):
    context = {
        "interms": Interimaire.objects.all()
    }
    return render(request, 'pages/interm.html', context)


@login_required()
def detail_interm(request, id_interm):
    context = {
        "interm": get_object_or_404(Interimaire, pk=id_interm),
        "intervs": Intervention.objects.filter(interimaire__id=id_interm)
    }
    return render(request, 'pages/detail_interm.html', context)


@login_required()
def candidats(request):
    context = {
        "candidats": Candidat.objects.all()
    }
    return render(request, 'pages/candidat.html', context)


@login_required()
def detail_candidat(request, id_candidat):
    context = {
        "candidat": get_object_or_404(Candidat, pk=id_candidat),
        "contrats": MiseADisposition.objects.filter(candidat__id=id_candidat)
    }
    return render(request, 'pages/detail_candidat.html', context)


@login_required()
def disposition(request):
    context = {
        "candidats": Candidat.objects.all(),
        "employeurs": Entreprise.objects.all()
    }
    return render(request, 'pages/disposition.html', context)


@login_required()
def contrat(request):
    if request.method == 'POST':
        entreprise = Entreprise.objects.get(request.POST.get('entreprise'))
        candidat = Candidat.objects.get(request.POST.get('candidat'))
        contrat = MiseADisposition.objects.create(
            entreprise=entreprise,
            candidat=candidat,
            motif=request.POST.get('motif'),
            date_de_debut=request.POST.get('date_de_debut'),
            date_de_fin=request.POST.get('date_de_fin'),
            debut_souplesse=request.POST.get('debut_souplesse'),
            fin_souplesse=request.POST.get('fin_souplesse'),
            horaire_collectif=request.POST.get('horaire_collectif'),
            horaire=request.POST.get('horaire'),
            salaire_heur_normal=request.POST.get('salaire_heur_normal'),
            salaire_heur_compl=request.POST.get('salaire_heur_compl'),
            montant_par_jour=request.POST.get('montant_par_jour'),
            prime_deplacement=request.POST.get('prime_deplacement'),
            autres_primes=request.POST.get('autres_primes'),
            carecteristique=request.POST.get('carecteristique'),
            risques=request.POST.get('risques'),
            equipements=request.POST.get('equipements'),
        )
        contrat.save()
        context = {
            'contrat': contrat,
        }
        return render(request, 'pages/contrat.html', context)
    return render(request, 'pages/disposition.html')
