# Generated by Django 2.2.5 on 2019-11-28 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='gender',
            field=models.CharField(choices=[('man', 'Erkek'), ('woman', 'Kadın'), ('unisex', 'UniSex')], default='unisex', max_length=6),
        ),
    ]