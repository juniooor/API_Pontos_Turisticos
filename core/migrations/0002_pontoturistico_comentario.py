# Generated by Django 4.2 on 2023-04-24 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0001_initial'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoturistico',
            name='Comentario',
            field=models.ManyToManyField(to='comentarios.comentario'),
        ),
    ]
