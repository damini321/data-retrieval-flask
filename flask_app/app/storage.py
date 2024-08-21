_storage = {}

def store_data(data):
    global _storage
    _storage = data

def get_stored_data():
    return _storage
