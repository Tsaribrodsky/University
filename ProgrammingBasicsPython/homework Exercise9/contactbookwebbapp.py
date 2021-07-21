from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/')
def mainpage(name):
    - page
    - menu
    - creating, updating, searching and removing
    
   return
"""
HTML code
"""

@app.route('/create')
def create_record():
    if request.method == 'POST':
        name= request.form('name')
        address = request.form('address')
        ....
        - open file and append. 
        pass
    elif: request.etod == 'GET':
        """
HTML
<form action=/create method='post;>
Name, Address, Birthday, Phone number, Email, Profession, Interests
"""
        pass
    else:
        return "Invalid reguest"
    
    
@app.route('/update')
def update_record():
    if request.method == 'POST':
        name= request.form('searchkey')
        - open file for reading and locate the data and get it
        - HTML
        display founded record
        - inpout fiels allowing modification .
        - call /makeupdate
        
        
        pass
    elif: request.etod == 'GET':
        """
HTML

<form action=/update method='post>
<imput type=text name=searchkey>
Name, Address, Birthday, Phone number, Email, Profession, Interests
"""
        pass
    else:
        return "Invalid reguest"
    
 
           '/update/commit'
@app.route('/makeupdate')
def makeupdate_record():
       if request.method == 'POST':
        name= request.form(' ')
        ....
        
        - open file for writing and locate the data and remove it then create new one.
        - HTML
        - confirmation message. 
        
        
        pass
       else:
           return "Invalid request"
        
@app.route('/search')
def search_record():
    pass


@app.route('/remove')
def remove_record():
    pass

##@app.route('/login',methods = ['POST', 'GET'])
##def login():
##   if request.method == 'POST':
#      user = request.form['nm']
 #     user += " POST"
 #     return redirect(url_for('success',name = user))
##   else:
##       return """
##"""

if __name__ == '__main__':
   app.run(port=5010, debug = True)
