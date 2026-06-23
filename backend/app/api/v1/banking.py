from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import uuid

from backend.app.dependencies.auth import get_current_user
from backend.app.dependencies.database import get_db
from backend.app.schemas.banking import (
    DepositRequest,
    WithdrawRequest,
    TransferRequest,
    CreateAccountRequest
)
from backend.app.repositories.account_repository import AccountRepository
from backend.app.models.account import Account
from backend.app.models.transaction import Transaction
from backend.app.dependencies.auth import get_current_user

router = APIRouter(
    prefix="/banking",
    tags=["Banking"]
)

@router.post("/accounts")
def create_account(
    request: CreateAccountRequest,
    db: Session = Depends(get_db)
):

    

    account = Account(
        current_user=Depends(get_current_user),
        customer_id=get_current_user.customer_id,  
        account_number=f"ACC{uuid.uuid4().hex[:8]}",
        account_type=request.account_type,
        balance=500,
        status="ACTIVE"
    )

    db.add(account)
    db.commit()
    db.refresh(account)

    return {
        "message": "Account created",
        "account_number": account.account_number
    }

@router.post("/deposit")
def deposit_money(
    request: DepositRequest,
    db: Session = Depends(get_db)
):
    account = AccountRepository.get_account(
        db,
        request.account_number
    )

    if not account:
        raise HTTPException(
            status_code=404,
            detail="Account not found"
        )

    account.balance += request.amount

    transaction = Transaction(
        sender_account=None,
        receiver_account=account.account_id,
        amount=request.amount,
        transaction_type="DEPOSIT",
        reference_number=str(uuid.uuid4()),
        status="SUCCESS"
    )

    db.add(transaction)
    db.commit()

    return {
        "message": "Deposit successful"
    }

@router.post("/withdraw")
def withdraw_money(
    request: WithdrawRequest,
    db: Session = Depends(get_db)
):
    account = AccountRepository.get_account(
        db,
        request.account_number
    )

    if not account:
        raise HTTPException(
            status_code=404,
            detail="Account not found"
        )

    if account.balance < request.amount:
        raise HTTPException(
            status_code=400,
            detail="Insufficient funds"
        )

    account.balance -= request.amount

    transaction = Transaction(
        sender_account=account.account_id,
        receiver_account=None,
        amount=request.amount,
        transaction_type="WITHDRAW",
        reference_number=str(uuid.uuid4()),
        status="SUCCESS"
    )

    db.add(transaction)
    db.commit()

    return {
        "message": "Withdrawal successful"
    }

@router.post("/transfer")
def transfer_money(
    request: TransferRequest,
    db: Session = Depends(get_db)
):
    try:
        sender = (
            AccountRepository
            .get_account_for_update(
                db,
                request.sender_account
            )
        )

        receiver = (
            AccountRepository
            .get_account_for_update(
                db,
                request.receiver_account
            )
        )

        if not sender:
            raise HTTPException(
                status_code=404,
                detail="Sender account not found"
            )

        if not receiver:
            raise HTTPException(
                status_code=404,
                detail="Receiver account not found"
            )

        if sender.balance < request.amount:
            raise HTTPException(
                status_code=400,
                detail="Insufficient balance"
            )

        sender.balance -= request.amount
        receiver.balance += request.amount

        transaction = Transaction(
            sender_account=sender.account_id,
            receiver_account=receiver.account_id,
            amount=request.amount,
            transaction_type="TRANSFER",
            reference_number=str(uuid.uuid4()),
            status="SUCCESS"
        )

        db.add(transaction)
        db.commit()

        return {
            "message": "Transfer successful"
        }

    except Exception:
        db.rollback()
        raise

@router.get("/transactions")
def get_transactions(
    db: Session = Depends(get_db)
):
    transactions = (
        db.query(Transaction)
        .all()
    )


    return transactions

@router.get("/test")
def test():
    return {"message": "Banking Router Working"}

