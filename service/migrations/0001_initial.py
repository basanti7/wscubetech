# Generated by Django 4.2.2 on 2023-07-27 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_icon', models.CharField(max_length=50)),
                ('service_title', models.CharField(max_length=50)),
                ('service_des', models.TextField()),
            ],
        ),
    ]
