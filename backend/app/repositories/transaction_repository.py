from backend.app.models.transaction import Transaction


class TransactionRepository:

    @staticmethod
    def create(
        db,
        transaction
    ):
        db.add(transaction)