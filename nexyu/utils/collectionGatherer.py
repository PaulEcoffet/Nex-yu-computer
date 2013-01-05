class CollectionGatherer:

    def __init__(self,  callback):
        self.callback = callback
        self.data = {}

    def addToCollection(self, id, data):
        if id not in self.data:
            self.data[id] = {"data": [data], "size": -1}
        else:
            self.data[id]["data"].append(data)
        size = self.data[id]["size"]
        if size != -1 and len(self.data[id]["data"]) == size:
            self._collectionComplete(id)

    def setCollectionSize(self, id, size):
        if id not in self.data:
            self.data[id] = {"data": [], "size": size}
        else:
            self.data[id]["size"] = size
        if len(self.data[id]["data"]) == size:
            self._collectionComplete(id)

    def _collectionComplete(self, id):
        self.callback.onCollectionComplete(self.data[id]["data"])
        del self.data[id]
