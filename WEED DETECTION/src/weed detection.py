from flask import *
from src.dbconnection import *
from src.newcnn import predictfn
app=Flask(__name__)
app.secret_key="hgvg"





import functools

def login_required(func):
    @functools.wraps(func)
    def secure_function():
        if "lid" not in session:
            return render_template('index.html')
        return func()

    return secure_function


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/l')
@app.route('/')
def log():
    return render_template("user/registrationindex.html")

@app.route('/l')
def login():
    return render_template("index.html")

@app.route('/login_post',methods=[ 'post'])
def login_post():
    uname=request.form['textfield']
    password=request.form['textfield2']
    qry="SELECT * FROM `login` WHERE  username=%s AND password=%s"
    val=(uname,password)
    res=selectone(qry,val)
    if res is None:
        return '''<script>alert("invalid");window.location="/"</script>'''
    elif res['type']=='admin':
        session['lid']=res['lid']
        return '''<script>alert("WELCOME");window.location="/home"</script>'''
    elif res['type']=='Expert':
        session['lid'] = res['lid']
        return '''<script>alert("WELCOME");window.location="/expert_home"</script>'''
    elif res[ 'type']== 'user':
        session['lid'] = res['lid']
        return '''<script>alert("WELCOME");window.location="user_home_page"</script>'''
    else:
        return '''<script>alert("invalid");window.location="/"</script>'''





@app.route('/add_crops',methods=['post'])
@login_required
def add_crops():
    return render_template("Admin/add crops.html")
@app.route('/add_crops1',methods=['post'])
@login_required
def add_crops1():
    cropname=request.form['textfield']
    details=request.form['textfield2']
    qry1="INSERT INTO `crop` VALUES (NULL,%s,%s,CURDATE())"
    val1=(cropname,details)
    iud(qry1,val1)
    return  '''<script>alert("Added");window.location="/manage_crop_details"</script>'''
@app.route('/delete_crop')
@login_required
def delete_crop():
    id=request.args.get('id')

    qry="DELETE FROM `crop` WHERE `cid`=%s"
    iud(qry,id)
    return '''<script>alert("DELETED");window.location="/manage_crop_details"</script>'''



@app.route('/add_expert',methods=['post'])
@login_required
def add_expert():
    return render_template("Admin/add expert.html")

@app.route('/add_expert1',methods=['post'])
@login_required
def add_expert1():
    fname = request.form['textfield']
    lname = request.form['textfield2']
    place = request.form['textfield3']
    post = request.form['textfield4']
    pin=request.form[ 'textfield5']
    phone=request.form[ 'textfield6']
    email=request.form[ 'textfield7']
    uname=request.form[ 'textfield8']
    password=request.form[ 'textfield9']
    qry="INSERT INTO `login` VALUES(NULL,%s,%s,'Expert')"
    val=(uname,password)
    id=iud(qry,val)
    qry1="INSERT INTO `expert` VALUES(NULL,%s,%s,%s,%s,%s,%s,%s,%s)"
    val1=(str(id),fname,lname,place,post,pin,phone,email)
    iud(qry1,val1)
    return '''<script>alert("Added");window.location="/manage_expert"</script>'''


@app.route('/edit_expert')
@login_required
def edit_expert():
    id=request.args.get('id')
    session['EE_id']=id
    qry="select * from expert where `lid`=%s"
    res=selectone(qry,id)

    return render_template("Admin/edit_expert.html",val=res)

@app.route('/edit_expert1',methods=['post'])
@login_required
def edit_expert1():
    fname = request.form['textfield']
    lname = request.form['textfield2']
    place = request.form['textfield3']
    post = request.form['textfield4']
    pin=request.form[ 'textfield5']
    phone=request.form[ 'textfield6']
    email=request.form[ 'textfield7']

    qry1="UPDATE `expert` SET `fname`=%s ,`lname`=%s,`place`=%s, `post`=%s,`pin`=%s,`phone`=%s,`email`=%s where `lid`=%s"
    val1=(fname,lname,place,post,pin,phone,email,session['EE_id'])
    iud(qry1,val1)
    return '''<script>alert("Added");window.location="/manage_expert"</script>'''

@app.route('/delete_expert')
@login_required
def delete_expert():
    id=request.args.get('id')
    qry="DELETE FROM `expert` WHERE `lid`=%s"
    iud(qry,id)
    qry1="DELETE FROM `login` WHERE `lid`=%s"
    iud(qry1,id)

    return '''<script>alert("deleted");window.location="/manage_expert"</script>'''


