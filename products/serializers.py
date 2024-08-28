from rest_framework import serializers
from .models import Product, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['type', 'slug', 'attributes', 'links']

    type = serializers.SerializerMethodField()
    attributes = serializers.SerializerMethodField()
    links = serializers.SerializerMethodField()

    def get_type(self, obj): 
        return "categories"

    def get_image(self, obj):
        if not obj.image:
            return None
        request = self.context.get('request')
        return request.build_absolute_uri(obj.image.url)
    
    def get_attributes(self, obj):
        return {
            "name": obj.name,
            "image": self.get_image(obj),
        }

    def get_links(self, obj):
        request = self.context.get('request')
        return {
            "self": request.build_absolute_uri(f"/api/p/products/?category={obj.slug}")
        } 

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['type', 'slug', 'attributes', 'links']

    type = serializers.SerializerMethodField()
    attributes = serializers.SerializerMethodField()
    links = serializers.SerializerMethodField()

    def get_type(self, obj):
        return "products"

    def get_image(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.image.url)

    def get_attributes(self, obj):
        return {
            "name": obj.name,
            "description": obj.description,
            "price": obj.price,
            "stock": obj.stock,
            "image": self.get_image(obj),
            "category": obj.category.name
        }

    def get_links(self, obj):
        request = self.context.get('request')
        return {
            "self": request.build_absolute_uri(f"/api/p/products/{obj.slug}/")
        }
