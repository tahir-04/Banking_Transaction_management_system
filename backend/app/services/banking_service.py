import uuid

from sqlalchemy import text
from sqlalchemy.orm import Session

from backend.app.models.transaction import Transaction
from backend.app.models.notification import Notification
from backend.app.models.audit_log import AuditLog
from backend.app.models.account import Account

def deposit(
    db: Session,
    account_number: str,
    amount: float
):
    account = (
        db.query(Account)
        .filter(
            Account.account_number == account_number
        )
        .first()
    )

    if not account:
        raise Exception(
            "Account not found"
        )

    account.balance += amount

    transaction = Transaction(
        transaction_id=uuid.uuid4(),
        sender_account=None,
        receiver_account=account.account_id,
        amount=amount,
        transaction_type="DEPOSIT",
        reference_number=str(uuid.uuid4()),
        status="SUCCESS"
    )

    db.add(transaction)

    audit = AuditLog(
        customer_id=account.customer_id,
        action="DEPOSIT_SUCCESS",
        metadata={
            "account_number": account_number,
            "amount": amount
        }
    )

    db.add(audit)

    notification = Notification(
        customer_id=account.customer_id,
        message=f"₹{amount} deposited successfully.",
        status="SENT"
    )

    db.add(notification)

    db.commit()

    return transaction

def withdraw(
    db: Session,
    account_number: str,
    amount: float
):
    account = (
        db.query(Account)
        .filter(
            Account.account_number == account_number
        )
        .first()
    )

    if not account:
        raise Exception(
            "Account not found"
        )

    if account.balance < amount:
        raise Exception(
            "Insufficient funds"
        )

    account.balance -= amount

    transaction = Transaction(
        transaction_id=uuid.uuid4(),
        sender_account=account.account_id,
        receiver_account=None,
        amount=amount,
        transaction_type="WITHDRAW",
        reference_number=str(uuid.uuid4()),
        status="SUCCESS"
    )

    db.add(transaction)

    audit = AuditLog(
        customer_id=account.customer_id,
        action="WITHDRAW_SUCCESS",
        metadata={
            "account_number": account_number,
            "amount": amount
        }
    )

    db.add(audit)

    notification = Notification(
        customer_id=account.customer_id,
        message=f"₹{amount} withdrawn successfully.",
        status="SENT"
    )

    db.add(notification)

    db.commit()

    return transaction


def transfer(
    db: Session,
    sender_account: str,
    receiver_account: str,
    amount: float
):
    try:
        db.execute(
            text(
                """
                CALL transfer_money(
                    :sender,
                    :receiver,
                    :amount
                )
                """
            ),
            {
                "sender": sender_account,
                "receiver": receiver_account,
                "amount": amount
            }
        )

        sender = (
            db.query(Account)
            .filter(
                Account.account_number == sender_account
            )
            .first()
        )

        receiver = (
            db.query(Account)
            .filter(
                Account.account_number == receiver_account
            )
            .first()
        )

        audit = AuditLog(
            customer_id=sender.customer_id,
            action="TRANSFER_SUCCESS",
            details={
                "sender": sender_account,
                "receiver": receiver_account,
                "amount": amount
            }
        )

        db.add(audit)

        notification = Notification(
            customer_id=sender.customer_id,
            message=f"₹{amount} transferred successfully.",
            status="SENT"
        )

        db.add(notification)

        db.commit()

        return {
            "message": "Transfer successful"
        }

    except Exception as e:
        db.rollback()
        raise e