# from flask import Flask, jsonify, request
# from flask_cors import CORS

# app = Flask(__name__)
# CORS(app)  # Enable Cross-Origin Resource Sharing

# # Sample data (replace with your data source)
# data = [
#     {"id": 1, "name": "Item 1"},
#     {"id": 2, "name": "Item 2"},
#     {"id": 3, "name": "Item 3"},
# ]

# @app.route('/api/items', methods=['GET'])
# def get_items():
#     return jsonify(data)

# @app.route('/api/items', methods=['POST'])
# def add_item():
#     new_item = request.json
#     if new_item:
#         new_item["id"] = len(data) + 1
#         data.append(new_item)
#         return jsonify({"message": "Item added successfully"}), 201
#     else:
#         return jsonify({"message": "Invalid data"}), 400

# if __name__ == '__main__':
#     app.run(debug=True)
