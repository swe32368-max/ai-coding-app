# CRUD Operations for Database Models

class DatabaseModel:
    def __init__(self):
        self.data = {}

    def create(self, key, value):
        """
        Create a new entry in the database.
        """
        self.data[key] = value
        return f'Entry {key} created.'

    def read(self, key):
        """
        Read an entry from the database.
        """
        return self.data.get(key, 'Entry not found.')

    def update(self, key, value):
        """
        Update an existing entry in the database.
        """
        if key in self.data:
            self.data[key] = value
            return f'Entry {key} updated.'
        else:
            return 'Entry not found.'

    def delete(self, key):
        """
        Delete an entry from the database.
        """
        if key in self.data:
            del self.data[key]
            return f'Entry {key} deleted.'
        else:
            return 'Entry not found.'

# Example usage
if __name__ == '__main__':
    db = DatabaseModel()
    print(db.create('item1', {'name': 'Sample Item', 'price': 10.99}))
    print(db.read('item1'))
    print(db.update('item1', {'name': 'Updated Item', 'price': 12.99}))
    print(db.read('item1'))
    print(db.delete('item1'))
    print(db.read('item1'))