@app.route('/add_notifications',methods=['post'])
@login_required
def add_notifications():
    return render_template("Admin/add notifications.html")
@app.route('/add_notifications1',methods=[ 'post'])
@login_required
def add_notifications1():
    notification=request.form['textfield']
    qry1="INSERT INTO `notification` VALUES (NULL,%s,CURDATE())"
    val1=(notification)
    iud(qry1,val1)
    return '''<script>alert("Added");window.location="/manage_notifications"</script>'''

@app.route('/delete_notification')
@login_required
def delete_notificaton():
    id=request.args.get('id')
    qry="DELETE FROM `notification` WHERE `id`=%s"
    iud(qry,id)

    return '''<script>alert("deleted");window.location="/manage_notifications"</script>'''




@app.route('/chat_with_farmer')
@login_required
def chat_with_farmer():
    qry="select * from  user"
    res=selectall(qry)
    return render_template("Expert/chat with farmer.html",val=res)

@app.route("/chat3")
def chatsp1():
    pid=request.args.get('uid')
    print(pid,"==============================")
    session['ppid']=pid
    qry="SELECT * FROM `user` WHERE `lid`=%s"
    res=selectone(qry,pid)
    print(res)

    qry = "SELECT * FROM `chat` WHERE `from_id`=%s AND `to_id`=%s OR `from_id`=%s AND `to_id`=%s "
    val = (session['lid'], session['ppid'], session['ppid'], session['lid'])
    res1 = selectall2(qry, val)

    print(res)

    fname = res['fname']
    lname = res['lname']
    return render_template("Expert/chat3.html", data=res1, fname=fname, lname=lname, fr=session['lid'])


@app.route('/send1', methods=['post'])
def sendchat1():
    message = request.form['textarea']
    to_id = session['ppid']
    from_id = session['lid']
    qry = "insert into chat values(null,%s,%s,%s,CURDATE(),curtime())"
    val = (from_id, to_id, message)
    iud(qry, val)
    return redirect("chatss1")


@app.route("/chatss1")
def chatss1():
    pid = session['ppid']
    qry = "SELECT * FROM `user` WHERE `lid`=%s"
    res = selectone(qry, pid)
    qry = "SELECT * FROM `chat` WHERE `from_id`=%s AND `to_id`=%s OR `from_id`=%s AND `to_id`=%s "
    val = (session['lid'], session['ppid'], session['ppid'], session['lid'])
    res1 = selectall2(qry, val)
    fname = res['fname']
    lname = res['lname']
    return render_template("Expert/chat3.html", data=res1, fname=fname, lname=lname, fr=session['lid'])


@app.route('/home')
@login_required
def home():
    return render_template("adminindex.html")
@app.route('/manage_crop_details')
@login_required
def manage_crop_details():
    qry = "select * from crop"
    res = selectall(qry)
    return render_template("Admin/manage crop details.html",val=res)


@app.route('/manage_expert')
@login_required
def manage_expert():
    qry="select * from expert"
    res=selectall(qry)
    return render_template("Admin/manage expert.html",val=res)


@app.route('/add_gov_policy',methods=['post'])
@login_required
def add_gov_policy():
    return render_template("Admin/add gov policy.html")


@app.route('/add_gov_policy1',methods=['post'])
@login_required
def add_gov_policy1():
    policy=request.form['textfield']
    details=request.form['textfield2']
    qry1="INSERT INTO `gov_policy` VALUES (NULL,%s,%s,CURDATE())"
    val1=(policy,details,)
    iud(qry1,val1)
    return '''<script>alert("Added");window.location="manage_gov_policies"</script>'''
@app.route('/delete_gov_policy')
@login_required
def delete_gov_policy():
    id = request.args.get('id')
    qry = "DELETE FROM `gov_policy` WHERE`g_id`=%s"
    iud(qry, id)
    return '''<script>alert("DELETED");window.location="manage_gov_policies"</script>'''


@app.route('/manage_gov_policies')
@login_required
def manage_gov_policies():
    qry="select *from gov_policy"
    res=selectall(qry)
    return render_template("Admin/manage gov policies.html",val=res)


