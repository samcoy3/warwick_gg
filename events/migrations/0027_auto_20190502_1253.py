# Generated by Django 2.2 on 2019-05-02 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0026_auto_20190502_1242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='charge_id',
            field=models.TextField(blank=True),
        ),
    ]
