# Generated by Django 3.0.5 on 2020-04-14 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('svip', '0016_auto_20200414_1611'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='cover',
            field=models.URLField(blank=True),
        ),
    ]
