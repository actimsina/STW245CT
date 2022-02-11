"""
Flask Based Rework of our app

So much easier with a web interface
"""
import flask
from flask import request
import pickle

class ShoppingItem:
    def __init__(self, name, cost, number = 1):
        self.name = name
        self.cost = cost
        self.number = number

class ShoppingList:
    def __init__(self):
        self.shoppingList = []

    def addItem(self, item):
        self.shoppingList.append(item)
        
    def calcCost(self):
        totalCost = 0
        for item in self.shoppingList:
            totalCost += item.cost * item.number

        return totalCost


def createList():
    """Helper Function to create a list"""
    theList = ShoppingList()
    
    item = ShoppingItem("foo widget", 100)
    theList.addItem(item)
    item = ShoppingItem("bar widget", 10, 5)
    theList.addItem(item)
    return theList


# ------------ AND THE APP ITSELF -----------
app = flask.Flask(__name__)
app.theList = createList()

@app.route('/')
def main():
    return flask.render_template('index.html', theList = app.theList)

@app.route("/save")
def save():
    #We can save the basket to a file
    with open("/opt/webapp/backup.pkl","wb") as fd:
        out = pickle.dump(app.theList, fd)
        #fd.write(out)
        
    return flask.send_file('backup.pkl',
                           mimetype='application/octet-stream',
                           attachment_filename='backup.pkl',
                           as_attachment=True)


@app.route("/load", methods=["GET","POST"])
def load():
    message = None
    if request.method == "POST":
        print (request.files)
        if 'uploadFile' in request.files:

            theFile = request.files['uploadFile']
            try:
                data = pickle.load(theFile)#, Loader=yaml.Loader)
                app.theList = data
                message = "Upload Successful"
            except Exception as ex:
                message = "Error Loading List {0}".format(ex)

            
        else:
            message = "You must select a file to upload"

    
    return flask.render_template('load.html', message=message)

@app.route("/pay")
def pay():

    totalCost = app.theList.calcCost()

    return flask.render_template("pay.html", cost=totalCost)
    
