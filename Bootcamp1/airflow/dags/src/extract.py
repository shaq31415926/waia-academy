import os
import psycopg2
import pandas as pd


def connect_to_redshift(dbname, host, port, user, password):

    connect = psycopg2.connect(
        dbname=dbname, host=host, port=port, user=user, password=password
    )
    print("connection to redshift made")

    return connect


def extract_transactional_data(dbname, host, port, user, password):

    connect = connect_to_redshift(dbname, host, port, user, password)

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