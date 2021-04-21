from flask import Flask
app = Flask(__name__)

#App decorator used to link a route to a function in this case, hello world is routed to /
#app.add_url_rule(‘/’, ‘hello’, hello_world) <- Manually bind url to function
@app.route('/<name>')
def hello_world(name):
   return 'Hello World ' + name


@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

#If theres a user in the request it is redirected to succes funtion
#This functions allows post and get methods
@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      #getting the value of a form from a post request
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
       #args is dictionary object containing a list of pairs of form parameter
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))

#The url_for() function accepts the name of a function as first argument, and one or more keyword arguments
#redirect(url_for('hello_guest',guest = name)) <- redirects to the function hello_guest
if __name__ == '__main__':
   app.run(debug=True)