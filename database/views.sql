CREATE VIEW banking.customer_accounts AS
SELECT
    c.customer_id,
    c.first_name,
    c.last_name,
    a.account_number,
    a.balance
FROM banking.customers c
JOIN banking.accounts a
ON c.customer_id = a.customer_id;

CREATE VIEW banking.account_summary AS
SELECT
    account_number,
    balance,
    status,
    account_type
FROM banking.accounts;

CREATE OR REPLACE FUNCTION
banking.get_balance(
    account_no VARCHAR
)
RETURNS DECIMAL AS
$$
DECLARE
    current_balance DECIMAL;
BEGIN

    SELECT balance
    INTO current_balance
    FROM banking.accounts
    WHERE account_number = account_no;

    RETURN current_balance;

END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION
banking.get_total_transactions(
    account UUID
)
RETURNS INTEGER AS
$$
DECLARE
    total INTEGER;
BEGIN

    SELECT COUNT(*)
    INTO total
    FROM banking.transactions
    WHERE sender_account = account
    OR receiver_account = account;

    RETURN total;

END;
$$ LANGUAGE plpgsql;

