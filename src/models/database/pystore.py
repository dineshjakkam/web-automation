import pystore
import os


class DataBase:
    def __init__(self):
        pystore.set_path(os.getcwd())
        self.store = pystore.store('webautomation')
        self.collection = None

    def get_store(self):
        return self.store

    def start_collection(self, collection):
        if self.collection is None:
            self.collection = self.store.collection(collection)

    def write_value(self, key, df):
        try:
            if key in self.collection.list_items():
                item = self.collection.item(key)
                self.collection.append(key, df, npartitions=item.data.npartitions)
            else:
                self.collection.write(key, df)
        except Exception as e:
            print("Exception in write_value {}".format(e))




