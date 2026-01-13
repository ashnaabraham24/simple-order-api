from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import OrderSerializer

# Accepts only POST requests
@api_view(["POST"])
def create_order(request):
    serializer = OrderSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

        # Success response with message
        return Response(
            {
                "message": "Order created successfully",
                "order": serializer.data
            },status=201
        )

    # If validation fails, return error messages
    return Response(serializer.errors, status=400)
