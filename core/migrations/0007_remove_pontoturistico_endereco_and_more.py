# Generated by Django 4.2.1 on 2023-06-26 22:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('enderecos', '0001_initial'),
        ('core', '0006_pontoturistico_foto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pontoturistico',
            name='endereco',
        ),
        migrations.AddField(
            model_name='pontoturistico',
            name='endereco',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='enderecos.endereco'),
        ),
    ]
