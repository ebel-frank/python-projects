def register(customername, customeraddress, email, password, creditcard, accountbalance):
    global user1
    user1 = Customer(customername, customeraddress, email, password, creditcard, accountbalance)
    print("You've sucessfully created an account, your details are")
    print("email: {0}, password: {1}".format(user1.email, user1.password))

class  User(object):
    __userid = ""       # this is strong privating __userid
    __password = ""
    def __init__(self, userid, password, loginstatus, registerdate):
        self.userid = userid
        self.password = password
        self.loginstatus = loginstatus
        self.registerdate = registerdate
        self.I = "Hi"
    def verify_login(self):
        return bool

class Customer(User):
    
    def __init__(self, customername, customeraddress, email, password, creditcard, accountbalance):
    	self.customername = customername
    	self.customeraddress = customeraddress
    	self.email = email
    	self.password = password
    	self.creditcard = creditcard
    	self.accountbalance =accountbalance
    def login(self, email, password):
        if email==self.email and password==self.password:
            print(self.customername+", Login Sucessfull!")
        else:
            print("Invalid username and password.")
    def update_profile(self, customername, customeraddress, email, ):
    	self.customername = customername
    	self.customeraddress = customeraddress
    	self.email = email

class Administrator(User):
    def __init__(self, adminname, email):
        self.adminname = adminname
        self.email = email
    def UpdateCatalog(self):
        return "The catalog has been updated", bool


