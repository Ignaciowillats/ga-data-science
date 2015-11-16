#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import sqlite3

# Create/open local db file
db = sqlite3.connect('db.db')

# Get cursor
cursor = db.cursor()

# Create table
cursor.execute("""
    CREATE TABLE flats (
        id INTEGER PRIMARY KEY,
        source TEXT,
        source_id TEXT,
        url TEXT,
        postcode TEXT
        );
    """)
db.commit()

# Drop table
cursor.execute("""
    DROP table flats;
    """)
db.commit()

# Add data
cursor.execute("""
    INSERT INTO flats(
        source,
        source_id,
        url,
        postcode)
    VALUES (?, ?, ?, ?);
    """, (
    'rightmove',
    '46745021',
    'http://www.rightmove.co.uk/property-to-rent/property-46745021.html',
    'N1 0DQ'
))
db.commit()

# Alternatively
cursor.execute('''
    INSERT INTO flats(
        source,
        source_id,
        url,
        postcode)
    VALUES (
        :source,
        :source_id,
        :url,
        :postcode
    );
''', {
    'source': 'rightmove',
    'source_id': '46745021',
    'url': 'http://www.rightmove.co.uk/property-to-rent/property-46745021.html',
    'postcode': 'N1 0DQ'
})
db.commit()


# Get id of last row inserted
last_row_id = cursor.lastrowid

# Retrieving data
cursor.execute("""
    SELECT source, source_id, url, postcode
    FROM flats;
    """)
all_rows = cursor.fetchall()  # Iterator object
for (source, source_id, url, postcode) in all_rows:
    print postcode

# Where example
cursor.execute("""SELECT postcode FROM flats WHERE id = ?;""", ('1',))
where_example = cursor.fetchone()

# Update
cursor.execute("""
    UPDATE flats
    SET postcode = 'xxx xxx'
    WHERE id = ?;
    """, (1,))
db.commit()

# Delete
cursor.execute("""
    DELETE FROM flats
    WHERE id = ?;
    """, (1,))
db.commit()

# Close conn
db.close()
