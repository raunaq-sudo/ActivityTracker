# Generated by Django 4.0.2 on 2022-08-05 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity_dashboard', '0013_unittest_attachment'),
    ]

    operations = [
        migrations.AddField(
            model_name='unittest',
            name='image',
            field=models.ImageField(default='', upload_to='', verbose_name='Image'),
        ),
    ]