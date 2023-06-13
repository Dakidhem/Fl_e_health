# Generated by Django 4.1.7 on 2023-05-03 13:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('patients', '0002_remove_patient_created_patient_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='patients', to=settings.AUTH_USER_MODEL),
        ),
    ]