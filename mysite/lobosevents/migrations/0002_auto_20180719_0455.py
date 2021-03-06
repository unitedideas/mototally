# Generated by Django 2.0.5 on 2018-07-19 04:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lobosevents', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.TimeField(blank=True, max_length=300, null=True)),
                ('event_date', models.TimeField(blank=True, null=True)),
                ('pro_time_est', models.TimeField(blank=True, null=True)),
                ('am_time_est', models.TimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SpecialTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('special_test_num', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='UserEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bike_year', models.IntegerField()),
                ('bike_make', models.CharField(max_length=300)),
                ('bike_model', models.CharField(max_length=300)),
                ('bike_displacement', models.IntegerField()),
                ('omra_number', models.IntegerField()),
                ('ama_number', models.IntegerField()),
                ('userprofile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lobosevents.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='UserSpecialTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField()),
                ('stop_time', models.TimeField()),
                ('specialtest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lobosevents.SpecialTest')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='specialtest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lobosevents.SpecialTest'),
        ),
        migrations.AddField(
            model_name='event',
            name='userevent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lobosevents.UserEvent'),
        ),
    ]
