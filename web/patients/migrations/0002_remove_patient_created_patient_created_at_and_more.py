# Generated by Django 4.1.7 on 2023-04-26 14:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='created',
        ),
        migrations.AddField(
            model_name='patient',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='patients', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='patient',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='patients'),
        ),
    ]
