# Generated by Django 4.0.2 on 2022-08-03 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity_dashboard', '0004_alter_kds_created_on_alter_kds_updated_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kds',
            name='created_on',
            field=models.DateField(null=True, verbose_name='Created On'),
        ),
        migrations.AlterField(
            model_name='kds',
            name='updated_on',
            field=models.DateField(null=True, verbose_name='Updated On'),
        ),
    ]
