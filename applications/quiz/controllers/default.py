# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
#########################################################################

@auth.requires_login()
def index():
    dict1=search()
    form=dict1['form']
    target_div=dict1['target_div']
    print target_div
    rows = db().select(db.category.ALL)
    image = db(db.auth_user.id==auth.user_id).select()
    for im in image:
        im = im
    return locals()

def select_subcategory():
    name = str(request.args[0])
    ##print name
    rows= db(db.main_table.Category==name).select()
    return locals()

def select_set():
    name = str(request.args[1])
    name1 = str(request.args[0])
    rows= db(db.main_table.Sub_Category==name).select()
    return locals()

def select_level():
    name = str(request.args[0])
    name1 = str(request.args[1])
    name2 = str(request.args[2])
    rows = db(db.main_table.Qset==name and db.main_table.Sub_Category==name1).select()
    return locals()

@auth.requires_login()

def question_display():
    cat = str(request.args[3])
    subcat = str(request.args[2])
    st = str(request.args[1])
    lvl = str(request.args[0])
    toshow = int(request.args[4])
    resumeid = (request.args[5])
    rows = db((db.main_table.Qset==st) & (db.main_table.Sub_Category==subcat) & (db.main_table.Category==cat) & (db.main_table.Qlevel==lvl)).select()
    for row in rows:
        queid = row.id
    db.ans1.qidans.default = queid
    db.ans2.qidans.default = queid
    db.ans3.qidans.default = queid
    db.ans4.qidans.default = queid
    db.ans5.qidans.default = queid
    form1 = SQLFORM(db.ans1 , submit_button='LOCK').process()
    if form1.accepted:
        redirect(URL('question_display', args = [lvl,st,subcat,cat,toshow+1,resumeid]))
    form2 = SQLFORM(db.ans2 , submit_button='LOCK').process()
    if form2.accepted:
        redirect(URL('question_display', args = [lvl,st,subcat,cat,toshow+1,resumeid]))
    form3 = SQLFORM(db.ans3 , submit_button='LOCK').process()
    if form3.accepted:
        redirect(URL('question_display', args = [lvl,st,subcat,cat,toshow+1,resumeid]))
    form4 = SQLFORM(db.ans4 , submit_button='LOCK').process()
    if form4.accepted:
        redirect(URL('question_display', args = [lvl,st,subcat,cat,toshow+1,resumeid]))
    form5 = SQLFORM(db.ans5 , submit_button='LOCK').process()
    if form5.accepted:
        redirect(URL('question_display', args = [lvl,st,subcat,cat,1,resumeid]))
    ans = db(db.question.qid==queid).select()
    #print queid
    for an in ans:
        anr = an
    ##print "yo"
    A = db(db.optiona.qida == queid).select()
    for a in A:
        ar = a
    B = db(db.optionb.qidb == queid).select()
    for b in B:
        br = b
    C = db(db.optionc.qidc == queid).select()
    for c in C:
        cr = c
    D = db(db.optiond.qidd == queid).select()
    for d in D:
        dr = d
    ##print "resumeid=",resumeid
    if resumeid != "None":
        #print "Ayush1"
        lines = db(db.your_state.id==resumeid).select()
        for line in lines:
            line = line
    return locals()

def startpage():
    cat = str(request.args[3])
    subcat = str(request.args[2])
    st = str(request.args[1])
    lvl = str(request.args[0])
    rows = db((db.main_table.Qset==st) & (db.main_table.Sub_Category==subcat) & (db.main_table.Category==cat) & (db.main_table.Qlevel==lvl)).select()
    for row in rows:
        queid = row.id
    lines = db((db.your_state.questionsetid==queid) & (db.your_state.yourid==auth.user_id)).select()
    resumeid = None
    for line in lines:
        resumeid = line.id
    #print resumeid
    return locals()

def pause():
    cat = str(request.args[3])
    subcat = str(request.args[2])
    st = str(request.args[1])
    lvl = str(request.args[0])
    rows = db((db.main_table.Qset==st) & (db.main_table.Sub_Category==subcat) & (db.main_table.Category==cat) & (db.main_table.Qlevel==lvl)).select()
    for row in rows:
        queid = row.id

    updt1 = None
    updt2 = None
    updt3 = None
    updt4 = None
    updt5 = None
    rows1 = db((db.ans1.qidans==queid) & (db.ans1.created_by==auth.user_id)).select()
    for row1 in rows1:
        updt1 = row1.Ans1

    rows1 = db((db.ans2.qidans==queid) & (db.ans2.created_by==auth.user_id)).select()
    for row1 in rows1:
        updt2 = row1.Ans2

    rows1 = db((db.ans3.qidans==queid) & (db.ans3.created_by==auth.user_id)).select()
    for row1 in rows1:
        updt3 = row1.Ans3

    rows1 = db((db.ans4.qidans==queid) & (db.ans4.created_by==auth.user_id)).select()
    for row1 in rows1:
        updt4 = row1.Ans4

    rows1 = db((db.ans5.qidans==queid) & (db.ans5.created_by==auth.user_id)).select()
    for row1 in rows1:
        updt5 = row1.Ans5

    db.your_state.insert(questionsetid=queid,marked1=updt1,marked2=updt2,marked3=updt3,marked4=updt4,marked5=updt5)

    return locals()


