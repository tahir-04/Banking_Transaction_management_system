from backend.app.models.account import Account


class AccountRepository:

    @staticmethod
    def get_account(
        db,
        account_number
    ):
        return (
            db.query(Account)
            .filter(
                Account.account_number == account_number
            )
            .first()
        )

    @staticmethod
    def get_account_for_update(
        db,
        account_number
    ):
        return (
            db.query(Account)
            .filter(
                Account.account_number == account_number
            )
            .with_for_update()
            .first()
        )