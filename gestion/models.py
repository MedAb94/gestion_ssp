from django.db import models


class Interimaire(models.Model):
    prenom = models.CharField(max_length=50)
    nom = models.CharField(max_length=50)
    mail = models.CharField(max_length=50, null=True)
    portable = models.CharField(max_length=50)
    date_naissance = models.DateField()
    lieu_naissance = models.CharField(max_length=50)
    adresse = models.CharField(max_length=50)
    mobilite_geographique = models.CharField(max_length=50)
    date_creation = models.DateField(auto_now_add=True)
    ci = models.FileField(upload_to="ci/")
    autres_documents = models.FileField(upload_to="docs/")

    def __str__(self):
        return f"{self.prenom} {self.nom.upper()}"


class Intervention(models.Model):
    nom_intervention = models.CharField(max_length=50)
    nom_client = models.CharField(max_length=50)
    tel_client = models.CharField(max_length=50)
    interimaire = models.ForeignKey(Interimaire, on_delete=models.CASCADE)
    adresse_client = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True)
    distance = models.FloatField()
    cout = models.FloatField()

    @property
    def cout_depalacement(self):
        return self.distance * 15

    @property
    def pourcentage_ssp(self):
        return ((self.cout * 10) / 100) + self.cout_depalacement / 2

    @property
    def net_a_payer(self):
        return (self.cout - ((self.cout * 10) / 100)) + self.cout_depalacement / 2


TYPE_CHOICES = [
    ('etudiant', 'Etudiant'),
    ('sortant', 'Sortant universitaire'),
    ('stagiaire', 'En stage'),
    ('technicien', 'Technicien'),
    ('employe', 'Trvail actuellement'),
]


class Candidat(models.Model):
    prenom = models.CharField(max_length=50)
    nom = models.CharField(max_length=50)
    mail = models.CharField(max_length=50)
    telephone = models.CharField(max_length=50)
    date_naissance = models.DateField()
    lieu_naissance = models.CharField(max_length=50)
    adresse = models.CharField(max_length=50)
    type = models.CharField(choices=TYPE_CHOICES, max_length=50)
    situation_actuelle = models.CharField(max_length=50)
    specialite = models.CharField(max_length=50)
    experience = models.CharField(max_length=50)
    cv = models.FileField(upload_to="cvs/")
    lettre_de_motivation = models.FileField(upload_to="lm/")
    date_creation = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.prenom}/{self.nom}"


class Client(models.Model):
    prenom = models.CharField(max_length=150)
    nom = models.CharField(max_length=150)
    tel = models.CharField(max_length=50)
    adresse = models.CharField(max_length=50)

    def __str__(self):
        return self.nom


class Entreprise(models.Model):
    nom = models.CharField(max_length=150)
    slogan = models.CharField(max_length=150)
    domaine = models.CharField(max_length=250)
    nif = models.CharField(max_length=50)
    rc = models.CharField(max_length=50)
    adresse = models.CharField(max_length=250)
    representant = models.CharField(max_length=250)
    telephone = models.CharField(max_length=16)
    email = models.CharField(max_length=250)

    def __str__(self):
        return self.nom


class MiseADisposition(models.Model):
    entreprise = models.ForeignKey(Entreprise, on_delete=models.SET_NULL, null=True)
    candidat = models.ForeignKey(Candidat, on_delete=models.SET_NULL, null=True)
    motif = models.CharField(max_length=255, null=True)
    date_de_debut = models.DateField(null=True)
    date_de_fin = models.DateField(null=True)
    debut_souplesse = models.DateField(null=True)
    fin_souplesse = models.DateField(null=True)
    horaire_collectif = models.CharField(max_length=255, null=True)
    horaire = models.CharField(max_length=255, null=True)
    salaire_heur_normal = models.CharField(max_length=255, null=True)
    salaire_heur_compl = models.CharField(max_length=255, null=True)
    montant_par_jour = models.FloatField(max_length=255, null=True)
    prime_deplacement = models.CharField(max_length=255, null=True)
    autres_primes = models.CharField(max_length=255, null=True)
    carecteristique = models.CharField(max_length=255, null=True)
    risques = models.CharField(max_length=255, null=True)
    equipements = models.CharField(max_length=255, null=True)
    creation = models.DateField(auto_now_add=True)
    def __str__(self):
        return f"{self.candidat}-{self.entreprise}"

    @property
    def montant_total(self):
        jrs = self.date_de_fin - self.debut_souplesse
        return jrs * self.montant_par_jour

    @property
    def montant_client(self):
        return self.montant_total + ((self.montant_total * 5) / 100)

    @property
    def salaire_emp(self):
        return self.montant_total - ((self.montant_total * 10) / 100)

    @property
    def marge_ssp(self):
        return self.montant_client - (self.salaire_emp)
