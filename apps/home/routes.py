# -*- encoding: utf-8 -*-

from datetime import datetime
import email
from unicodedata import name

import flask
from apps.home import blueprint
from flask import render_template, request, redirect, url_for
from flask_login import current_user, login_required
from jinja2 import TemplateNotFound
from apps import db
from apps.home.databases import engine, orderstable, product_search
from apps.home.databases import companytable, employeestable, partytable, productstable, paymentstable, purchasestable, messagestable, salestable, stockstable, invoicestable, orderstable
from apps.home.forms import CustomerForm, InvoiceGenerator, CompanyForm, UserForm, ProductForm, StockForm


@blueprint.route('/index')
@login_required
def index():
    orders = orderstable()
    return render_template('home/index.html', df=orders)


# # Custom pages start


@blueprint.route('/company')
@login_required
def company():

    return render_template('home/company.html', df=companytable())


@blueprint.route('/party')
@login_required
def party():

    return render_template('home/party.html', df=partytable())


@blueprint.route('/employees')
@login_required
def employees():

    return render_template('home/employees.html', df=employeestable())


@blueprint.route('/payments')
@login_required
def payments():

    return render_template('home/payments.html', df=paymentstable())


@blueprint.route('/purchases')
@login_required
def purchases():

    return render_template('home/purchases.html', df=purchasestable())


@blueprint.route('/invoices')
@login_required
def invoices():

    return render_template('home/invoices.html', df=invoicestable())


@blueprint.route('/products')
@login_required
def products():

    return render_template('home/products.html', df=productstable())


@blueprint.route('/messages')
@login_required
def messages():

    return render_template('home/messages.html', df=messagestable())


@blueprint.route('/sales')
@login_required
def sales():

    return render_template('home/sales.html', df=salestable())


@blueprint.route('/stocks')
@login_required
def stocks():

    return render_template('home/stocks.html', df=stockstable())

# # Custom pages end

# # Custom forms start


@blueprint.route('/cust_add', methods=['GET', 'POST'])
def cust_add():
    customer_form = CustomerForm(request.form)
    if request.method == 'POST':
        if 'cust_add' in request.form:

            # read form data
            name = request.form['name']
            email = request.form['email'] or "None"

            email_query = """SELECT * FROM customers WHERE email = '{}'""".format(
                email)
            if engine.connect().execute(email_query).fetchone():
                return render_template('forms/customer_add.html',
                                       form=customer_form,
                                       msg="Email already registered.")

            phone = request.form['phone']
            phone_query = """SELECT * FROM customers WHERE phone = '{}'""".format(
                phone)
            if engine.connect().execute(phone_query).fetchone():
                return render_template('forms/customer_add.html',
                                       form=customer_form,
                                       msg="Phone already registered.")
            gender = request.form.get('customRadioInline1')
            wallet = request.form.get('customCheck1') or 0
            dob = request.form['dob'] or "NULL"
            state = request.form['state']
            city = request.form['city'] or "None"
            address = request.form['address'] or "None"
            gstno = request.form['gstno'] or "None"

        if customer_form.validate_on_submit:
            query = """INSERT INTO customers(name, phone, stateId, city, address, email, gstNo, addedBy, created_at, 
                    updated_at, dob, gender, wallet_active) VALUES ('{}','{}',{},'{}',
                    '{}','{}','{}',{},'{}','{}',{},'{}',{})""".format(name, phone, state, city, address, email, gstno, flask.session['_user_id'], datetime.now(), datetime.now(), dob, gender, wallet)
            engine.connect().execute(query)
            return redirect(url_for('home_blueprint.party'))

    return render_template('forms/customer_add.html', form=customer_form)


@blueprint.route('/comp_add', methods=['GET', 'POST'])
def comp_add():
    company_form = CompanyForm(request.form)
    if request.method == 'POST':
        if 'cust_add' in request.form:

            # read form data
            name = request.form['name']
            address = request.form['address']
            city = request.form['city']
            state = request.form['state']
            website = request.form['website']
            email = request.form['email']
            pincode = request.form['pincode']
            tinno = request.form['tinno']
            regddate = request.form['regddate']
            panno = request.form['panno']
            cinno = request.form['cinno']
            phone = request.form['phone']
            landline = request.form['landline']
            regdno = request.form['regdno']
            gstno = request.form['gstno']

        if company_form.validate_on_submit:
            query = """INSERT INTO company(name, address, city, stateId, website, email, pincode, tinNo, regdDate, panNo, cinNo, phone, landline, regdNo, gstNo, addedBy, created_at, updated_at) 
                VALUES ('{}','{}','{}',{},'{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')""".format(
                name, address, city, state, website, email, pincode, tinno, regddate, panno, cinno, phone, landline, regdno, gstno, flask.session['_user_id'], datetime.now(), datetime.now())
            engine.connect().execute(query)
            return redirect(url_for('home_blueprint.company'))

    return render_template('forms/company_add.html', form=company_form)