@app.route('/manage_notifications')
@login_required
def manage_notifications():
    qry="select *from notification"
    res=selectall(qry)
    return render_template("Admin/manage notification.html",val=res)

@app.route('/send_reply')
@login_required
def send_reply():
    id=request.args.get('id')
    session['cid']=id
    return render_template("Admin/send reply.html")

@app.route('/send_reply1',methods=['post'])
@login_required
def send_reply1():
    rply=request.form['textfield']
    q="UPDATE `complaint` SET `reply`=%s WHERE `cid`=%s"
    v=(rply,session['cid'])
    iud(q,v)
    return '''<script>alert("sent");window.location="view_complaints"</script>'''


@app.route('/view_complaints')
@login_required
def view_complaints():
    qry="SELECT `user`.`fname`,`lname` ,`complaint`.* FROM `complaint` JOIN `user` ON `user`.`lid`=`complaint`.`lid`"
    res=selectall(qry)
    return render_template("Admin/view complaints.html",val=res)

@app.route('/view_farmers')
@login_required
def view_farmers():
    qry = "select * from user"
    res = selectall(qry)
    return render_template("Admin/view farmers.html",val=res)
@app.route('/view_feedback')
@login_required
def view_feedback():
    qry="SELECT * FROM `feedback` JOIN `user` ON `user`.lid =feedback.uid"
    res=selectall(qry)
    return render_template("Admin/view feedback.html",val=res)

@app.route('/add_farming_method',methods=['post'])
@login_required
def add_farming_method():
    return render_template("Expert/add farming method.html")

@app.route('/add_farming_method1',methods=['post'])
@login_required
def add_farming_method1():
    fmethod=request.form['textfield']
    details=request.form['textfield2']
    qry1="INSERT INTO `farming_method`VALUES (NULL,%s,%s,%s,CURDATE())"
    val1=(session['lid'],fmethod,details)
    iud(qry1,val1)
    return '''<script>alert("Added");window.location="manage farming_method"</script>'''
@app.route('/delete_farming_method')
@login_required
def delete_farming_method():
    fid = request.args.get('id')
    qry = "DELETE FROM `farming_method` WHERE `fid`=%s"
    iud(qry, fid)
    return '''<script>alert("DELETED");window.location="manage_farming_method"</script>'''


@app.route('/add_fertilization',methods=['post'])
@login_required
def add_fertilization():
    return render_template("Expert/add fertilization.html")

@app.route('/add_fertilization1',methods=['post'])
@login_required
def add_fertilization1():
    name=request.form['textfield']
    details=request.form['textfield2']
    qry1="INSERT INTO`fertilization`VALUES(NULL,%s,%s)"
    val1=(name,details)
    iud(qry1,val1)
    return '''<script>alert("Added");window.location="manage_fertilization_details"</script>'''

@app.route('/delete_fertilization')
@login_required
def delete_fertilization():
    fid = request.args.get('id')
    qry = "DELETE FROM `fertilization`WHERE `fid`=%s"
    iud(qry, fid)
    return '''<script>alert("DELETED");window.location="manage_fertilization_details"</script>'''
@app.route('/expert_home')
@login_required
def expert_home():
    return render_template("Expert/expert home.html")



@app.route('/manage_farming_method')
@login_required
def  manage_farming_method():
    qry = "select *from farming_method"
    res = selectall(qry)
    # return render_template("Expert/manage fertilization details.html",val=res)
    return render_template("Expert/manage farming method.html",val=res)


@app.route('/manage_fertilization_details')
@login_required
def manage_fertilization_details():
    qry = "select *from fertilization"
    res = selectall(qry)

    return render_template("Expert/manage fertilization details.html",val=res)



"=========================chat with expet============================="


@app.route('/chat_with_expert')
@login_required
def chat_with_expert():
    qry = "SELECT * FROM `expert"
    res = selectall(qry)
    return render_template("user/chat with expert.html", val=res)

@app.route("/chat2")
def chatsp():
    pid=request.args.get('uid')
    print(pid,"==============================")
    session['pid']=pid
    qry="SELECT * FROM  expert  WHERE `lid`=%s"
    res=selectone(qry,pid)


    print(res)


    qry="SELECT * FROM `chat` WHERE `from_id`=%s AND `to_id`=%s OR `from_id`=%s AND `to_id`=%s "
    val=(session['lid'],session['pid'],session['pid'],session['lid'])
    res1=selectall2(qry,val)

    print(res)

    fname=res['fname']
    lname=res['lname']
    return render_template("chat2.html",data=res1,fname=fname,lname=lname,fr=session['lid'])



