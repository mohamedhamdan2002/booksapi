from dataclasses import field
from rest_framework import serializers
from .models import Books,Category


class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model=Books
        fields=(
            "id",
            "title",
            "author",
            "number_of_pages",
            "price",
            "active",
            "status",
            "publish_date",
            "quantity",
            "category",
            
        ) 
        
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=(
            "id",
            "name",
        )