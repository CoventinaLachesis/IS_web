# Generated by Django 4.1.2 on 2022-12-15 14:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('menu', '0002_table_use_by_alter_menu_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='Use_by',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
