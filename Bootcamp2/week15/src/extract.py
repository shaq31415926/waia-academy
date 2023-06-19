import psycopg2
import pandas as pd


def connect_to_redshift(dbname, host, port, user, password):
    """Method that connects to redshift. This gives a warning so will look for another solution"""

    connect = psycopg2.connect(
        dbname=dbname, host=host, port=port, user=user, password=password
    )

    print("connection to redshift made")

    return connect


def extract_transactional_data(dbname, host, port, user, password):
    """
    This function connects to redshift and carries out the following transformation tasks
    1. Removes all rows where customer id is missing
    2. Removes the stock codes M, D, CRUK, POST, BANK CHARGES,
    3. Adds description to the online transactions table
    4. Replaces missing stock description with Unknown
    5. Fixes the data type of invoice date
    6. Create a new variable called total order value
    """


    # connect to redshift
    connect = connect_to_redshift(dbname, host, port, user, password)

    # read the sql query which does the following

    query = """
    SELECT ot.invoice, 
       ot.stock_code,
       CASE WHEN s.description IS NULL THEN 'Unknown'
            ELSE s.description END AS description,
       ot.price,
       ot.quantity,
       /*add a variable that gives the total order value*/
       ot.price*ot.quantity as total_order_value,
       CAST(invoice_date As DateTime) AS invoice_date,
       ot.customer_id,
       ot.country
FROM bootcamp.online_transactions ot
/* this is a subquery that removes '?' from the stock_description table */
LEFT JOIN (SELECT *
           FROM bootcamp.stock_description
           WHERE description <> '?') AS s ON ot.stock_code = s.stock_code
WHERE ot.customer_id <> ''
  AND ot.stock_code NOT IN ('BANK CHARGES', 'POST', 'D', 'M', 'CRUK')
    """
    online_trans_cleaned = pd.read_sql(query, connect)

    print("The shape of the extracted and transformed data is", online_trans_cleaned.shape)

    return online_trans_cleaned
