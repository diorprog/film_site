# Generated by Django 4.2.5 on 2023-10-06 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='Premier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='premier')),
            ],
        ),
        migrations.DeleteModel(
            name='Trending',
        ),
    ]