from flask import Flask,render_template,request,jsonify

app = Flask(__name__)

items = [
    {'id': 1, 'name':'Item 1' ,'description':"first static work"},
    {'id': 2, 'name':'Item 2' ,'description':"second static work"}
]

@app.route("/")
def welcome():
    return "Welcome to ToDo web app"

# get all the items of ToDo
@app.route("/items",methods=['GET'])
def get_items():
    return jsonify(items)

# get specific item by id
@app.route("/items/<int:item_id>",methods=['GET'])
def get_item_byid(item_id):
    item = next(item for item in items if item_id == item["id"])
    if item is None:
        return "Error : Item is missing"
    return jsonify(item)

# create a new task
@app.route("/items",methods=['POST'])
def create_item():
    if not request.json or not 'name' in request.json:
        return jsonify({"Error : item not found"})
    new_item={
        "id" : items[-1]["id"] + 1 if items else 1,
        "name" : request.json['name'],
        "description" : request.json['description']
    }
    items.append(new_item)
    return jsonify(new_item)

# update an existing item
@app.route("/items_update/<int:item_id>",methods=['PUT'])
def update_item(item_id):
    item = next(item for item in items if item_id == item["id"])
    if item is None:
        return "Error : Item is missing"
    item['name'] = request.json.get('name',item['name'])
    item['description'] = request.json.get('description',item['description'])

    return jsonify(item)

# Delete an item
@app.route("/items_delete/<int:item_id>",methods=['DELETE'])
def delete_item(item_id):
    global items
    item = next(item for item in items if item_id != item["id"])

    jsonify ({"results":"item deleted"})



# @app.route("/form")
# def todo_form():
#     return render_template("todo_form.html")

# @app.route("/submit<>",methods=['GET'])
# def form_submit():
#     return items

if __name__ == '__main__':
    app.run(debug=True)