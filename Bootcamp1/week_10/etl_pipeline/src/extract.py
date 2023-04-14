import psycopg2
import pandas as pd


# connect to redshift

def connect_to_redshift(dbname, host, port, user, password):
    """Method that connects to redshift. This gives a warning so will look for another solution"""

    connect = psycopg2.connect(
        dbname=dbname, host=host, port=port, user=user, password=password
    )

    print("connection to redshift made")

    return connect


def extract_transactional_data(dbname, host, port, user, password):
    """This method connects to redshift and extracts customer transactions data.

     1. Removes all customers with no customer id
     2. Joins descriptions to do the online transaction table, and replaces missing values and ? with Unknown
     3. Removes all invoices that have the stock code postage, bank changes, d, m and cruk
     4. Removes all invoices where quantity is less than 0

     """

    # connect to redshift
    connect = connect_to_redshift(dbname, host, port, user, password)

    # write query that extract data

    query = """select t1.*,
                      case when t2.Description = '?' or t2.Description is null then 'Unknown' 
                        else t2.Description end as Description
                from bootcamp1.online_transactions t1
                left join bootcamp1.stock_description t2 on t1.stock_code = t2.stock_code
                where customer_id <> ''
                    and t1.stock_code not in ('POSTAGE', 'BANK CHARGES', 'D', 'M', 'CRUK')
                    and t1.quantity > 0
               """

    online_transactions_reduced = pd.read_sql(query, connect)

    print(f"The data frame contains {online_transactions_reduced.shape[0]} invoices")

    return online_transactions_reduced