@app.route('/send',methods=['post'])
def sendchat():
    message=request.form['textarea']
    to_id = session['pid']
    from_id = session['lid']
    qry="insert into chat values(null,%s,%s,%s,CURDATE(),curtime())"
    val=(from_id,to_id,message)
    iud(qry,val)
    return redirect("chatss")
@app.route("/chatss")
def chatss():
    pid=session['pid']
    qry="SELECT * FROM `expert` WHERE `lid`=%s"
    res=selectone(qry,pid)
    qry="SELECT * FROM `chat` WHERE `from_id`=%s AND `to_id`=%s OR `from_id`=%s AND `to_id`=%s "
    val=(session['lid'],session['pid'],session['pid'],session['lid'])
    res1=selectall2(qry,val)
    fname=res['fname']
    lname=res['lname']
    return render_template("chat2.html",data=res1,fname=fname,lname=lname,fr=session['lid'])


"====================================================================================================="




@app.route('/registration')
def registration():
    return render_template("user/registration.html")
@app.route('/registration2',methods=['post'])
def registration2():
    fname=request.form['textfield']
    lname=request.form['textfield2']
    place=request.form['textfield4']
    post=request.form['textfield5']
    pin=request.form['textfield6']
    phoneno=request.form['textfield7']
    email=request.form['textfield8']
    uname = request.form['textfield9']
    password = request.form['textfield10']
    qry="INSERT INTO `login`VALUES (NULL ,%s,%s,'user')"
    val=(uname,password)
    id=iud(qry,val)
    qry1="INSERT INTO `user` VALUES (NULL,%s,%s,%s,%s,%s,%s,%s,%s)"
    val1=(str(id),fname,lname,place,post,pin,phoneno,email)
    val1=iud(qry1,val1)
    return '''<script>alert("SUCCESSFULLY REGISTERED");window.location="/"</script>'''


# @app.route('/ send_complaints')
# def send_complaints():
#     return render_template("user/send complaint.html")
@app.route('/send_feedback')
@login_required
def send_feedback():
    return render_template("user/send feedback.html")
@app.route('/send_complaints')
@login_required
def send_complaints():
    return render_template("user/send complaint.html")

@app.route('/send_feedback2',methods=['post'])
@login_required
def send_feedback2():
    feedback=request.form['textfield']
    qry="INSERT INTO `feedback` VALUES (NULL,%s,%s,'pending',CURDATE())"
    val=(session['lid'],feedback)
    iud(qry,val)
    return '''<script>alert("send successfull");window.location="/"</script>'''

@app.route('/user_home_page')
@login_required
def user_home_page():
    return render_template("user/user home page.html")
@app.route('/view_crop_details')
@login_required
def view_crop_details():
    qry="SELECT *FROM `crop`"
    res=selectall(qry)
    return render_template("user/view crop details.html",val=res)
@app.route('/view_farming_method')
@login_required
def view_farming_method():
    qry = "SELECT *FROM `farming_method`JOIN `expert` ON `expert`.`lid`=`farming_method`.`lid`"

    res = selectall(qry)
    return render_template("user/view farming method.html",val=res)
@app.route('/view_fertilization_details')
@login_required
def view_fertilization_details():
    qry="SELECT *FROM `fertilization`"
    res=selectall(qry)
    return render_template("user/view fertilization details.html",val=res)
@app.route('/view_government_policies')
@login_required
def view_government_policies():
    qry="SELECT *FROM `gov_policy`"
    res=selectall(qry)

    return render_template("user/view governent policies.html",val=res)
@app.route('/view_notification')
@login_required
def view_notification():
    qry="SELECT * FROM `notification`"
    res=selectall(qry)
    return render_template("user/view notification.html",val=res)

@app.route('/view_reply')
@login_required
def view_reply():
    q="SELECT * FROM `complaint` WHERE `lid`=%s"
    res=selectall2(q,session['lid'])
    return render_template("user/view reply.html",data=res)

@app.route('/send_comp',methods=['post'])
@login_required
def send_comp():
    return render_template("user/send complaint.html")

