from django.db import models
from page.models import DEFAULT_STATUS, STATUS

GENDER_CHOICE = [
    ('man', 'Erkek'),
    ('woman', 'Kadın'),
    ('unisex', 'UniSex'),
]


class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(
        max_length=200,
        default="",
    )
    status = models.CharField(
        default=DEFAULT_STATUS,
        choices=STATUS,
        max_length=10,
    )
    gender = models.CharField(
        max_length=6,
        default="unisex",
        choices=GENDER_CHOICE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.pk + 1000} - {self.gender}-{self.title}"


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250, default="")
    content = models.TextField()
    cover_image = models.ImageField(upload_to='page', null=True, blank=True)
    price = models.FloatField()
    stock = models.PositiveSmallIntegerField(default=0)
    is_home = models.BooleanField(default=False)
    status = models.CharField(
        default=DEFAULT_STATUS,
        choices=STATUS,
        max_length=10,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
