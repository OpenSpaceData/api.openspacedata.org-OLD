# Generated by Django 3.1 on 2021-03-18 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20210318_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='satellite',
            name='task',
            field=models.CharField(choices=[('SAR', 'SAR'), ('MSI', 'MSI')], max_length=256),
        ),
    ]