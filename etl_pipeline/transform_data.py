class DataTransformer:
    def __init__(self, data):
        self.data = data

    def transform(self):
        # Example transformation: Add a 'source' field to each post
        for item in self.data:
            item['source'] = 'jsonplaceholder API'
        return self.data
