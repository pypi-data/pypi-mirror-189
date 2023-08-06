from FNLP.Language import Words

from F import DICT, DATE, CONVERT
from F.TYPE.Dict import fict
from F.TYPE.List import fist

""" Smart dict:type wrapper for Single MongoDB Record."""
class Record(fict):
    _id = ""
    fields = []
    original_record = None

    def __init__(self, record, **kwargs):
        super().__init__(**kwargs)
        self.original_record = record
        self.import_record(record)

    def import_record(self, record:dict):
        if not record:
            return None
        self._id = DICT.get("_id", record, "Unknown")
        self._add_fields(record)
        self.update(record)

    def _add_fields(self, record:dict):
        for key in record.keys():
            self.fields.append(key)

    def get_field(self, fieldName):
        return self[fieldName]

    def get_embeddedDict(self, fieldName, key):
        obj: dict = self.get_field(fieldName)
        embedded_obj = DICT.get(key, obj, None)
        return embedded_obj

    def update_updatedDate(self):
        self["updatedDate"] = DATE.TODAY

    def update_field(self, fieldName, value):
        self[fieldName] = value
        self.update_updatedDate()

    def export(self, isUpdate=False):
        if isUpdate:
            self.update_updatedDate()
        result = {}
        for f in self.fields:
            result[f] = self[f]
        return result

    def smartAddUpdate(self, fmdbObject):
        dbCollection = fmdbObject.collection(self.collection_name)
        dbCollection.smart_AddUpdate(self)



""" Smart list:type wrapper for List of MongoDB Records."""
class Records(fist):
    database_name = ""
    collection_name = ""

    def set_database_name(self, database_name):
        self.database_name = database_name

    def set_collection_name(self, collection_name):
        self.collection_name = collection_name

    def import_records(self, records:list):
        for rec in records:
            newR = Record(rec)
            self.append(newR)

    def loop_exported(self) -> dict:
        for rec in self:
            rec: Record
            yield rec.export()

    def loop_records(self) -> Record:
        for rec in self:
            rec: Record
            yield rec

    def to_exported_list(self) -> [dict]:
        results = []
        for item in self:
            results.append(item.export())
        return results

    def flatten(self):
        pass

    """
    [ { "field1": "value1", "field2": "value2" },  { "date": "12334", "word_counts": { "example": 2 } } ]
    { "value1" : "value2" }
    """
    def map_to_fields(self, field1, field2):
        mapped = {}
        for item in self:
            val1 = DICT.get(field1, item, None)
            val2 = DICT.get(field2, item, None)
            mapped[val1] = val2
        return mapped

    @staticmethod
    def map_fields(dic, keyField: str, valueField: str, sortByKey=True):
        temp = dic
        if sortByKey:
            temp = DICT.SORT_BY_KEY(temp, False)
        keyList = CONVERT.dict_TO_List_OF_Keys(temp)
        valueList = CONVERT.dict_TO_List_OF_Values(temp)
        mapped = {keyField: keyList, valueField: valueList}
        return mapped

    def prepare_word_count(self, word):
        mapped_records = {}
        for item in self:
            date = DICT.get("date", item, None)
            word_counts = DICT.get("word_counts", item, None)
            capital = Words.make_capital(word)
            word_count = DICT.get(capital, word_counts, 0)
            word_count2 = DICT.get(str(word).lower(), word_counts, 0)
            if not word_count or not date or str(date) == "Unknown":
                continue
            keyName = str(date)
            mapped_records[keyName] = int(word_count) + int(word_count2)
        return mapped_records


    # def map_dict(self, keyField: str, valueField: str, sortByKey=True):
    #     if sortByKey:
    #         dic = DICT.SORT_BY_KEY(self, False)
    #     keyList = CONVERT.dict_TO_List_OF_Keys(self)
    #     valueList = CONVERT.dict_TO_List_OF_Values(self)
    #     mapped = {keyField: keyList, valueField: valueList}
    #     return mapped



    def smartAddUpdateRecords(self, fmdbObject):
        dbCollection = fmdbObject.collection(self.collection_name)
        dbCollection.smart_AddUpdate(self)

"""
capital = Words.make_capital(WORD)
word_count = DICT.get(capital, word_counts, 0)
word_count2 = DICT.get(str(WORD).lower(), word_counts, 0)
if not word_count or not date or str(date) == "Unknown":
    continue
keyName = str(date)
mapped_records[keyName] = int(word_count) + int(word_count2)
"""

"""
db = "research"
collection = "articles

fields = [ "_id", "title", "date" ]
single_article = {"_id": "1234", "title": "hey there", "date": "july 24 2022"}
"""