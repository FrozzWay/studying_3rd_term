class Record:
    def __init__(self, data):
        self.data = data
        self.next = None


class Collection:
    def __init__(self):
        self.first = None
        self.sorted_first = None

    def fill(self):
        id = 0
        while True:
            stop_input = False

            data = dict()
            #keys = ("surname", "reg_number", "from", "up_to", "rate")
            keys = ("surname",)

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

    def output(self, x):
        if x:
            current = self.first
        else:
            current = self.sorted_first
        while current is not None:
            for key, val in current.data.items():
                print(f'{key}: {val}')
            print('')
            current = current.next

    def search(self, criteria, value):
        current = self.first
        while current is not None:
            if current.data[criteria] == value:
                for key, val in current.data.items():
                    print(f'{key}: {val}')
            current = current.next

    def sort(self, criteria):
        current_unsorted = self.first.next  # 2й элемент исходного списка
        self.sorted_first = Record(self.first.data)  # Копирование первого элемента в результирующий список

        # Берем каждый элемент по порядку из неотсортерованного списка (element) начиная со 2го
        while current_unsorted is not None:
            tmp = Record(current_unsorted.data)
            self._compare_and_put(tmp, criteria)
            # move next
            current_unsorted = current_unsorted.next

    def _compare_and_put(self, tmp, criteria):
        current_sorted = self.sorted_first
        # element <= first el.
        if tmp.data[criteria] <= current_sorted.data[criteria]:
            tmp.next = current_sorted
            self.sorted_first = tmp
            return
        # element > first el.
        while True:
            # element > last el.
            if current_sorted.next is None:
                tmp.next = None
                current_sorted.next = tmp
                return
            # prev. el. < element <= next el.
            if current_sorted.data[criteria] < tmp.data[criteria] <= current_sorted.next.data[criteria]:
                tmp2 = current_sorted.next
                current_sorted.next = tmp
                tmp.next = tmp2
                return

            current_sorted = current_sorted.next


collection = Collection()