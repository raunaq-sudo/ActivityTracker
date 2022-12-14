# Generated by Django 4.0.2 on 2022-08-08 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity_dashboard', '0014_unittest_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='unittest',
            name='image',
        ),
        migrations.AddField(
            model_name='unittest',
            name='error_attachment',
            field=models.FileField(blank=True, upload_to='uploads/errors/', verbose_name='Error Attachments'),
        ),
        migrations.AddField(
            model_name='unittest',
            name='error_description',
            field=models.TextField(null=True, verbose_name='Error Description'),
        ),
        migrations.AddField(
            model_name='unittest',
            name='output_description',
            field=models.TextField(null=True, verbose_name='Output'),
        ),
        migrations.AlterField(
            model_name='unittest',
            name='attachment',
            field=models.FileField(blank=True, upload_to='uploads/', verbose_name='Output Attachments'),
        ),
    ]
