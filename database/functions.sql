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