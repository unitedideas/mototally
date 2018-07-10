# Generated by Django 2.0.6 on 2018-07-09 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gomoto', '0010_auto_20180709_1731'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bike',
            old_name='dry_weight',
            new_name='weight',
        ),
        migrations.RemoveField(
            model_name='bike',
            name='wet_weight',
        ),
        migrations.AlterField(
            model_name='bike',
            name='category',
            field=models.CharField(blank=True, choices=[('Off-Road', 'Off-Road'), ('Motocross', 'Motocross'), ('Adventure', 'Adventure'), ('Trials', 'Trials'), ('Mini', 'Mini')], default='Off-Road', max_length=300, null=True),
        ),
    ]