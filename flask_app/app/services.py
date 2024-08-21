def fetch_data():
    # Mock data simulating external service response
    return {"numbers": [1, 2, 3, 4, 5], "text": "hello world"}

def process_data(data):
    # Example processing: summing numbers and converting text to uppercase
    processed_data = {
        "sum": sum(data["numbers"]),
        "uppercase_text": data["text"].upper()
    }
    return processed_data
