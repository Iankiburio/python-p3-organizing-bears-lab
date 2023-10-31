select_all_female_bears_return_name_and_age = """
    SELECT
        name,
        age
    FROM
        bears
    WHERE
        sex = 'F';
"""

select_all_bears_names_and_orders_in_alphabetical_order = """
    SELECT
        name,
        age
    FROM
        bears
    WHERE
        name IS NOT NULL
    ORDER BY
        name COLLATE NOCASE ASC;
"""

select_all_bears_names_and_ages_that_are_alive_and_order_youngest_to_oldest = """
    SELECT
        name,
        age
    FROM
        bears
    WHERE
        alive = true
    ORDER BY
        age ASC;
"""

select_oldest_bear_and_returns_name_and_age = """
    SELECT
        name,
        age
    FROM
        bears
    WHERE
        age = (SELECT MAX(age) FROM bears WHERE age IS NOT NULL AND ALIVE = true);
"""

select_youngest_bear_and_returns_name_and_age = """
    SELECT
        name,
        age
    FROM
        bears
    WHERE
        age = (SELECT MIN(age) FROM bears);
"""