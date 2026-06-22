ALTER TABLE banking.transactions
ADD CONSTRAINT chk_transaction_status
CHECK (
    status IN
    ('SUCCESS','FAILED','PENDING')
);