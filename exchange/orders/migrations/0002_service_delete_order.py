# Generated by Django 4.1.5 on 2023-01-16 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField(blank=True)),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
                ('customer_id', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]
