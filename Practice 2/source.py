class Record:
    def __init__(self, data):
        self.surname = data.get("surname", "")
        self.reg_number = data.get("reg_number", "")
        self._from = data.get("from", "")
        self.up_to = data.get("up_to", "")
        self.rate = data.get("rate", "")
        self.next = None


class Collection:
    def __init__(self):
        self.first = None

    def fill(self):
        while True:
            stop_input = False

            data = dict.fromkeys(("surname", "reg_number", "from", "up_to", "rate"))
            for key in data.keys():
                print(f'{key}: ')
                value = input()
                if value == "":
                    stop_input = True
                    break
                data[key] = value

            tmp = Record(data)
            if self.first is None:
                self.first = tmp
            else:
                self._put(tmp, self.first)

            if stop_input:
                break

    def _put(self, tmp, first):
        current = first
        while current.next is not None:
            current = current.next
        current.next = tmp

    def output(self):
        current = self.first
        while current is not None:
            print(current.name)
            current = current.next


collection = Collection()
collection.fill()
#collection.output()