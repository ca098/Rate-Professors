# Generated by Django 3.0.3 on 2020-03-12 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rate_professors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='code',
            field=models.CharField(max_length=3, unique=True),
        ),
    ]
