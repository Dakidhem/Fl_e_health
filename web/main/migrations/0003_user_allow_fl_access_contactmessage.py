# Generated by Django 4.1.7 on 2023-06-13 14:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_user_user_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='allow_fl_access',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
                ('fullname', models.CharField(max_length=50)),
                ('text', models.TextField(blank=True, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contact_message', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'ContactMessages',
            },
        ),
    ]
