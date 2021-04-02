# Generated by Django 3.1.7 on 2021-04-01 17:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0016_auto_20210324_2041'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('desc', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Destination',
        ),
        migrations.AlterField(
            model_name='flights',
            name='departure_date',
            field=models.DateField(default=datetime.date(2021, 4, 1)),
        ),
    ]
