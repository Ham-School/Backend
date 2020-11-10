# Generated by Django 3.1.2 on 2020-11-09 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clase', models.CharField(max_length=50)),
                ('Grado', models.CharField(max_length=35)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apellidoP', models.CharField(max_length=35)),
                ('apellidoM', models.CharField(max_length=35)),
                ('nombre', models.CharField(max_length=35)),
                ('edad', models.PositiveIntegerField()),
                ('Tipo', models.CharField(choices=[('Maestro', 'Maestro'), ('Alumno', 'Alumno')], default='Alumno', max_length=7)),
                ('fecha', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestionAcademica.curso')),
                ('Usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestionAcademica.usuario')),
            ],
        ),
    ]
