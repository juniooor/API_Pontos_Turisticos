# Generated by Django 4.2 on 2023-05-24 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atracoes', '0002_atracao_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atracao',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='atracoes'),
        ),
    ]
