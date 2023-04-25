# Generated by Django 4.2 on 2023-04-21 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_no', models.IntegerField()),
                ('name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254)),
                ('department', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('joined_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