@app.route('/send_comp2',methods=['post'])
@login_required
def send_comp2():
    complaint=request.form['textfield']
    qry="INSERT INTO `complaint` VALUES(NULL,%s,%s,'pending',CURDATE())"
    val=(session['lid'],complaint)
    iud(qry,val)
    return '''<script>alert("send succesfull");window.location="/view_reply"</script>'''



@app.route('/editcrops',methods=['post','get'])
@login_required
def editcrops():
    id=request.args.get('id')
    session['cropid']=id
    qry="select * from crop where cid=%s"
    res=selectone(qry,id)
    return render_template("Admin/editcrops.html",val=res)


@app.route('/editcrops1',methods=['post','get'])
@login_required
def editcrops1():
    crop=request.form['textfield']
    details=request.form['textfield2']
    qry="UPDATE `crop` SET `crops`=%s,`details`=%s WHERE `cid`=%s"
    val=(crop,details,session['cropid'])
    iud(qry,val)
    return '''<script>alert("updated");window.location='/manage_crop_details#about'</script>'''






@app.route('/editpolicy',methods=['post','get'])
@login_required
def editpolicy():
    id=request.args.get('id')
    session['policyid']=id
    qry="select * from gov_policy where g_id=%s"
    res=selectone(qry,id)
    return render_template("Admin/editgovpolicy.html",val=res)




@app.route('/editpolicy1',methods=['post','get'])
@login_required
def editpolicy1():
    policy=request.form['textfield']
    desc=request.form['textfield2']
    date=request.form['textfield3']
    qry="UPDATE `gov_policy` SET `policy`=%s,`details`=%s,`date`=%s WHERE `g_id`=%s"
    val=(policy,desc,date,session['policyid'])
    iud(qry,val)
    return '''<script>alert("updated");window.location='/manage_gov_policies#about'</script>'''

@app.route('/editnotification',methods=['post','get'])
@login_required
def editnotification():
    id=request.args.get('id')
    session['notid']=id
    qry="select * from notification where id=%s"
    res=selectone(qry,id)
    return render_template("Admin/editnotifications.html",val=res)

@app.route('/editnotification1',methods=['post','get'])
@login_required
def editnotification1():
    notification=request.form['textfield']

    qry="UPDATE`notification` SET `notification`=%s WHERE `id`=%s"
    val=(notification,session['notid'])
    iud(qry,val)
    return '''<script>alert("updated");window.location='/manage_notifications#about'</script>'''
@app.route('/editfarmingmethod',methods=['post','get'])
@login_required
def editfarmingmethod():
    id=request.args.get('id')
    session['fid']=id
    qry = "select * from farming_method where fid=%s"
    res=selectone(qry,id)
    return render_template("Expert/editfarming method.html", val=res)

@app.route('/editfarmingmethod1',methods=['post','get'])
@login_required
def editfarmingmethod1():
    fmethod=request.form['textfield']
    details=request.form['textfield2']
    qry="UPDATE `farming_method` SET `fmethod`=%s,`details`=%s WHERE `fid`=%s"
    val=(fmethod,details,session['fid'])
    iud(qry,val)
    return'''<script>alert ("updated");window.location='/manage_farming_method#about'</script>'''

@app.route('/editfertilization',methods=['post','get'])
@login_required
def editfertilization():
    id=request.args.get('id')
    session['fid']=id
    qry="SELECT *FROM fertilization  WHERE fid=%s"
    res=selectone(qry,id)
    return render_template("Expert/editfertilization.html",val=res)
@app.route('/editfertilization1',methods=['post','get'])
@login_required
def editfertilization1():
    name=request.form['textfield']
    details=request.form['textfield2']
    qry="UPDATE `fertilization` SET `name`=%s,`details`=%s WHERE `fid`=%s"
    val=(name,details,session['fid'])
    iud(qry,val)
    return'''<script>alert("updated");window.location='/manage_fertilization_details#about'</script>'''


@app.route('/predict',methods=['post','get'])
def predict():
    if request.method=="POST":
        img=request.files['file']
        img.save(r"C:\Users\hisana\PycharmProjects\weed detection\src\static\a.jpg")
        res = predictfn("static/a.jpg")
        print(res,"eeeeeeee")
        if res[0]==1:
            return render_template("user/PREDICT.html",data="Weed Detected")
        else:
            return render_template("user/PREDICT.html",data="Crop Detected")


    else:
        return render_template("user/PREDICT.html",data="")


app.run(debug=True)