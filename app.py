from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory "database"
items = [
    {"id": 1, "name": "Apple", "price": 1.5},
    {"id": 2, "name": "Banana", "price": 0.5},
]

# GET all items
@app.route("/items", methods=["GET"])
def get_items():
    return jsonify(items)

# GET single item
@app.route("/items/<int:item_id>", methods=["GET"])
def get_item(item_id):
    item = next((i for i in items if i["id"] == item_id), None)
    if item is None:
        return jsonify({"error": "Item not found"}), 404
    return jsonify(item)

# POST - create new item
@app.route("/items", methods=["POST"])
def create_item():
    data = request.get_json()
    new_item = {
        "id": items[-1]["id"] + 1 if items else 1,
        "name": data["name"],
        "price": data["price"],
    }
    items.append(new_item)
    return jsonify(new_item), 201

# PUT - update existing item
@app.route("/items/<int:item_id>", methods=["PUT"])
def update_item(item_id):
    item = next((i for i in items if i["id"] == item_id), None)
    if item is None:
        return jsonify({"error": "Item not found"}), 404
    data = request.get_json()
    item.update(data)
    return jsonify(item)

# DELETE - remove item
@app.route("/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    global items
    items = [i for i in items if i["id"] != item_id]
    return jsonify({"message": "Item deleted"})

if __name__ == "__main__":
    app.run(debug=True)
