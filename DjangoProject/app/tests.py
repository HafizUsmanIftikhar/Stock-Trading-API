from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Users, StockData, Transactions
from .serializers import UserSerializer, StockDataSerializer, TransactionSerializer
from django.contrib.auth.models import User
from django.utils import timezone


class APIUnitTests(APITestCase):
    def setUp(self):
        # Create test data for Users, StockData, and Transactions
        self.user = Users.objects.create(username="tes", balance=1000.0)
        self.stock_data = StockData.objects.create(ticker='VIVO', open_price=150.0, close_price=160.0, high=170.0, low=140.0, volume=10000, timestamp=timezone.now())
        self.transaction = Transactions.objects.create(user=self.user, ticker='VIVO', transaction_type='buy', transaction_volume=10, transaction_price=155.0, timestamp=timezone.now())


    def test_create_user(self):
        url = reverse('create_user')
        data ={
            "username": "test1",
            "balance": 2000
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Users.objects.count(), 2)  # Update the count to reflect the new user
        self.assertEqual(Users.objects.get(username="test1").balance, 2000)

    def test_get_user(self):
        existing_user = Users.objects.create(username='test1', balance=2000.00)
        url = reverse('get_user', args=[existing_user.username])
        response = self.client.get(url)

        expected_data = {
            "user_id": existing_user.user_id,
            "username": "test1",
            "balance": "2000.00",
        }

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_data)
        
    def test_ingest_stock_data(self):
        url = reverse('ingest_stock_data')
        data = {
            'ticker': 'GOOG',
            'open_price': "2500.0",
            'close_price': "2600.0",
            'high': "2700.0",
            'low': "2400.0",
            'volume': "20000",
            'timestamp': timezone.now()
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(StockData.objects.count(), 2)
        self.assertEqual(StockData.objects.get(ticker='GOOG').open_price, 2500.0)


    def test_get_all_stock_data(self):
        url = reverse('get_all_stock_data')
        response = self.client.get(url)
        print(response.content.decode())
        expected_data = [
            {
                'ticker': 'VIVO',
                'open_price': '150.0',
                'close_price': '160.0',
                'high': '170.0',
                'low': '140.0',
                'volume': 10000,
                'timestamp': '2024-01-01'
            },
            {
                'ticker': 'GOOG',
                'open_price': '2500.0',
                'close_price': '2600.0',
                'high': '2700.0',
                'low': '2400.0',
                'volume': 20000,
                'timestamp': '2024-01-03'
            }
        ]
 
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(response.data, expected_data)

    # def test_get_stock_data(self):
    #     url = reverse('get_stock_data', args=['VIVO'])
    #     response = self.client.get(url)

    #     expected_data = [
    #        {
    #         'ticker': 'VIVO',
    #         'open_price': '150.0',
    #         'close_price': '160.0',
    #         'high': '170.0',
    #         'low': '140.0',
    #         'volume': 10000,
    #         'timestamp': '2024-01-01'
    #     }
    #     ]

    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     # self.assertEqual(response.data, expected_data)

    # def test_create_transaction(self):
    #     url = reverse('create_transaction')
    #     data = {
    #         'user_id': self.user_id,
    #         'ticker': 'VIVO',
    #         'transaction_type': 'Buy',
    #         'transaction_volume': 5,
    #         'transaction_price': 165.0,
    #         'timestamp': '2024-01-01',
    #     }

    #     response = self.client.post(url, data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     self.assertEqual(Transactions.objects.count(), 2)
    #     self.assertEqual(Transactions.objects.get(transaction_type='Buy').transaction_volume, 5)

    # def test_get_user_transactions(self):
    #     url = reverse('get_user_transactions', args=[self.user_id])
    #     response = self.client.get(url)

    #     expected_data = [
    #         {
    #             'transaction_id': self.transaction_id,
    #             'user_id': self.user_id,
    #             'ticker': 'VIVO',
    #             'transaction_type': 'Buy',
    #             'transaction_volume': 10,
    #             'transaction_price': 155.0,
    #             'timestamp': '2024-01-01',
    #         }
    #     ]

    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     # self.assertEqual(response.data, expected_data)

    # def test_get_user_transactions_by_timestamp(self):
    #     url = reverse('get_user_transactions_by_timestamp', args=[self.user_id, '2024-01-01', '2024-01-03'])
    #     response = self.client.get(url)

    #     expected_data = [
    #         {
    #             'transaction_id': self.transaction.id,
    #             'user_id': self.user.id,
    #             'ticker': 'VIVO',
    #             'transaction_type': 'Buy',
    #             'transaction_volume': 10,
    #             'transaction_price': 155.0,
    #             'timestamp': '2024-01-01',
    #         }
    #     ]

    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(response.data, expected_data) 