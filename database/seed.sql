INSERT INTO banking.accounts (
customer_id,
account_number,
account_type,
balance
)
SELECT
customer_id,
'100000001',
'SAVINGS',
10000
FROM banking.customers
WHERE email='tahir@gmail.com';