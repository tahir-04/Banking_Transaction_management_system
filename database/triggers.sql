CREATE TRIGGER customer_timestamp
BEFORE UPDATE
ON banking.customers
FOR EACH ROW
EXECUTE FUNCTION
banking.update_timestamp();