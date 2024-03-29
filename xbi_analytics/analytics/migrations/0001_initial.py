# Generated by Django 3.0.1 on 2020-01-10 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GraphData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('month', models.CharField(max_length=12)),
                ('rate', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='GridData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(max_length=10)),
                ('number', models.CharField(max_length=10)),
                ('sending_city', models.CharField(max_length=30)),
                ('receiving_city', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='PieChartData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(max_length=10)),
                ('fraction', models.IntegerField()),
            ],
        ),
    ]
