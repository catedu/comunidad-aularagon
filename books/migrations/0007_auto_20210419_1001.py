# Generated by Django 3.1.8 on 2021-04-19 08:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailmenus', '0023_remove_use_specific'),
        ('books', '0006_auto_20210416_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookindexpage',
            name='flat_menu',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailmenus.flatmenu'),
        ),
    ]
