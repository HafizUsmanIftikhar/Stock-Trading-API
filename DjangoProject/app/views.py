from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view,renderer_classes
from rest_framework.response import Response
from .models import Users, StockData, Transactions
from .serializers import UserSerializer, StockDataSerializer, TransactionSerializer
from DjangoProject.task import process_transaction
import redis
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from rest_framework.renderers import TemplateHTMLRenderer
from datetime import datetime



class CreateUserView(APIView):
    serializer_class=UserSerializer
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetUserView(APIView):
    serializer_class=UserSerializer
    def get(self, request, username):
        # Check if the user data is in the cache
        cached_user = cache.get(username)
        if cached_user:
            return Response(cached_user)

        # If not in cache, fetch the user from the database
        user = Users.objects.get(username=username)
        serializer = UserSerializer(user)
        serialized_user = serializer.data

        # Store the user data in the cache
        cache.set(username, serialized_user)

        return Response(serialized_user)


class IngestStockDataView(APIView):
    serializer_class=StockDataSerializer
    def post(self, request):
        serializer = StockDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@cache_page(60 * 5)
def get_all_stock_data(request):
    cached_stock_data = cache.get('stock_data')
    if cached_stock_data is not None:
        return Response(cached_stock_data)

    stock_data = StockData.objects.all()
    serializer = StockDataSerializer(stock_data, many=True)
    serialized_data = serializer.data
    cache.set('stock_data', serialized_data, 60 * 5)  # Cache the data for 5 minutes
    return Response(serialized_data)


@api_view(['GET'])
@cache_page(60 * 5)
def get_stock_data(request, ticker):
    cached_stock_data = cache.get(f'stock_data_{ticker}')
    if cached_stock_data is not None:
        return Response(cached_stock_data)

    stock_data = StockData.objects.filter(ticker=ticker)
    serializer = StockDataSerializer(stock_data, many=True)
    serialized_data = serializer.data

    cache.set(f'stock_data_{ticker}', serialized_data, 60 * 5)  # Cache the data for 5 minutes

    return Response(serialized_data)

class CreateTransactionView(APIView):
    serializer_class=TransactionSerializer
    def post(self,request):
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            # Perform transaction processing logic here
            userid = request.data.get('user_id')
            # Do Transections using celery
            # process_transaction.delay(userid)
            process_transaction.apply_async(args=[userid])
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class GetUserTransactionsView(APIView):
    serializer_class=TransactionSerializer
    def get(self, request, user_id):
        transactions = Transactions.objects.filter(user_id=user_id)
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data)



@api_view(['GET'])
def get_user_transactions_by_timestamp(request, user_id, start_timestamp, end_timestamp):
    
        # Parse the timestamp strings to datetime objects
    start_datetime = datetime.fromisoformat(start_timestamp[:-1])  # Remove the 'Z' character
    end_datetime = datetime.fromisoformat(end_timestamp[:-1])

    # Query transactions between two timestamps for a specific user
    transactions = Transactions.objects.filter(
        user_id=user_id,
        timestamp__range=(start_datetime, end_datetime)
    )

    # Serialize the transactions and return the response
    serializer = TransactionSerializer(transactions, many=True)
    return Response(serializer.data)

    # example
    # transactions/1/2024-01-22T00:00:00Z/2024-01-22T23:59:59Z/