# Generated by Django 3.0.2 on 2020-01-28 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Trynkit', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='id',
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=50, primary_key=True, serialize=False, unique=True),
        ),
    ]
