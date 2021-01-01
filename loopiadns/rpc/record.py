from loopiadns.rpc.record_type import RecordType


class Record:
    def __init__(self, record_type: RecordType, data: str, ttl: int = 3600, record_id: int = None):
        self.__type = record_type
        self.__ttl = ttl
        self.__data = data
        self.__record_id = record_id
        self.__priority = 0

    @property
    def type(self):
        return self.__type

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

    @property
    def id(self):
        return self.__record_id

    @property
    def ttl(self):
        return self.__ttl

    @property
    def priority(self):
        return self.__priority

    def as_dict(self):
        result = {
            "type": str(self.type),
            "ttl": self.ttl,
            "rdata": self.data,
            "priority": self.priority
        }
        if self.id is not None:
            result["record_id"] = self.id

        return result
