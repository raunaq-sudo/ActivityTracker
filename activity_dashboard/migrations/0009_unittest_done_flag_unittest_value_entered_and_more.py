# Generated by Django 4.0.2 on 2022-08-05 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity_dashboard', '0008_alter_unittest_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='unittest',
            name='done_flag',
            field=models.BooleanField(default=False, verbose_name='Done'),
        ),
        migrations.AddField(
            model_name='unittest',
            name='value_entered',
            field=models.CharField(blank=True, max_length=100, verbose_name='Value'),
        ),
        migrations.AlterField(
            model_name='unittest',
            name='comments_ut',
            field=models.TextField(blank=True, verbose_name='Comments'),
        ),
        migrations.AlterField(
            model_name='unittest',
            name='screenshot',
            field=models.FileField(blank=True, upload_to='', verbose_name='Screenshot'),
        ),
    ]