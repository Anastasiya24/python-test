# Generated by Django 3.0.8 on 2020-07-12 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('seller', models.CharField(max_length=100)),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
