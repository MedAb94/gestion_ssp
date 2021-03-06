# Generated by Django 3.0.8 on 2020-08-09 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0006_auto_20200726_1409'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entreprise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=150)),
                ('slogan', models.CharField(max_length=150)),
                ('domaine', models.CharField(max_length=250)),
                ('nif', models.CharField(max_length=50)),
                ('rc', models.CharField(max_length=50)),
                ('adresse', models.CharField(max_length=250)),
                ('representant', models.CharField(max_length=250)),
                ('telephone', models.CharField(max_length=16)),
                ('email', models.CharField(max_length=250)),
            ],
        ),
        migrations.RenameField(
            model_name='client',
            old_name='presente_par',
            new_name='prenom',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='domaine',
            new_name='tel',
        ),
        migrations.AlterField(
            model_name='candidat',
            name='cv',
            field=models.FileField(upload_to='cvs/'),
        ),
        migrations.AlterField(
            model_name='candidat',
            name='lettre_de_motivation',
            field=models.FileField(upload_to='lm/'),
        ),
        migrations.AlterField(
            model_name='interimaire',
            name='autres_documents',
            field=models.FileField(upload_to='docs/'),
        ),
        migrations.AlterField(
            model_name='interimaire',
            name='ci',
            field=models.FileField(upload_to='ci/'),
        ),
    ]
