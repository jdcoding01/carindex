from helpers.database_manager import DatabaseManager


encuentra24PreferencesTables = """

CREATE TABLE IF NOT EXISTS encuentra24_preferences (
    id integer PRIMARY KEY,
    uid text NOT NULL,
    marca text NOT NULL,
    modelo text NOT NULL,
    year text NOT NULL,
    precio text NOT NULL,
    available_timestamp text NOT_NULL,
    unavailable_timestamp text default "null"
);

"""


DatabaseManager("encuentra24").create_table(encuentra24PreferencesTables)


encuentra24CrPreferencesTables = """

CREATE TABLE IF NOT EXISTS encuentra24_cr_preferences (
    id integer PRIMARY KEY,
    uid text NOT NULL,
    marca text NOT NULL,
    modelo text NOT NULL,
    year text NOT NULL,
    precio text NOT NULL,
    available_timestamp text NOT_NULL,
    unavailable_timestamp text default "null"
);

"""


DatabaseManager("encuentra24_cr").create_table(encuentra24CrPreferencesTables)




