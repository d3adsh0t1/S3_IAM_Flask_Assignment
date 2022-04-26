import os
from flask import Flask, render_template, url_for,redirect,request
from bucket import BucketAPI
from iam import Iam
app = Flask(__name__)

@app.route('/') 
def root():
    return render_template('index.html')

@app.route('/bucket') 
def bucket():
    list_buckets = BucketAPI.list_Bucket()
    # print(list_buckets)
    return render_template('bucket.html',Bucket=list_buckets)

@app.route('/bucket/create' , methods=['GET','POST'])
def CreateBucket():
    
    if request.method == 'POST':
        Name = request.form['Name']
        Region = request.form['Region']
    
        BucketAPI.create_Bucket(Name,Region)
        return redirect(url_for('bucket'))

    else:
        return render_template('createBucket.html') 


@app.route('/bucket/delete/<val>')
def RemoveBucket(val):
    BucketAPI.remove_Bucket(val)
    return redirect(url_for('bucket'))

@app.route('/iam')
def iam():
    user_list = Iam.list_Users()
    # print(user_list)
    return render_template('iam.html',List_Users=user_list)


def getPolicyList():
    policy_list = Iam.list_Policy()['Policies']
    allowed = ['S3','IAM','EC2']
    allowed_policies = []
    print(policy_list[0]['PolicyName'])
    for i in range(len(policy_list)):
        for ele in allowed:
            if policy_list[i]['PolicyName'].find(ele) != -1:
                allowed_policies.append(policy_list[i])

    return allowed_policies


@app.route('/iam/create',methods=['GET','POST'])
def CreateUser():
    
    if request.method == 'POST':
        
        uName = request.form['name']
        gName = request.form['group']
        Iam.create_User(uName,gName)
        return redirect(url_for('iam'))

    else:
        group_list = Iam.list_Groups()['Groups']
        try:
            return render_template('createUser.html',ListGroup=group_list)
        except:
            return redirect(url_for('CreateGroup'))


@app.route('/iam/edit' , methods=['GET','POST'])
def edit_User():
    if request.method == 'POST':
        Oldname = request.form['name']
        Newname = request.form['newName']
        Iam.edit_User(Oldname,Newname)
        return redirect(url_for('iam'))
    else:
        list_users = Iam.list_Users()['Users']
        print(list_users)
        for item in list_users:
            if 'khawslabuser61@nuvelabs.com' in item['UserName']:
                list_users.remove(item)
        return render_template('EditUser.html',Users=list_users)

@app.route('/iam/delete/<val>')
def RemoveUser(val):
    if val != 'khawslabuser61@nuvelabs.com':
        Iam.delete_User(val)
    return redirect(url_for('iam'))


@app.route('/iam/groups')
def group():
    group_list = Iam.list_Groups()['Groups']
    return render_template('group.html',List_Group=group_list)

@app.route('/iam/groups/create' ,methods=['GET','POST'])
def CreateGroup():

    if request.method == 'POST':
        Gname = request.form['group']
        pName = request.form.getlist('policy')
        Iam.create_Group(Gname,pName)
        return redirect(url_for('iam'))
    
    else:
        # ListPolicy = [i['PolicyName'] for i in getPolicyList()]
        return render_template('createGroup.html',ListPolicy=getPolicyList())

@app.route('/iam/groups/edit',methods=['GET','POST'])
def EditGroup():
    if request.method == 'POST':
        Oldname = request.form['name']
        Newname = request.form['newName']
        Iam.edit_Group(Oldname,Newname)
        return redirect(url_for('group'))
    else:
        list_group = Iam.list_Groups()['Groups']
        for item in list_group:
            if 'NL_DND_aws_full_access' in item['GroupName']:
                list_group.remove(item)
        return render_template('EditGroup.html',Groups=list_group)

@app.route('/iam/groups/delete/<val>')
def RemoveGroup(val):
    if val != 'NL_DND_aws_full_access':
        Iam.remove_Group(val)
    
    return redirect(url_for('group'))

@app.route("/iam/policy")
def policy():
    return render_template('policy.html', AllP=getPolicyList())

@app.route("/test" ,methods=['GET','POST'])
def test():
    if request.method == 'POST':
        arr = request.form.getlist('check')
        # arr.append(request.form.getlist('check'))
        print(arr)
        return 'Done'
    return render_template('test.html')

if __name__== '__main__':
    port = int(os.environ.get('PORT',5000))
    app.run(debug=True,host='0.0.0.0', port=port)