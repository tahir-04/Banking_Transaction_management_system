CREATE INDEX idx_email
ON banking.customers(email);

CREATE INDEX idx_phone
ON banking.customers(phone);

CREATE INDEX idx_account_number
ON banking.accounts(account_number);

CREATE INDEX idx_customer_account
ON banking.accounts(customer_id);

CREATE INDEX idx_transaction_date
ON banking.transactions(created_at);

CREATE INDEX idx_sender
ON banking.transactions(sender_account);

CREATE INDEX idx_receiver
ON banking.transactions(receiver_account);