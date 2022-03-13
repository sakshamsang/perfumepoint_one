from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, RadioField, BooleanField, DateField, SelectField, TextAreaField, IntegerField, FloatField
from wtforms.validators import Email, DataRequired, Length
from apps.home.databases import states_tuples, company_tuples, manager_tuples, roles_tuples, brand_tuples, category_tuples


class InvoiceGenerator(FlaskForm):
    product_name = StringField('Product Name')
    product_code = StringField('Product Code')
    product_oBarcode = StringField('Product Barcode')
    product_qty = IntegerField('Quantity')
    product_discount = FloatField('Discount')
    subtotal = FloatField('Subtotal')


class CustomerForm(FlaskForm):
    name = StringField('Name*',
                       id='customer_name',
                       validators=[DataRequired()])
    email = EmailField('Email Address',
                       id='customer_email',
                       validators=[Email()])
    phone = StringField('Phone Number*',
                        id='customer_phone',
                        validators=[DataRequired(), Length(min=8, max=10)])
    dob = DateField('Date of Birth',
                    id='customer_dob')
    state = SelectField('State*',
                        id='customer_states',
                        choices=states_tuples(),
                        validators=[DataRequired()])
    city = StringField('City',
                       id='customer_city')
    address = TextAreaField('Address',
                            id='customer_address')
    gstno = StringField('GST Number',
                        id='customer_gst')
    wallet = BooleanField('Wallet',
                          id='customCheck1',
                          name='customCheck1')
    gender = RadioField("Gender", 
                        name="customRadioInline1",
                        choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])

class CompanyForm(FlaskForm):
    name = StringField('Name*',
                       id='company_name',
                       validators=[DataRequired()])
    address = TextAreaField('Address',
                            id='customer_address')
    city = StringField('City',
                       id='customer_city')
    state = SelectField('State*',
                        id='customer_states',
                        choices=states_tuples(),
                        validators=[DataRequired()])
    pincode = StringField('Pincode*',
                       id='company_pincode',
                       validators=[DataRequired()])
    email = EmailField('Email Address',
                       id='customer_email',
                       validators=[Email()])
    phone = StringField('Phone Number*',
                        id='customer_phone',
                        validators=[DataRequired(), Length(min=8, max=10)])
    landline = StringField('Land Line',
                        id='customer_landline',
                        validators=[Length(min=8, max=10)])
    regddate = DateField('Regd Date',
                    id='company_regddate')
    regdno = StringField('Regd No*',
                       id='company_regdno',
                       validators=[DataRequired()])
    gstno = StringField('GST No*',
                       id='company_gstno',
                       validators=[DataRequired()])
    panno = StringField('PAN No*',
                       id='company_panno',
                       validators=[DataRequired()])
    tinno = StringField('TIN No*',
                       id='company_tinno',
                       validators=[DataRequired()])
    cinno = StringField('CIN No*',
                       id='company_cinno',
                       validators=[DataRequired()])
    website = TextAreaField('WebSite',
                            id='customer_website')
    rssale = StringField('1 Rs Sale Points',
                       id='company_rssale')
    point = StringField('1 Point Redeem value',
                       id='company_point')

class UserForm(FlaskForm):
    company = SelectField('Company*',
                        id='user_company',
                        choices=company_tuples(),
                        validators=[DataRequired()])
    manager = SelectField('Manager*',
                        id='user_manager',
                        choices=manager_tuples(),
                        validators=[DataRequired()])
    role = SelectField('Role*',
                        id='user_role',
                        choices=roles_tuples(),
                        validators=[DataRequired()])
    name = StringField('Name*',
                       id='users_name',
                       validators=[DataRequired()])
    email = EmailField('Email Address',
                       id='users_email',
                       validators=[Email()])
    # pass and confirm passs need to be added

class ProductForm(FlaskForm):
    name = StringField('Name*',
                       id='product_name',
                       validators=[DataRequired()])
    code = StringField('Product Code*',
                       id='product_code',
                       validators=[DataRequired()])
    brand = SelectField('Brand*',
                        id='product_brand',
                        choices=states_tuples(),
                        validators=[DataRequired()])
    category = SelectField('Category*',
                        id='product_category',
                        choices=states_tuples(),
                        validators=[DataRequired()])
    mrp = FloatField('MRP',
                        id='product_mrp')
    discount = FloatField('Discount',
                        id='product_discount')
    price = FloatField('Price',
                        id='product_price')
    taxrate = FloatField('Tax Rate',
                        id='product_taxrate')
    unit = IntegerField('Unit',
                        id='product_unit')
    rackno = StringField('Rack Number',
                        id='customer_rackno')
    expiry = StringField('Product Expiry',
                        id='product_expiry')
    hsncode = StringField('HSN Code',
                        id='product_hsncode')
    hsnname = StringField('HSN Name',
                        id='product_hsnname')
    cbarcode = StringField('Custom barcode',
                        id='product_cbarcode')
    obarcode = StringField('Original barcode',
                        id='product_obarcode')

class StockForm(FlaskForm):
    pfor = SelectField('Purchased For*',
                        id='stock_pfor',
                        choices=states_tuples(),
                        validators=[DataRequired()])
    product = SelectField('Product*',
                        id='stock_product',
                        choices=states_tuples(),
                        validators=[DataRequired()])
    invoice = SelectField('Invoice No*',
                        id='stock_invoice',
                        choices=states_tuples(),
                        validators=[DataRequired()])
    invoiced = DateField('invoice Date',
                    id='stock_invoiced')
    pfrom = SelectField('Purchased From*',
                        id='stock_pfrom',
                        choices=states_tuples(),
                        validators=[DataRequired()])
    purchasedp = StringField('Purchased Item Price in GST*',
                       id='product_price',
                       validators=[DataRequired()])
    discount = SelectField('Discount*',
                        id='stock_discount',
                        validators=[DataRequired()])
    sprice = SelectField('Sales Price*',
                        id='stock_sprice',
                        validators=[DataRequired()])
    qty = StringField('Quantity',
                        id='stock_qty')
    unit = StringField('Unit',
                        id='stock_unit')
    remarks = TextAreaField('remarks',
                        id='stock_remarks')
