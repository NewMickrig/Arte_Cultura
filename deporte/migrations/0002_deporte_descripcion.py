# Generated by Django 3.2.4 on 2021-07-13 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deporte', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='deporte',
            name='descripcion',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]
