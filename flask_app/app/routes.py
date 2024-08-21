from flask import Blueprint, jsonify
from .services import fetch_data, process_data
from .storage import store_data, get_stored_data

main_bp = Blueprint('main', __name__)

@main_bp.route('/fetch-data', methods=['GET'])
def fetch_data_route():
    # Simulate fetching data from an external service
    data = fetch_data()
    
    # Process the fetched data
    processed_data = process_data(data)
    
    # Store the processed data
    store_data(processed_data)
    
    return jsonify({"message": "Data fetched and processed successfully"}), 200

@main_bp.route('/get-processed-data', methods=['GET'])
def get_processed_data_route():
    # Retrieve the processed data from storage
    data = get_stored_data()
    return jsonify(data), 200
