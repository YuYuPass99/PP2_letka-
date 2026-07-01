-- 1. Procedure: upsert single contact (insert or update phone if exists)
CREATE OR REPLACE PROCEDURE upsert_contact(p_name VARCHAR, p_phone VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM phonebook WHERE name = p_name) THEN
        UPDATE phonebook SET phone = p_phone WHERE name = p_name;
    ELSE
        INSERT INTO phonebook (name, phone) VALUES (p_name, p_phone);
    END IF;
END;
$$;

-- 2. Procedure: insert many users from list, validate phones, return invalid ones
CREATE OR REPLACE PROCEDURE insert_many_users(
    p_names VARCHAR[],
    p_phones VARCHAR[],
    OUT invalid_data TEXT
)
LANGUAGE plpgsql AS $$
DECLARE
    i INT;
    bad TEXT := '';
BEGIN
    FOR i IN 1 .. array_length(p_names, 1) LOOP
        -- Phone validation: must be 10-15 digits, optionally starting with +
        IF p_phones[i] !~ '^\+?[0-9]{10,15}$' THEN
            bad := bad || 'Invalid: ' || p_names[i] || ' / ' || p_phones[i] || E'\n';
        ELSE
            IF EXISTS (SELECT 1 FROM phonebook WHERE name = p_names[i]) THEN
                UPDATE phonebook SET phone = p_phones[i] WHERE name = p_names[i];
            ELSE
                INSERT INTO phonebook (name, phone) VALUES (p_names[i], p_phones[i]);
            END IF;
        END IF;
    END LOOP;

    invalid_data := CASE WHEN bad = '' THEN 'All records valid.' ELSE bad END;
END;
$$;

-- 3. Procedure: delete by name or phone
CREATE OR REPLACE PROCEDURE delete_contact(p_name VARCHAR DEFAULT NULL, p_phone VARCHAR DEFAULT NULL)
LANGUAGE plpgsql AS $$
BEGIN
    IF p_name IS NOT NULL THEN
        DELETE FROM phonebook WHERE name = p_name;
    END IF;
    IF p_phone IS NOT NULL THEN
        DELETE FROM phonebook WHERE phone = p_phone;
    END IF;
END;
$$;
