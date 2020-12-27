# Generated by Django 3.0.11 on 2020-12-25 03:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0003_auto_20201224_1208'),
        ('conf', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appsettings',
            name='global_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='settings_global_codes', to='map.Region', verbose_name='Регион портала'),
        ),
    ]