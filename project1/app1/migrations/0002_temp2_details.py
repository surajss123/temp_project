# Generated by Django 5.0.2 on 2024-04-03 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='temp2_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Number', models.IntegerField(max_length=10)),
                ('How_Much', models.IntegerField(max_length=20)),
                ('You_Order', models.CharField(max_length=20)),
                ('Address', models.CharField(max_length=50)),
            ],
        ),
    ]
