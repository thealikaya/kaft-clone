from django.db import models

# Create your models here.

DEFAULT_STATUS = "draft"

STATUS = [
    # left side : DB
    # right side : human-readable name
    ('draft', 'Taslak'),
    ('published', 'Yayinlandi'),
    ('deleted', 'Silindi'),
]


class Page(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250, default="")
    content = models.TextField()
    cover_image = models.ImageField(upload_to='page', null=True, blank=True)
    status = models.CharField(
        default=DEFAULT_STATUS,
        choices=STATUS,
        max_length=10,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Carousel(models.Model):
    title = models.CharField(max_length=200)
    cover_image = models.ImageField(
        upload_to='carousel',
        blank=True,
        null=True
    )
    status = models.CharField(
        default=DEFAULT_STATUS,
        choices=STATUS,
        max_length=10
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
