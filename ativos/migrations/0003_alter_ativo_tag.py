# Generated by Django 5.0 on 2024-10-23 13:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ativos', '0002_tag_ativo_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ativo',
            name='tag',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ativos.tag'),
        ),
    ]
