# Generated by Django 2.0.4 on 2018-05-11 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songbook', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='chords',
            field=models.TextField(blank=True),
        ),
    ]
