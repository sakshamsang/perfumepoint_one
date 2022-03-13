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


def product_search():
    product_sql = """ SELECT products.name, products.code, products.oBarcode, products.mrp,
                     products.discount, products.tax from products """
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
