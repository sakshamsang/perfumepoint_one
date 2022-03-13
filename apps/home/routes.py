# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from datetime import datetime
from unicodedata import name

import flask
from apps.home import blueprint
from flask import render_template, request, redirect, url_for
from flask_login import current_user, login_required
from jinja2 import TemplateNotFound
from apps import db
from apps.home.databases import engine, product_search
from apps.home.databases import companytable, employeestable, partytable, productstable, paymentstable, purchasestable, messagestable, salestable, stockstable, invoicestable
from apps.home.forms import CustomerForm, InvoiceGenerator, CompanyForm , UserForm, ProductForm, StockForm


@blueprint.route('/index')
@login_required
def index():

    return render_template('home/index.html', segment='index')


# # Custom pages start

@blueprint.route('/test')
@login_required
def test():
    print(flask.session)
    return render_template('home/test.html', df=companytable())


@blueprint.route('/company')
@login_required
def company():

    return render_template('home/company.html', df=companytable())


@blueprint.route('/party')
@login_required
def party():

    return render_template('tables/party.html', df=partytable())


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
            print('Yeh bhi')
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
            email = request.form['email'] or "None"

            email_query = """SELECT * FROM customers WHERE email = '{}'""".format(
                email)

            if engine.connect().execute(email_query).fetchone():
                print('Yeh chala')
                return render_template('forms/customer_add.html',
                                       form=company_form,
                                       msg="Email already registered.")

            phone = request.form['phone']
            gender = request.form.get('customRadioInline1')
            wallet = request.form.get('customCheck1') or 0
            dob = request.form['dob'] or "NULL"
            state = request.form['state']
            city = request.form['city'] or "None"
            address = request.form['address'] or "None"
            gstno = request.form['gstno'] or "None"

        if company_form.validate_on_submit:
            print('Yeh bhi')
            query = """INSERT INTO customers(name, phone, stateId, city, address, email, gstNo, addedBy, created_at, 
                    updated_at, dob, gender, wallet_active) VALUES ('{}','{}',{},'{}',
                    '{}','{}','{}','{}','{}','{}',{},'{}',{})""".format(name, phone, state, city, address, email, gstno, current_user, datetime.now(), datetime.now(), dob, gender, wallet)
            engine.connect().execute(query)
            return redirect(url_for('home_blueprint.party'))

    return render_template('forms/company_add.html', form=company_form)

@blueprint.route('/product_add', methods=['GET', 'POST'])
def product_add():
    product_form = ProductForm(request.form)
    if request.method == 'POST':
        if 'cust_add' in request.form:

            # read form data
            name = request.form['name']
            email = request.form['email'] or "None"

            email_query = """SELECT * FROM customers WHERE email = '{}'""".format(
                email)

            if engine.connect().execute(email_query).fetchone():
                print('Yeh chala')
                return render_template('forms/customer_add.html',
                                       form=product_form,
                                       msg="Email already registered.")

            phone = request.form['phone']
            gender = request.form.get('customRadioInline1')
            wallet = request.form.get('customCheck1') or 0
            dob = request.form['dob'] or "NULL"
            state = request.form['state']
            city = request.form['city'] or "None"
            address = request.form['address'] or "None"
            gstno = request.form['gstno'] or "None"

        if product_form.validate_on_submit:
            print('Yeh bhi')
            query = """INSERT INTO customers(name, phone, stateId, city, address, email, gstNo, addedBy, created_at, 
                    updated_at, dob, gender, wallet_active) VALUES ('{}','{}',{},'{}',
                    '{}','{}','{}','{}','{}','{}',{},'{}',{})""".format(name, phone, state, city, address, email, gstno, current_user, datetime.now(), datetime.now(), dob, gender, wallet)
            engine.connect().execute(query)
            return redirect(url_for('home_blueprint.party'))

    return render_template('forms/product_add.html', form=product_form)


@blueprint.route('/invoice_gen', methods=['GET', 'POST'])
def invoice_gen():
    form = InvoiceGenerator(request.form)

    df = product_search()

    return render_template('forms/invoice_gen.html', form=form, name=df['name'].to_list())

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
