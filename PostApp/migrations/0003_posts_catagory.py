# Generated by Django 3.1.1 on 2020-09-26 10:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PostApp', '0002_auto_20200926_1711'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='catagory',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='PostApp.catagory'),
            preserve_default=False,
        ),
    ]