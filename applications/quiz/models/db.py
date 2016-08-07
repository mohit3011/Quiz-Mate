# -*- coding: utf-8 -*-

#########################################################################
## This scaffolding model makes your app work on Google App Engine too
## File is released under public domain and you can use without limitations
#########################################################################

## if SSL/HTTPS is properly configured and you want all HTTP requests to
## be redirected to HTTPS, uncomment the line below:
# request.requires_https()

## app configuration made easy. Look inside private/appconfig.ini
from gluon.contrib.appconfig import AppConfig
## once in production, remove reload=True to gain full speed
myconf = AppConfig(reload=True)


if not request.env.web2py_runtime_gae:
    ## if NOT running on Google App Engine use SQLite or other DB
    db = DAL(myconf.take('db.uri'), pool_size=myconf.take('db.pool_size', cast=int), check_reserved=['all'])
else:
    ## connect to Google BigTable (optional 'google:datastore://namespace')
    db = DAL('google:datastore+ndb')
    ## store sessions and tickets there
    session.connect(request, response, db=db)
    ## or store session in Memcache, Redis, etc.
    ## from gluon.contrib.memdb import MEMDB
    ## from google.appengine.api.memcache import Client
    ## session.connect(request, response, db = MEMDB(Client()))

## by default give a view/generic.extension to all actions from localhost
## none otherwise. a pattern can be 'controller/function.extension'
response.generic_patterns = ['*'] if request.is_local else []
## choose a style for forms
response.formstyle = myconf.take('forms.formstyle')  # or 'bootstrap3_stacked' or 'bootstrap2' or other
response.form_label_separator = myconf.take('forms.separator')


## (optional) optimize handling of static files
# response.optimize_css = 'concat,minify,inline'
# response.optimize_js = 'concat,minify,inline'
## (optional) static assets folder versioning
# response.static_version = '0.0.0'
#########################################################################
## Here is sample code if you need for
## - email capabilities
## - authentication (registration, login, logout, ... )
## - authorization (role based authorization)
## - services (xml, csv, json, xmlrpc, jsonrpc, amf, rss)
## - old style crud actions
## (more options discussed in gluon/tools.py)
#########################################################################

from gluon.tools import Auth, Service, PluginManager

auth = Auth(db)
service = Service()
plugins = PluginManager()
auth.settings.extra_fields['auth_user']= [
	Field('Gender', requires=IS_IN_SET(['Male','Female','Other'])),
	Field('Image', 'upload'),
	Field('DOB', 'date'),
    Field('Profession',requires=IS_IN_SET(['Goverment Job','House-wife','Student','Private-Job','Business'])),
    Field('Description', 'text'),
    Field('Interest','string')]
## create all tables needed by auth if not custom tables
auth.define_tables(username=False, signature=False)

## configure email
mail = auth.settings.mailer
mail.settings.server = 'logging' if request.is_local else myconf.take('smtp.server')
mail.settings.sender = myconf.take('smtp.sender')
mail.settings.login = myconf.take('smtp.login')

## configure auth policy
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.settings.reset_password_requires_verification = True
db.auth_user.password.requires = IS_STRONG(min=8, upper=1, special=2)
#########################################################################
## Define your tables below (or better in another model file) for example
##
## >>> db.define_table('mytable',Field('myfield','string'))
##
## Fields can be 'string','text','password','integer','double','boolean'
##       'date','time','datetime','blob','upload', 'reference TABLENAME'
## There is an implicit 'id integer autoincrement' field
## Consult manual for more options, validators, etc.
##
## More API examples for controllers:
##
## >>> db.mytable.insert(myfield='value')
## >>> rows=db(db.mytable.myfield=='value').select(db.mytable.ALL)
## >>> for row in rows: print row.id, row.myfield
#########################################################################

