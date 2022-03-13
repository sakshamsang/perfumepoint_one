from sqlalchemy import create_engine, MetaData
from apps import db
import pandas as pd

engine = create_engine(
    'mysql+pymysql://admin:Yvb!e19ztrNe*aE$7!@perfumepoint.ck8lusdzobbh.ap-south-1.rds.amazonaws.com/staging')

meta = MetaData()


def states_tuples():
    states_sql = """ select * from states """
    states = pd.read_sql(states_sql, engine.connect())
    return list(zip(states['id'], states['name']))


def company_tuples():
    states_sql = """ select * from company """
    states = pd.read_sql(states_sql, engine.connect())
    return list(zip(states['id'], states['name']))


def manager_tuples():
    states_sql = """ select * from states """
    states = pd.read_sql(states_sql, engine.connect())
    return list(zip(states['id'], states['name']))


def roles_tuples():
    states_sql = """ select * from states """
    states = pd.read_sql(states_sql, engine.connect())
    return list(zip(states['id'], states['name']))


def brand_tuples():
    states_sql = """ select * from states """
    states = pd.read_sql(states_sql, engine.connect())
    return list(zip(states['id'], states['name']))


def category_tuples():
    states_sql = """ select * from states """
    states = pd.read_sql(states_sql, engine.connect())
    return list(zip(states['id'], states['name']))


def product_search(code=None):
    if code == None:
        product_sql = """ SELECT products.name, products.code, products.oBarcode, products.mrp,
                     products.discount, products.tax, products.hsncode, products.brand, products.group from products """
    else:
        product_sql = """ SELECT * from products where products.code in ('{}') """.format(code)
    products = pd.read_sql(product_sql, engine.connect())
    return products


def companytable():

    query = "SELECT company.id, company.name, company.phone, company.address, company.gstNo, company.regdNo FROM company"

    df = pd.read_sql_query(query, engine.connect())
    return df


def employeestable():

    query = "Select b.id, b.name, b.email, a.name as mName, company.name, b.created_at from (SELECT users.id, users.name, users.email, users.managerId, users.companyId, users.created_at FROM users) as b LEFT JOIN (Select users.id, users.name from users) as a ON b.managerId = a.id LEFT JOIN company ON company.id = b.companyId"

    df = pd.read_sql_query(query, engine.connect())
    return df


def messagestable():

    query = "SELECT messages.id, messages.campaign, messages.group_id, messages.name, messages.mobile, messages.scheduled_for, messages.message FROM messages"

    df = pd.read_sql_query(query, engine.connect())
    return df


def partytable():

    query = "SELECT customers.id, customers.name, customers.gender, customers.dob, customers.phone, customers.email, customers.city, states.name, customers.address, customers.wallet_active, customers.gstNo FROM customers LEFT JOIN states ON states.id = customers.stateId"

    df = pd.read_sql_query(query, engine.connect())
    return df


def purchasestable():

    query = "SELECT purchases.id, purchases.name, purchases.phone, purchases.name, purchases.city, purchases.address, purchases.email, purchases.gstNo, purchases.dob, purchases.gender, purchases.wallet_active FROM customers LEFT JOIN states ON states.id = customers.stateId"

    df = pd.read_sql_query(query, engine.connect())
    return df


def productstable():

    query = "SELECT products.id, products.name, products.code, products.group, products.brand, products.mrp, products.discount, products.price, products.tax, products.expiry, products.oBarcode, products.cBarcode, products.hsnCode, products.hsnName, products.updated_at FROM products "

    df = pd.read_sql_query(query, engine.connect())
    return df


def invoicestable():

    query = "SELECT invoices.id, invoices.invoiceNo, invoices.invoiceType, invoices.orderId, invoices.invoiceDate, invoices.totalAmount, invoices.paymentMode FROM invoices"

    df = pd.read_sql_query(query, engine.connect())
    return df


def paymentstable():

    query = "SELECT payments.id, payments.invoiceNo, payments.paymentDate, payments.paymentFrom, payments.paymentTo, payments.amount, payments.mode, payments.remarks FROM payments"

    df = pd.read_sql_query(query, engine.connect())
    return df


def salestable():

    query = "SELECT sales.id, sales.name, sales.phone, sales.name, sales.city, sales.address, sales.email, sales.gstNo, sales.dob, sales.gender, sales.wallet_active FROM customers LEFT JOIN states ON states.id = customers.stateId"

    df = pd.read_sql_query(query, engine.connect())
    return df


