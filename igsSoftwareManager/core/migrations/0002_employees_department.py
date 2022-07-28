# Generated by Django 4.0.6 on 2022-07-28 11:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employees',
            name='department',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.departments'),
            preserve_default=False,
        ),
    ]
