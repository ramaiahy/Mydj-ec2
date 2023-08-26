# Generated by Django 3.2 on 2023-08-26 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eno', models.IntegerField()),
                ('ename', models.CharField(max_length=50)),
                ('esal', models.FloatField()),
                ('eaddr', models.CharField(max_length=100)),
            ],
        ),
    ]
