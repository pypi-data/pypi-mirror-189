from pymongo import MongoClient

from F.CLASS import Flass
from F.LOG import Log

s = " "
Log = Log(f"DBClient")

"""
    -> THE MASTER BASE CLASS
        - The Database Instance Itself.
    -> Does not need a collection to be initiated.
    -> Other Classes inherent this object.
"""

BASE_MONGO_URI = lambda mongo_ip, mongo_port: f"mongodb://{mongo_ip}:{mongo_port}"
BASE_MONGO_AUTH_URI = lambda mongo_ip, mongo_port, user, pw: f"mongodb://{user}:{pw}@{mongo_ip}:{mongo_port}"

class FMClient(Flass):
    host = None
    ip = None
    port = 27017
    username = None
    password = None
    client_info = None
    client_connection_status = False
    client: MongoClient = None
    db = None
    databases = {}
    database_names = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if self.ip:
            self.connect(self.ip, self.port, self.username, self.password)
        elif self.host:
            self.connect(self.host, self.port, self.username, self.password)
        if self.client_connection_status:
            self.databases = {}
            self.get_all_databases()

    def get_all_databases(self):
        dbs = self.client.list_database_names()
        for db_name in dbs:
            self.databases[db_name] = self.client[db_name]

    def get_collection(self, name):
        return self.db[name]

    def insert_one(self, collection, document):
        self.db[collection].insert_one(document)

    def find_one(self, collection, query={}):
        return self.db[collection].find_one(query)

    def find(self, collection, query={}):
        return self.db[collection].find(query)

    def update_one(self, collection, query, update):
        self.db[collection].update_one(query, update)

    def delete_one(self, collection, query):
        self.db[collection].delete_one(query)

    def close(self):
        self.client.close()

    # -> !!MAIN CONSTRUCTOR!! <-
    def connect(self, ip, port=27017, username=None, password=None, database=None):
        Log.i(f"DBClient: HOST=[ {ip}:{port} ]")
        url = BASE_MONGO_URI(ip, port)
        if username:
            url = BASE_MONGO_AUTH_URI(ip, port, username, password)
        try:
            Log.i(f"Initiating MongoDB: URI={url}")
            self.client = MongoClient(host=url, connectTimeoutMS=10000)
            self.is_connected()
            return self
        except Exception as e:
            Log.e(f"Unable to initiate MongoDB: URI={url}", error=e)
            return None

    def is_connected(self):
        try:
            # Ping the server to see if it's reachable
            self.client.admin.command('ping')
            self.client_connection_status = True
            self.client_info = self.client.server_info()
            self.database_names = self.client.list_database_names()
            Log.d("MongoDB is Up.")
            return True
        except Exception as e:
            Log.e("MongoDB is Down.", error=e)
            self.client_connection_status = False
            self.client_info = None
            self.database_names = None
            return False


if __name__ == '__main__':
    client = FMClient()
    client.connect("192.168.1.180", 27017)
    print(client)