def get_val(collection, key, default='git'):
    value = collection.get(key, 'Not found')
    if value == 'Not found':
        return default
    return value