# Generated by Django 3.1 on 2021-03-19 15:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_application_ma_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='application',
            old_name='ma_name',
            new_name='machine_name',
        ),
    ]