# Generated by Django 4.1.7 on 2023-06-17 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FlResults',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('logs', models.TextField(blank=True, null=True)),
                ('min_client', models.IntegerField(default=2)),
                ('num_round', models.IntegerField(default=2)),
            ],
            options={
                'db_table': 'FlResults',
            },
        ),
    ]
