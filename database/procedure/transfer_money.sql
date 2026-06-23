CREATE OR REPLACE PROCEDURE transfer_money(
    sender_acc VARCHAR,
    receiver_acc VARCHAR,
    transfer_amount NUMERIC
)
LANGUAGE plpgsql
AS $$
DECLARE
    sender_id UUID;
    receiver_id UUID;
    sender_balance NUMERIC;
BEGIN

    IF transfer_amount <= 0 THEN
        RAISE EXCEPTION
        'Amount must be greater than zero';
    END IF;

    SELECT
        account_id,
        balance
    INTO
        sender_id,
        sender_balance
    FROM banking.accounts
    WHERE account_number = sender_acc
    FOR UPDATE;

    IF NOT FOUND THEN
        RAISE EXCEPTION
        'Sender account not found';
    END IF;

    SELECT
        account_id
    INTO receiver_id
    FROM banking.accounts
    WHERE account_number = receiver_acc
    FOR UPDATE;

    IF NOT FOUND THEN
        RAISE EXCEPTION
        'Receiver account not found';
    END IF;

    IF sender_balance < transfer_amount THEN
        RAISE EXCEPTION
        'Insufficient funds';
    END IF;

    UPDATE banking.accounts
    SET balance = balance - transfer_amount
    WHERE account_id = sender_id;

    UPDATE banking.accounts
    SET balance = balance + transfer_amount
    WHERE account_id = receiver_id;

    INSERT INTO banking.transactions
    (
        transaction_id,
        sender_account,
        receiver_account,
        amount,
        transaction_type,
        reference_number,
        status
    )
    VALUES
    (
        uuid_generate_v4(),
        sender_id,
        receiver_id,
        transfer_amount,
        'TRANSFER',
        'TXN-' || floor(random()*1000000000),
        'SUCCESS'
    );

END;
$$;