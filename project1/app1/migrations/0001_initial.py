# Generated by Django 5.0.2 on 2024-04-02 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='temp_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('School', models.CharField(max_length=20)),
                ('Place', models.CharField(max_length=20)),
                ('Phone_Number', models.IntegerField(max_length=20)),
            ],
        ),
    ]
