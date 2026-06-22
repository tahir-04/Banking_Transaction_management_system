CREATE TABLE banking.customers (
    customer_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50),
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(15) UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    is_verified BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE banking.accounts (
    account_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    customer_id UUID NOT NULL,

    account_number VARCHAR(20) UNIQUE NOT NULL,

    account_type VARCHAR(20) NOT NULL,

    balance DECIMAL(18,2) DEFAULT 0,

    currency VARCHAR(10) DEFAULT 'INR',

    status VARCHAR(20) DEFAULT 'ACTIVE',

    minimum_balance DECIMAL(18,2)
        DEFAULT 500,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (customer_id)
    REFERENCES banking.customers(customer_id)
);

CREATE TABLE banking.transactions (
    transaction_id UUID PRIMARY KEY
        DEFAULT uuid_generate_v4(),

    sender_account UUID,

    receiver_account UUID,

    transaction_type VARCHAR(30),

    amount DECIMAL(18,2),

    description TEXT,

    reference_number VARCHAR(100),

    status VARCHAR(20),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(sender_account)
        REFERENCES banking.accounts(account_id),

    FOREIGN KEY(receiver_account)
        REFERENCES banking.accounts(account_id)
);

CREATE TABLE banking.beneficiaries (
    beneficiary_id UUID PRIMARY KEY
        DEFAULT uuid_generate_v4(),

    customer_id UUID,

    beneficiary_account VARCHAR(20),

    beneficiary_name VARCHAR(100),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(customer_id)
        REFERENCES banking.customers(customer_id)
);

CREATE TABLE banking.notifications (
    notification_id UUID PRIMARY KEY
        DEFAULT uuid_generate_v4(),

    customer_id UUID,

    message TEXT,

    status VARCHAR(20),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(customer_id)
        REFERENCES banking.customers(customer_id)
);

CREATE TABLE banking.audit_logs (
    audit_id UUID PRIMARY KEY
        DEFAULT uuid_generate_v4(),

    customer_id UUID,

    action VARCHAR(200),

    metadata JSONB,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(customer_id)
        REFERENCES banking.customers(customer_id)
);

CREATE TABLE banking.sessions (
    session_id UUID PRIMARY KEY
        DEFAULT uuid_generate_v4(),

    customer_id UUID,

    refresh_token TEXT,

    expires_at TIMESTAMP,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(customer_id)
        REFERENCES banking.customers(customer_id)
);

ALTER TABLE banking.accounts
ADD CONSTRAINT chk_account_type
CHECK (
    account_type IN
    ('SAVINGS','CURRENT')
);

ALTER TABLE banking.accounts
ADD CONSTRAINT chk_balance
CHECK (
    balance >= 0
);

ALTER TABLE banking.accounts
ADD CONSTRAINT chk_status
CHECK (
    status IN
    ('ACTIVE','FROZEN','CLOSED')
);

ALTER TABLE banking.transactions
ADD CONSTRAINT chk_amount
CHECK (
    amount > 0
);

ALTER TABLE banking.transactions
ADD CONSTRAINT chk_transaction_status
CHECK (
    status IN
    ('SUCCESS','FAILED','PENDING')
);