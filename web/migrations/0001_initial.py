# Generated by Django 3.0.8 on 2020-07-12 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Certification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('date_granted', models.DateField()),
                ('institution', models.CharField(max_length=64)),
                ('institution_url', models.URLField(max_length=254)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('university', models.CharField(max_length=64)),
                ('department', models.CharField(max_length=64)),
                ('department_url', models.URLField(max_length=254)),
                ('degree', models.CharField(max_length=64)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True)),
                ('link_header', models.CharField(max_length=64)),
                ('link_url', models.URLField(max_length=254)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('publication_date', models.DateField()),
                ('journal', models.CharField(max_length=64)),
                ('volume', models.IntegerField()),
                ('journal_code', models.CharField(max_length=32)),
                ('url', models.URLField(max_length=254)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=254)),
                ('institution', models.CharField(max_length=64)),
                ('position', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=64)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True)),
                ('institution', models.CharField(max_length=64)),
                ('institution_url', models.URLField(max_length=64)),
                ('description', models.TextField(blank=True)),
            ],
        ),
    ]
