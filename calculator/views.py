from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def calculate_price(request):
    data = request.data
    total_cost = float(data['total_cost'])
    profit_amount = float(data['profit'])
    tax = float(data['tax'])
    discount = float(data['discount'])

    selling_price = total_cost + profit_amount
    net_price = selling_price - (selling_price * discount / 100)
    final_price = net_price + (net_price * tax / 100)

    return Response({
        "selling_price": round(selling_price, 2),
        "net_price": round(net_price, 2),
        "final_price": round(final_price, 2),
    })
