import snowflake.connector

# Connect to Snowflake
conn = snowflake.connector.connect(
    user='AMARDIPKUMAR',
    password='Rudra@4820241234',
    account='ji00828.ap-southeast-1',
    warehouse='COMPUTE_WH',
    database='TEST_DB',
    schema='SALES_SCHEMA'
)

# Create a cursor
cur = conn.cursor()

# Execute SQL
cur.execute("SELECT * FROM customers LIMIT 10")

# Fetch results
rows = cur.fetchall()
for row in rows:
    print(row)

# Close connections
cur.close()
conn.close()
