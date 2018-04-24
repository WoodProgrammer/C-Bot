from pymongo import MongoClient


class BotModel:
    def __init__(self):
        self._cli = MongoClient()
        self._db = self._cli['chat_bot']

    def _set_payload(self,payload):
        try:
            self._db['payloads'].insert_one(payload)
            return True
        except Exception as exp:
            #logging exp
            return exp

    def _get_detail(self,payload_name):
        return self._db['payloads'].find_one({'payload_name':payload_name})

    def _get_detail(self,id):
        return self._db['payloads'].find_one({'id':id})
