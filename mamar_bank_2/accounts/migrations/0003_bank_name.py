# Generated by Django 5.0.2 on 2024-03-31 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_bank'),
    ]

    operations = [
        migrations.AddField(
            model_name='bank',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