@blueprint.route('/product_add', methods=['GET', 'POST'])
def product_add():
    product_form = ProductForm(request.form)
    if request.method == 'POST':
        if 'prod_add' in request.form:

            # read form data
            name = request.form['name']
            code = request.form['code']
            brand = request.form['brand']
            category = request.form['category']
            mrp = request.form['mrp']
            discount = request.form['discount']
            price = request.form['price']
            taxrate = request.form['taxrate']
            unit = request.form['unit']
            rackno = request.form['rackno']
            expiry = request.form['expiry']
            hsncode = request.form['hsncode']
            hsnname = request.form['hsnname']
            obarcode = request.form['obarcode']
            cbarcode = request.form['cbarcode']

        if product_form.validate_on_submit:
            query = """INSERT INTO products(name, code, brand, group, mrp, discount, price, tax, unit, rack, expiry, hsnCode, hsnName, oBarcode, cBarcode, addedBy, created_at, updated_at) 
                VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')""".format(
                name, code, brand, category, mrp, discount, price, taxrate, unit, rackno, expiry, hsncode, hsnname, obarcode, cbarcode, flask.session['_user_id'], datetime.now(), datetime.now())
            engine.connect().execute(query)
            return redirect(url_for('home_blueprint.products'))

    return render_template('forms/product_add.html', form=product_form)


# @blueprint.route('/user_add', methods=['GET', 'POST'])
# def user_add():
#     user_form = UserForm(request.form)
#     if request.method == 'POST':
#         if 'user_add' in request.form:

#             # read form data
#             name = request.form

#         if customer_form.validate_on_submit:
#             query = """INSERT INTO customers(name, phone, stateId, city, address, email, gstNo, addedBy, created_at,
#                     updated_at, dob, gender, wallet_active) VALUES ('{}','{}',{},'{}',
#                     '{}','{}','{}',{},'{}','{}',{},'{}',{})""".format(name, phone, state, city, address, email, gstno, flask.session['_user_id'], datetime.now(), datetime.now(), dob, gender, wallet)
#             engine.connect().execute(query)
#             return redirect(url_for('home_blueprint.party'))

#     return render_template('forms/customer_add.html', form=customer_form)
table = []
invoiceNo = None
orderId = None
companyId = None
invoiceId = None


@blueprint.route('/invoice_gen', methods=['GET', 'POST'])
def invoice_gen():
    form = InvoiceGenerator(request.form)

    df = product_search()

    global invoiceNo
    global orderId
    global companyId
    global invoiceId
    global table

    if 'row_add' in request.form:
        code = request.form.get('product_code')
        qty = request.form.get('product_qty')
        disc = request.form.get('product_discount')
        productInfo = product_search(code)

        if invoiceNo == None:
            companyId = engine.connect().execute("Select User.companyId from User where id={}".format(
                flask.session['_user_id'])).fetchone()[0]
            invoiceId = engine.connect().execute(
                "Select MAX(invoices.id) from invoices").fetchone()[0]+1
            invoiceNo = "" + \
                str(companyId) + "IN" + datetime.today().strftime('%Y%m%d') + \
                str(invoiceId).zfill(10)
            orderId = "" + \
                str(companyId) + "OR" + datetime.today().strftime('%Y%m%d') + \
                str(invoiceId).zfill(10)

        orders_query = """INSERT INTO orders (invoiceId, orderId, companyId, productId, mrp, discount, price, qty, gst, 
            taxAmt, discAmt, totalDiscAmt, cgstAmt, sgstAmt, totalTaxAmt, total, addedBy, created_at,
            updated_at) values ('{}', '{}', {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, '{}', 
            '{}', '{}')""".format(
            invoiceId, orderId, companyId, productInfo['id'].item(), productInfo['mrp'].item(), disc, round(
                productInfo['mrp'].item()*(1-float(disc)/100), 2), int(qty), productInfo['tax'].item(),
            round(productInfo['mrp'].item()*0.18/1.18, 2), round(productInfo['mrp'].item()*(float(disc)/100), 2), round(
                productInfo['mrp'].item()*(float(disc)/100)*int(qty), 2), round(productInfo['mrp'].item()*0.18/2.36, 2),
            round(productInfo['mrp'].item()*0.18/2.36, 2),   round(productInfo['mrp'].item()*0.18/1.18*int(qty), 2),  round(productInfo['mrp'].item()*(1-float(disc)/100)*int(qty), 2), flask.session['_user_id'], datetime.now(), datetime.now())

        table.append(orders_query)

        # orders_query.append("""Insert into orders () """)
        return redirect(url_for('home_blueprint.invoice_gen'))

    if ' generate_invoice' in request.form:

        invoice_query = """Insert into invoices (invoiceNo, orderId, invoiceDate, 
        companyid, customerId, totalCGST, totalSGST, totalIGST, totalTaxRs, totalItems, totalQty, totalAmount, totalDiscount,
         totalPayable, paymentMode, paymentRef, addedBy, created_at, updated_at) values ('{}', '{}', '{}', '{}', '{}', '{}', '{}',
          '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', )"""

        table = []
        invoiceNo = None
        orderId = None
        companyId = None
        invoiceId = None
        return redirect(url_for('home_blueprint.invoice_gen'))

    return render_template('forms/invoice_gen.html', form=form, df=df)

# # Custom forms end


@blueprint.route('/<template>')
@login_required
def route_template(template):

    try:

        if not template.endswith('.html'):
            template += '.html'

        # Detect the current page
        segment = get_segment(request)

        # Serve the file (if exists) from app/templates/home/FILE.html
        return render_template("home/" + template, segment=segment)

    except TemplateNotFound:
        return render_template('home/page-404.html'), 404

    except:
        return render_template('home/page-500.html'), 500


# Helper - Extract current page name from request
def get_segment(request):

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment

    except:
        return None
