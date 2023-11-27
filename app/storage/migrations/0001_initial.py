# Generated by Django 4.2.6 on 2023-11-07 11:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField()),
            ],
        ),
        migrations.CreateModel(
            name='Routeur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
                ('quantite_in', models.IntegerField(null=True)),
                ('quantite_out', models.IntegerField(null=True)),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('number', models.AutoField(primary_key=True, serialize=False)),
                ('serie', models.CharField(unique=True)),
                ('description_equipment', models.CharField()),
                ('quantite', models.IntegerField(default=1)),
                ('date_de_livraison', models.DateTimeField(auto_now_add=True)),
                ('projet', models.CharField()),
                ('nom_du_fournisseur', models.CharField()),
                ('cout', models.IntegerField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('show', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='storage.equipment')),
            ],
        ),
    ]
