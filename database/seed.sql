INSERT INTO banking.customers (
first_name,
last_name,
email,
phone,
password_hash
)
VALUES (
'Tahir',
'Mohamed',
'tahir@gmail.com',
'9876543210',
'hashed_password'
);

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

