# Generated by Django 4.2.11 on 2024-03-23 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_quote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='github_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