def stockstable():

    query = "SELECT stocks.id, stocks.productId, stocks.quantity, stocks.purchasePrice, stocks.salePrice, stocks.saleDiscount, stocks.purchasedForId, stocks.purchasedFromId, stocks.purchasedOn, stocks.invoiceNo FROM stocks"

    df = pd.read_sql_query(query, engine.connect())
    return df

def orderstable():

    # query = """SELECT orders.id, orders.invoiceId, orders.orderId, company.name, orders.productId, products.name, orders.mrp, orders.discount, orders.price, orders.qty, 
    #         orders.gst, orders.taxAmt, orders.discAmt, orders.totalDiscAmt, orders.cgstAmt, orders.sgstAmt, orders.igstAmt, orders.totalTaxAmt, orders.total, 
    #         CASE WHEN orders.created_at is null THEN invoices.created_at ELSE orders.created_at END as created_at
    #         FROM orders LEFT JOIN company ON company.id = orders.companyId LEFT JOIN products ON products.id = orders.productId
    #         LEFT JOIN invoices on invoices.id = orders.invoiceId LIMIT 100000
    #         """
    query = """SELECT
    company.name AS CompanyName,
    products.name AS ProductName,
    products.price AS Price,
    products.brand,
    T.YM,
    (
        T.Total - T.TotalBought + T.TotalSold
    ) * products.price AS TotalOpeningPrice,
    T.Total - T.TotalBought + T.TotalSold AS TotalOpening,
    T.TotalBought,
    T.TotalSold,
    T.Total * products.price AS TotalClosingPrice,
    T.Total AS TotalClosing
FROM
    (
    SELECT
        C.productId,
        C.purchasedForId,
        C.TotalBought,
        C.TotalSold,
        C.YM,
        IF(
            @prev <> productId,
            @x := C.TotalBought - C.TotalSold,
            @x := C.TotalBought - C.TotalSold + @x
        ) AS Total,
        @prev := productId
    FROM
        (
        SELECT
            A.productId,
            A.purchasedForId,
            A.TotalBought,
            CASE WHEN B.TotalSold IS NULL THEN 0 ELSE B.TotalSold
    END AS TotalSold,
    A.YM
FROM
    (
    SELECT
        stocks.productId,
        stocks.purchasedForId,
        SUM(stocks.quantity) AS TotalBought,
        DATE_SUB(
            LAST_DAY(stocks.purchasedOn),
            INTERVAL DAY(LAST_DAY(stocks.purchasedOn)) - 1 DAY
        ) AS YM
    FROM
        stocks
    GROUP BY
        stocks.productId,
        stocks.purchasedForId,
        YM
) AS A
LEFT JOIN(
    SELECT
        orders.productId,
        orders.companyId,
        SUM(orders.qty) AS TotalSold,
        DATE_SUB(
            LAST_DAY(
                CASE WHEN orders.created_at IS NULL THEN invoices.created_at ELSE orders.created_at
            END
        ),
        INTERVAL DAY(
            LAST_DAY(
                CASE WHEN orders.created_at IS NULL THEN invoices.created_at ELSE orders.created_at
            END
        )
) - 1 DAY
) AS YM
FROM
    orders
LEFT JOIN invoices ON orders.invoiceId = invoices.id
GROUP BY
    orders.productId,
    orders.companyId,
    YM
) AS B
ON
    A.YM = B.YM AND A.productId = B.productId AND A.purchasedForId = B.companyId
ORDER BY
    A.productId,
    A.purchasedForId,
    A.YM
) AS C,
(
SELECT
    @x := 0
) AS X,
(
SELECT
    @prev := 1
) AS Y
) AS T
LEFT JOIN products ON T.productId = products.id
LEFT JOIN company ON T.purchasedForId = company.id"""


    # result = conn.execute(query).fetchall()

    # df = pd.DataFrame(result)
    # df.columns = ['ID', 'InvoiceID', 'OrderID', 'Company', 'ProductID', 'Product',
    #               'MRP', 'Discount', 'Price', 'Quantity', 'GST', 'TaxAmt', 'Discount', 'TotalDisc',
    #               'CGST', 'SGST', 'IGST', 'TotalTaxAmt', 'Total', 'Date']
    # df['Date'] = pd.to_datetime(df['Date']).dt.date
    # df['Month'] = pd.to_datetime(df['Date']).dt.to_period('M')
    # df = df.astype({'Month': str})
    # df['Year'] = pd.to_datetime(df['Date']).dt.year


    df = pd.read_sql(query, engine.connect())
   
    return df
