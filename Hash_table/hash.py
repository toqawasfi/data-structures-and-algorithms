class Hashtable:
    def __init__(self, size=100):
        """
        Initializes a Hashtable
        """
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash(self, key):
        """
        Computes the hash value for the given key.
        """
        return hash(key) % self.size

    def set(self, key, value):
        """
        Sets the key-value pair in the hashtable, handling collisions as needed.
        """
        hash_value = self.hash(key)
        for i, (existing_key, existing_value) in enumerate(self.table[hash_value]):
            if existing_key == key:
                self.table[hash_value][i] = (key, value)
                return
        self.table[hash_value].append((key, value))

    def get(self, key):
        """
        Retrieves the value associated with the given key from the hashtable.
        """
        hash_value = self.hash(key)
        for existing_key, value in self.table[hash_value]:
            if existing_key == key:
                return value
        return None

    def has(self, key):
        """
        Checks if the given key exists in the hashtable.
        """
        hash_value = self.hash(key)
        for existing_key, _ in self.table[hash_value]:
            if existing_key == key:
                return True
        return False

    def keys(self):
        """
        Retrieves all the keys from the hashtable.
        """
        keys = []
        for bucket in self.table:
            for key, _ in bucket:
                keys.append(key)
        return keys