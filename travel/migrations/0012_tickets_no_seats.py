# Generated by Django 3.1.7 on 2021-03-13 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0011_remove_tickets_no_seats'),
    ]

    operations = [
        migrations.AddField(
            model_name='tickets',
            name='no_seats',
            field=models.IntegerField(default=1),
        ),
    ]
