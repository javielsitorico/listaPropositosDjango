# Generated by Django 4.1.5 on 2023-01-12 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proposito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proposito', models.CharField(max_length=255)),
                ('fechaObjetivo', models.DateField()),
                ('conseguido', models.BooleanField(null=True)),
                ('fechaConseguido', models.DateField(null=True)),
            ],
        ),
    ]
