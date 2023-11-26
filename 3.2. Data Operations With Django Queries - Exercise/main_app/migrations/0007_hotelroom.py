# Generated by Django 4.2.4 on 2023-10-27 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_rename_is_completed_task_is_finished'),
    ]

    operations = [
        migrations.CreateModel(
            name='HotelRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.PositiveIntegerField()),
                ('room_type', models.CharField(choices=[('St', 'Standard'), ('De', 'Deluxe'), ('Su', 'Suite')], max_length=20)),
                ('capacity', models.PositiveIntegerField()),
                ('amenities', models.TextField()),
                ('price_per_night', models.DecimalField(decimal_places=2, max_digits=8)),
                ('is_reserved', models.BooleanField(default=False)),
            ],
        ),
    ]
