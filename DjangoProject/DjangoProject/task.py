from celery import shared_task
from app.models import Transactions, Users
from django.core.exceptions import ObjectDoesNotExist


@shared_task
def process_transaction(user_id):
    try:
        user = Users.objects.get(user_id=user_id)
        transaction = Transactions.objects.filter(user_id=user_id).latest('timestamp')

        # Check if the user has enough balance
        if transaction.transaction_type == 'Buy' and user.balance < transaction.transaction_price * transaction.transaction_volume:
            transaction.status = 'insufficient_balance'
            transaction.save()
            return None

        if transaction.transaction_type == 'Buy':
            user.balance -= transaction.transaction_price * transaction.transaction_volume
        elif transaction.transaction_type == 'Sell':
            user.balance += transaction.transaction_price * transaction.transaction_volume

        user.save()

        transaction.status = 'processed'
        transaction.save()

        return "ok"
    except ObjectDoesNotExist:
        # where the transaction or user does not exist
        return None
    