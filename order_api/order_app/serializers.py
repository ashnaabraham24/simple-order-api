from rest_framework import serializers
from .models import Order

# Converts'Order' model instances to JSON and validates input data
class OrderSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source="user.name", read_only=True)
    product_name = serializers.CharField(source="product.name", read_only=True)
    class Meta:
        model = Order
        # Include all fields from the Order model
        fields = "__all__" 

    # Basic validation for quantity field    
    def validate_quantity(self, value):
        if value <= 0:
            raise serializers.ValidationError("Quantity must be greater than 0")
        return value