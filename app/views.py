from flask import render_template, jsonify, request
from app import app
from app.models.user import User

"""Views defines routes to be called by the client. These rotutes return json data to be consumed by a client. For storing the data 
	during the life time of the application, I am using a super global current user to store an instance of the user class objet

	This module manages communication between the flask server and the Graphic user interface
"""
current_user = ""


@app.route('/')
def index():
	return render_template("index.html")

@app.route('/dashboard')
def dashboard():
	return render_template("dashboard.html")

@app.route('/api/register',methods=['POST'])
def register():
	"""Registrtaion route, it accepts first_name,last_name,email and password from a user form and instatiates a user object which is 
	later assigned to the global variable current_user"""
	first_name=request.form['first_name']
	last_name=request.form['last_name']
	email=request.form['email']
	password=request.form['password']
	global current_user
	current_user= User(first_name,last_name,email,password)
	return jsonify({'status':"success","message":"User registration successful","name":current_user.name,"email":current_user.email})

@app.route("/api/login",methods=['POST'])
def login():
	"""Login route accepts email and password from a form and compares it with the ones set in the User class by passing both credentials as arguments
	to the login method"""
	email=request.form['email']
	password=request.form['password']
	global current_user
	temp=current_user.login(email,password)
	if temp==True:
		return jsonify({'status':"success","message":"User logged in successfully"})
	else:
		return jsonify({'status':"failed","message":"User login failed"})

@app.route("/api/shoppinglist",methods=['POST'])
def add_shoppinglist():
	"""Add a user's shoppinglist"""
	name=request.form['name']
	itemnumber=request.form['description']
	global current_user
	current_user.add_shoppinglist(name,itemnumber)
	shoppinglist=current_user.view_shoppinglist(name)
	return jsonify({"status":"success","message":"shoppinglist added successfully","data":name})

@app.route("/api/shoppinglistitem/<string:shoppinglist>/item/add",methods=['POST'])
def add_item(shoppinglist):
	"""This adds an Item to the cart list and returns a JSON string with the ppropriate status"""
	global current_user
	item=request.form['item']
	item=current_user.add_shoppinglist_item(shoppinglist,item)
	if item !=False:
		return jsonify({"status":"success","message":"shoppinglist item added succcessfully","data":item})
	else:
		return jsonify({"status":"failed","message":"shoppinglist item not added"})

@app.route('/api/<string:shoppinglist>/item/<string:item>/edit',methods=['POST'])
def edit_item(shoppinglist,item):
	global current_user
	old_name=item
	new_name=request.form['new_name']
	result=current_user.edit_shoppinglist_item(shoppinglist,old_name,new_name)
	if result !=False:
		return jsonify({"status":"success","message":"Item edited successfully","data":result})
	else:
		return jsonify({"status":"failed","message":"Item failed to edit"})

@app.route("/api/shoppinglists")
def view_carts():
	global current_user
	shoppinglists=[]

	carts=current_user.view_shoppinglist()
	for cart in carts:
		shoppinglists.append(current_user.view_shoppinglist(cart))
	return jsonify({"status":"success","data":shoppinglists})

@app.route("/api/shoppinglist/<string:shoppinglist>/edit",methods=['POST'])
def edit_shoppinglist(shoppinglist):
	global current_user
	if shoppinglist in current_user.shoppinglists:
		name=request.form['name']
		itemnumber=request.form['name']
		example=current_user.shoppinglists[shoppinglist].edit(name,itemnumber)
		if example:
			tmp=current_user.shoppinglists[shoppinglist]
			del current_user.shoppinglists[shoppinglist]
			current_user.shoppinglists[name]=tmp
			return jsonify({'status':'success','message':'shoppinglist edited successfully'})
		else:
			return jsonify({'status':'fail','message':'shoppinglist not edited'})
	else:
		return jsonify({'status':'fail','message':'shoppinglist not edited'})

@app.route("/api/shoppinglist/<string:cartname>")
def view_cart(cartname):
	global current_user
	resp=current_user.view_shoppinglist(cartname)

	if resp:
		return jsonify([{"status":"success","data":resp}])
	else:
		return jsonify({"status":"failed","message":"shoppinglist does not exist"})		

@app.route("/api/items/shoppinglist/<string:shoppinglist>",methods=['GET'])
def view_shoppinglist_item(shoppinglist):
	global current_user
	shoppinglist_items=current_user.view_cart_list_item(shoppinglist)
	if shoppinglist_items:
		list_items=[]
		for item in shoppinglist_items:
			list_items.append(item.show_info())
		return jsonify({"status":"success","data":list_items})
	else:
		return jsonify({"status":"failed","message":"No items returned"})


@app.route("/api/item/<string:shoppinglist>/<string:item_name>")
def view_items(shoppinglist,item_name):
	global current_user
	shoppinglist_item=current_user.view_cart_list_item(shoppinglist,item_name)
	if shoppinglist_item:
		list_items=[]
		list_items.append(shoppinglist_item[0].show_info())
		return jsonify({"status":"success","data":list_items})
	else:
		return jsonify({"status":"failed","message":"No items returned"})

@app.route("/api/delete/<string:shoppinglist>/<string:item_name>")
def delete(shoppinglist,item_name):
	global current_user
	shoppinglist_item=current_user.delete_shoppinglist_item(shoppinglist,item_name)
	if shoppinglist_item:
		return jsonify({"status":"success","data":"Deleted successfully"})
	else:
		return jsonify({"status":"failed","message":"Delete fail"})

@app.route("/api/complete/<string:shoppinglist>/<string:item>")
def complete(shoppinglist,item):
	global current_user
	completed=current_user.mark_complete(shoppinglist,item)
	if completed:
		return jsonify({"status":"success","data":completed})
	else:
		return jsonify({"status":"failed","message":"Item not marked complete"})