def marksheet():
    cat = str(request.args[3])
    subcat = str(request.args[2])
    st = str(request.args[1])
    lvl = str(request.args[0])
    rows = db((db.main_table.Qset==st) & (db.main_table.Sub_Category==subcat) & (db.main_table.Category==cat) & (db.main_table.Qlevel==lvl)).select()
    for row in rows:
        queid = row.id

    db.rate.quizid.default = queid
    form = SQLFORM(db.rate).process()
    updt1 = None
    updt2 = None
    updt3 = None
    updt4 = None
    updt5 = None
    rows1 = db((db.ans1.qidans==queid) & (db.ans1.created_by==auth.user_id)).select()
    for row1 in rows1:
        updt1 = row1.Ans1

    rows1 = db((db.ans2.qidans==queid) & (db.ans2.created_by==auth.user_id)).select()
    for row1 in rows1:
        updt2 = row1.Ans2

    rows1 = db((db.ans3.qidans==queid) & (db.ans3.created_by==auth.user_id)).select()
    for row1 in rows1:
        updt3 = row1.Ans3

    rows1 = db((db.ans4.qidans==queid) & (db.ans4.created_by==auth.user_id)).select()
    for row1 in rows1:
        updt4 = row1.Ans4

    rows1 = db((db.ans5.qidans==queid) & (db.ans5.created_by==auth.user_id)).select()
    for row1 in rows1:
        updt5 = row1.Ans5

    db.your_state.insert(questionsetid=queid,marked1=updt1,marked2=updt2,marked3=updt3,marked4=updt4,marked5=updt5)

    thisid = queid
    lines = db((db.your_state.questionsetid==thisid) & (db.your_state.yourid==auth.user_id)).select()
    answers = db(db.cans.qidcans==thisid).select()
    score = 0
    for line in lines:
        line = line

    for ans in answers:
        ans = ans
       

    if ans.cans1==line.marked1:
        score1 = 10
        score += 10
    elif ans.cans1=="None":
        score1 = 0
        score = score
    else:
        score1 = -2
        score -= 2

    if ans.cans2==line.marked2:
        score2 = 10
        score += 10
    
    elif ans.cans2=="None":
        score2 = 0
        score = score
        
    else:
        score2 = -2
        score -= 2

    if ans.cans3==line.marked3:
        score3 = 10
        score += 10
        
    elif ans.cans3=="None":
        score3 = 0
        score = score 
        
    else:
        score3 = -2
        score -= 2

    if ans.cans4==line.marked4:
        score4 = 10
        score += 10
        
    elif ans.cans4=="None":
        score4 = 0
        score = score
    
    else:
        score4 = -2
        score -= 2

    if ans.cans5==line.marked5:
        score5 = 10
        score += 10
        
    elif ans.cans5=="None":
        score5 = 0
        score = score 
        
    else:
        score5 = -2
        score -= 2
    thisusr = None
    thisusr = db(db.score.created_by == db.auth_user(auth.user_id).id).select()

    print auth.user_id,db.auth_user(auth.user_id).id
    if thisusr is None:
        print "none it"
        db.score.insert(created_by=db.auth_user(auth.user_id).id,score=score)
    else:
        print "yes 1"
        db(db.score.created_by==auth.user_id).update(score=score)
    return locals()

def suggestquestion():
    form = SQLFORM(db.suggest_question, _class='form-horizontal')
    return locals()

def topscorer():
    list = db().select(db.score.ALL,orderby=~db.score.score)
    return locals()
def user():
    return dict(form=auth())

def search():
    return dict(form=FORM(INPUT(_id='keyword',_name='keyword',_onkeyup="ajax('callback', ['keyword'], 'target');")),target_div=DIV(_id='target'))

def callback():
    query = db.category.Category.contains(request.vars.keyword)
    pages = db(query).select(orderby=db.category.Category)
    links = [A(p.Category, _href=URL('select_subcategory',args=p.Category)) for p in pages]
    return UL(*links)

def edit_profile():
    rows = db.auth_user(request.args(0,cast=int))
    form = SQLFORM(db.auth_user,rows).process()
    if form.process().accepted:
        response.flash = 'record updated'
    return locals()

def ratings():
    lines = db(db.rate).select()
    print lines
    return locals()

@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()
