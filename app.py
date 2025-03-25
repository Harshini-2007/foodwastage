from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

available_food = {}  # In-memory storage for demonstration

@app.route('/api/submit-food', methods=['POST'])
def submit_food():
    data = request.get_json()
    restaurant_name = data.get('restaurantName')
    food_quantity = data.get('foodQuantity')
    contact_number = data.get('contactnumber')
    address = data.get('address')

    if restaurant_name and food_quantity and contact_number and address is not None:
        available_food[restaurant_name] = {
            'quantity': food_quantity,
            'contact': contact_number,
            'address': address
        }
        print(f"{restaurant_name} submitted {food_quantity} units of food.")
        return jsonify({'message': 'Food availability submitted successfully!'}), 200
    else:
        return jsonify({'error': 'Missing restaurant name or food quantity or contact number or address.'}), 400

@app.route('/api/available-restaurants', methods=['GET'])
def get_available_restaurants():
    available_list = []
    for name, data in available_food.items():
        available_list.append({
            "name": name,
            "quantity": data.get('quantity'),
            "contact": data.get('contact'),
            "address": data.get('address')
        })
    return jsonify(available_list), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)