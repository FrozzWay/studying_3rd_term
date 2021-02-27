class Record:
    def __init__(self, data):
        self.id = data.get("id")
        self.surname = data.get("surname", "")
        self.reg_number = data.get("reg_number", "")
        self._from = data.get("from", "")
        self.up_to = data.get("up_to", "")
        self.rate = data.get("rate", "")
        self.copy_of_data = data
        self.next = None

    def __getitem__(self, key):
        return getattr(self, key)


class Collection:
    def __init__(self):
        self.first = None
        self.sorted_first = None

    def fill(self):
        id = 0
        while True:
            stop_input = False

            data = dict()
            keys = ("surname", "reg_number", "from", "up_to", "rate")

            data['id'] = id
            id += 1

            for key in keys:
                print(f'{key}: ')
                value = input()
                if value == "":
                    stop_input = True
                    break
                data[key] = value

            tmp = Record(data)

            if self.first is None:
                self.first = tmp
            elif data.get('surname'):
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
            for key, val in current.copy_of_data.items():
                print(f'{key}: {val}')
            current = current.next

    def sort(self, key):
        current_unsorted = self.first
        current_sorted = Record(self.first.copy_of_data)

        # Берем каждый элемент по порядку из неотсортерованного списка (element)
        while current_unsorted is not None:
            # element <= first el.
            if current_unsorted[key] <= current_sorted[key]:
                pass
            current_unsorted = current_unsorted.next


collection = Collection()
collection.fill()
collection.output()
