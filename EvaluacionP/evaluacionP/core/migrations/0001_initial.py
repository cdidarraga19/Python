# Generated by Django 4.1.3 on 2022-11-04 18:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GamePosition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('description', models.TextField(verbose_name='Descripción')),
            ],
            options={
                'verbose_name': 'Posición',
                'verbose_name_plural': 'Posiciones',
                'db_table': 'posicion',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Nacionality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('description', models.TextField(verbose_name='Descripción')),
            ],
            options={
                'verbose_name': 'Nacionalidad',
                'verbose_name_plural': 'Nacionalidades',
                'db_table': 'nacionalidad',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('flag', models.ImageField(upload_to='', verbose_name='Bandera del equipo')),
                ('team_crest', models.ImageField(upload_to='', verbose_name='Escudo del equipo')),
            ],
            options={
                'verbose_name': 'Equipo',
                'verbose_name_plural': 'Equipos',
                'db_table': 'equipo',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='TechincalDirector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('lastname', models.CharField(max_length=50, verbose_name='Apellido')),
                ('date_of_birth', models.DateField(verbose_name='Fecha de nacimiento')),
                ('role', models.CharField(choices=[('1', 'Técnico'), ('2', 'Asistente'), ('3', 'Médico'), ('4', 'Preparador')], max_length=50)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.nacionality', verbose_name='Equipo')),
            ],
            options={
                'verbose_name': 'Técnico',
                'verbose_name_plural': 'Técnicos',
                'db_table': 'tecnico',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('lastname', models.CharField(max_length=50, verbose_name='Apellido')),
                ('photo', models.ImageField(upload_to='', verbose_name='Foto del jugador')),
                ('date_of_birth', models.DateField(verbose_name='Fecha de nacimiento')),
                ('shirt_number', models.PositiveIntegerField(verbose_name='Número')),
                ('headline', models.BooleanField(choices=[(True, 'Si'), (False, 'No')], verbose_name='Es titular?')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.gameposition', verbose_name='Posición de juego')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.team', verbose_name='Equipo')),
            ],
            options={
                'verbose_name': 'Jugador',
                'verbose_name_plural': 'Jugadores',
                'db_table': 'jugador',
                'ordering': ['id'],
            },
        ),
    ]
