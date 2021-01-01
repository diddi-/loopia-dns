from enum import Enum


class RecordType(Enum):
    CNAME = "CNAME",
    A = "A"

    def __str__(self):
        return self.value