## after defining tables, uncomment below to enable auditing
# auth.enable_record_versioning(db)
db.define_table('main_table',
                Field('Category','string'),
                Field('Sub_Category','string'),
                Field('Qset','string'),
                Field('Qlevel','string'))

db.define_table('category',
                Field('Category'))

db.define_table('question',
                Field('qid','reference main_table'),
                Field('Q1','text'),
                Field('Q2','text'),
                Field('Q3','text'),
                Field('Q4','text'),
                Field('Q5','text'))

db.define_table('optiona',
                Field('qida','reference main_table'),
                Field('A1','string'),
                Field('A2','string'),
                Field('A3','string'),
                Field('A4','string'),
                Field('A5','string'))

db.define_table('optionb',
                Field('qidb','reference main_table'),
                Field('B1','string'),
                Field('B2','string'),
                Field('B3','string'),
                Field('B4','string'),
                Field('B5','string'))

db.define_table('optionc',
                Field('qidc','reference main_table'),
                Field('C1','string'),
                Field('C2','string'),
                Field('C3','string'),
                Field('C4','string'),
                Field('C5','string'))

db.define_table('optiond',
                Field('qidd','reference main_table'),
                Field('D1','string'),
                Field('D2','string'),
                Field('D3','string'),
                Field('D4','string'),
                Field('D5','string'))

db.define_table('cans',
                Field('qidcans','reference main_table'),
                Field('cans1','string'),
                Field('cans2','string'),
                Field('cans3','string'),
                Field('cans4','string'),
                Field('cans5','string'))



db.define_table('ans1',
                Field('qidans','reference main_table',writable=False,readable=False),
                Field('Ans1','list:string',label=''),
                auth.signature)
db.ans1.Ans1.requires = IS_IN_SET(('A', 'B','C','D'))
db.ans1.Ans1.widget = SQLFORM.widgets.radio.widget
db.define_table('ans2',
                Field('qidans','reference main_table',writable=False,readable=False),
                Field('Ans2','list:string',label=''),
                auth.signature)
db.ans2.Ans2.requires = IS_IN_SET(('A', 'B','C','D'))
db.ans2.Ans2.widget = SQLFORM.widgets.radio.widget
db.define_table('ans3',
                Field('qidans','reference main_table',writable=False,readable=False),
                Field('Ans3','list:string',label=''),
                auth.signature)
db.ans3.Ans3.requires = IS_IN_SET(('A', 'B','C','D'))
db.ans3.Ans3.widget = SQLFORM.widgets.radio.widget
db.define_table('ans4',
                Field('qidans','reference main_table',writable=False,readable=False),
                Field('Ans4','list:string',label=''),
                auth.signature)
db.ans4.Ans4.requires = IS_IN_SET(('A', 'B','C','D'))
db.ans4.Ans4.widget = SQLFORM.widgets.radio.widget
db.define_table('ans5',
                Field('qidans','reference main_table',writable=False,readable=False),
                Field('Ans5','list:string',label=''),
                auth.signature)
db.ans5.Ans5.requires = IS_IN_SET(('A', 'B','C','D'))
db.ans5.Ans5.widget = SQLFORM.widgets.radio.widget



db.define_table('your_state',
                Field('yourid','reference auth_user', default=auth.user_id),
                Field('questionsetid','reference main_table'),
                Field('marked1'),
                Field('marked2'),
                Field('marked3'),
                Field('marked4'),
                Field('marked5'))

db.define_table('score',
                Field('score','integer'),
                auth.signature)

db.define_table('suggest_question',
                Field('category','string'),
                Field('subcategory','string'),
                Field('question','text'),
                Field('optionA','text'),
                Field('optionB','text'),
                Field('optionC','text'),
                Field('optionD','text'),
                auth.signature)

db.define_table('rate',
                Field('quizid', 'reference main_table' , writable=False , readable=False),
                Field('Rate_Quiz', 'integer' , requires=IS_IN_SET(range(1,6))),
               auth.signature)
