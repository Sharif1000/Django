# Generated by Django 5.0.2 on 2024-02-21 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('roll', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('father_name', models.TextField(max_length=30)),
                ('address', models.TextField()),
            ],
        ),
    ]