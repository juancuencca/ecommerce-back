from .models import Category, Product
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify

@receiver(pre_save, sender=Category)
def create_category_slug(sender, instance, **kwargs):
    if not instance.slug:
        name_slug = slugify(instance.name)
        instance.slug = f"{name_slug}"

@receiver(pre_save, sender=Product)
def create_product_slug(sender, instance, **kwargs):
    if not instance.slug:
        name_slug = slugify(instance.name)
        instance.slug = f"{name_slug}"
