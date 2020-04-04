# Generated by Django 2.2.5 on 2019-09-25 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0004_auto_20190925_2211'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='carousel')),
                ('status', models.CharField(choices=[('draft', 'Taslak'), ('published', 'Yayinlandi'), ('deleted', 'Silindi')], default='', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
