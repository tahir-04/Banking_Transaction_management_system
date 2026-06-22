CREATE OR REPLACE FUNCTION
banking.update_timestamp()
RETURNS TRIGGER AS
$$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER customer_timestamp
BEFORE UPDATE
ON banking.customers
FOR EACH ROW
EXECUTE FUNCTION
banking.update_timestamp();