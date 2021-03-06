# Generated by Django 3.0.8 on 2020-07-26 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0004_auto_20200726_1148'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=150)),
                ('presente_par', models.CharField(max_length=150)),
                ('domaine', models.CharField(max_length=50)),
                ('adresse', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='interimaire',
            name='ref',
        ),
        migrations.AddField(
            model_name='candidat',
            name='type',
            field=models.CharField(choices=[('etudiant', 'Etudiant'), ('sortant', 'Sortant universitaire'), ('stagiaire', 'En stage'), ('technicien', 'Technicien'), ('employe', 'Trvail actuellement')], default='etudiant', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='candidat',
            name='date_creation',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='interimaire',
            name='date_creation',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='intervention',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.CreateModel(
            name='MiseADisposition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_de_debut', models.DateField()),
                ('date_de_fin', models.DateField()),
                ('debut_souplesse', models.DateField()),
                ('fin_souplesse', models.DateField()),
                ('montant_par_jour', models.FloatField()),
                ('candidat', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gestion.Candidat')),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gestion.Client')),
            ],
        ),
    ]
