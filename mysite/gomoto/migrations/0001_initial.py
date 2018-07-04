# Generated by Django 2.0.5 on 2018-07-04 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bikes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('make', models.CharField(max_length=300)),
                ('model', models.CharField(max_length=300)),
                ('weight', models.FloatField()),
                ('displacement', models.IntegerField()),
                ('seatheight', models.FloatField()),
                ('price', models.FloatField()),
                ('horsepower', models.FloatField()),
                ('category', models.CharField(choices=[('Off-road', 'Off-road'), ('Motocross', 'Motocross'), ('Adventure', 'Adventure'), ('Trials', 'Trials'), ('Mini', 'Mini')], default='Off-road', max_length=300)),
                ('engine_type', models.CharField(choices=[('Four-stroke', 'Four-stroke'), ('Two-stroke', 'Two-stroke'), ('Electric', 'Electric')], default='Four-stroke', max_length=300)),
            ],
        ),
    ]