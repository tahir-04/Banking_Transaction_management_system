CREATE VIEW banking.account_summary AS
SELECT
    account_number,
    balance,
    status,
    account_type
FROM banking.accounts;