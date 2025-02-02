# Generated by Django 4.2.17 on 2024-12-07 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='bodyType',
            field=models.CharField(default='Sedan', max_length=100),
        ),
        migrations.AddField(
            model_name='car',
            name='color',
            field=models.CharField(default='White', max_length=100),
        ),
        migrations.AddField(
            model_name='car',
            name='condition',
            field=models.CharField(default='New', max_length=100),
        ),
        migrations.AddField(
            model_name='car',
            name='enginePower',
            field=models.CharField(default='100 HP', max_length=100),
        ),
        migrations.AddField(
            model_name='car',
            name='engineVolume',
            field=models.CharField(default='1.6 L', max_length=100),
        ),
        migrations.AddField(
            model_name='car',
            name='fuel',
            field=models.CharField(choices=[('Diesel', 'Diesel'), ('Petrol', 'Petrol'), ('Electric', 'Electric'), ('Hybrid', 'Hybrid')], default='Petrol', max_length=100),
        ),
        migrations.AddField(
            model_name='car',
            name='gear',
            field=models.CharField(default='Manual', max_length=100),
        ),
        migrations.AddField(
            model_name='car',
            name='heavyDamage',
            field=models.CharField(default='No', max_length=100),
        ),
        migrations.AddField(
            model_name='car',
            name='mileage',
            field=models.CharField(default='0 km', max_length=100),
        ),
        migrations.AddField(
            model_name='car',
            name='plate',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AddField(
            model_name='car',
            name='seller',
            field=models.CharField(default='Owner', max_length=100),
        ),
        migrations.AddField(
            model_name='car',
            name='swap',
            field=models.CharField(default='No', max_length=100),
        ),
        migrations.AddField(
            model_name='car',
            name='traction',
            field=models.CharField(default='FWD', max_length=100),
        ),
        migrations.AddField(
            model_name='car',
            name='warranty',
            field=models.CharField(default='No Warranty', max_length=100),
        ),
    ]
