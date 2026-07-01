-- 1. Function: search by pattern (name or phone)
CREATE OR REPLACE FUNCTION search_by_pattern(pattern VARCHAR)
RETURNS TABLE(id INT, name VARCHAR, phone VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    RETURN QUERY
        SELECT p.id, p.name, p.phone
        FROM phonebook p
        WHERE p.name ILIKE '%' || pattern || '%'
           OR p.phone ILIKE '%' || pattern || '%';
END;
$$;

-- 2. Function: get data with pagination
CREATE OR REPLACE FUNCTION get_paginated(page_limit INT, page_offset INT)
RETURNS TABLE(id INT, name VARCHAR, phone VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    RETURN QUERY
        SELECT p.id, p.name, p.phone
        FROM phonebook p
        ORDER BY p.id
        LIMIT page_limit OFFSET page_offset;
END;
$$;
