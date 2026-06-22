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

