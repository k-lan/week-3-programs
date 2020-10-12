from pythonds.basic import Queue


def get_tens(num: int):
    """
     :param num: number to read
     :return: int in the tens place
     """
    tmp = str(num)
    ones = tmp[len(tmp) - 2]
    return int(ones)


def get_ones(num: int):
    """
    :param num: number to read
    :return: int in the ones place
    """
    tmp = str(num)
    ones = tmp[len(tmp) - 1]
    return int(ones)


def get_hundreds(num: int):
    """
     :param num: number to read
     :return: int in the hundreds place
     """
    tmp = str(num)
    ones = tmp[len(tmp) - 3]
    return int(ones)


class RadixSort():
    def __init__(self, num_list):
        """
        Sort a number list using a radix sort, takes a list of ints and sorts them from
        smallest to largest. Will not work if numbers are larger than 3 digits.
        :param num_list:
        :return:
        """
        self.main_bin = Queue()
        for num in num_list:
            self.main_bin.enqueue(num)
        self.bin_0 = Queue()
        self.bin_1 = Queue()
        self.bin_2 = Queue()
        self.bin_3 = Queue()
        self.bin_4 = Queue()
        self.bin_5 = Queue()
        self.bin_6 = Queue()
        self.bin_7 = Queue()
        self.bin_8 = Queue()
        self.bin_9 = Queue()

    def radix_sort(self):
        """
        Combines the RadixSort methods to sort the list,
        only works on single digit integers but is set up
        to be further programmed to accept lists with multiple digit numbers.
        :return: List of sorted numbers
        """
        while self.main_bin.size() != 0:  # Sort the items based on their ones position
            tmp = self.main_bin.dequeue()
            ones_pos = get_ones(tmp)
            self.add_to_bin(ones_pos, tmp)

        self.empty_bins()
        sorted_list = []
        while self.main_bin.size() != 0:
            sorted_list.append(self.main_bin.dequeue())
        return sorted_list

    def add_to_bin(self, temp, tmp):
        """
        Add number to the bin based on its value
        :param temp: Specific number that we're sorting off of
        :param tmp: entire number that we're adding to the list
        """
        if temp == 0:
            self.bin_0.enqueue(tmp)
        elif temp == 1:
            self.bin_1.enqueue(tmp)
        elif temp == 2:
            self.bin_2.enqueue(tmp)
        elif temp == 3:
            self.bin_3.enqueue(tmp)
        elif temp == 4:
            self.bin_4.enqueue(tmp)
        elif temp == 5:
            self.bin_5.enqueue(tmp)
        elif temp == 6:
            self.bin_6.enqueue(tmp)
        elif temp == 7:
            self.bin_7.enqueue(tmp)
        elif temp == 8:
            self.bin_8.enqueue(tmp)
        elif temp == 9:
            self.bin_9.enqueue(tmp)

    def empty_bins(self):
        """
        Empty each of the 10 bins into the main bin, this should sort them.
        """
        while self.bin_0.size() != 0:
            self.main_bin.enqueue(self.bin_0.dequeue())

        while self.bin_1.size() != 0:
            self.main_bin.enqueue(self.bin_1.dequeue())

        while self.bin_2.size() != 0:
            self.main_bin.enqueue(self.bin_2.dequeue())

        while self.bin_3.size() != 0:
            self.main_bin.enqueue(self.bin_3.dequeue())

        while self.bin_4.size() != 0:
            self.main_bin.enqueue(self.bin_4.dequeue())

        while self.bin_5.size() != 0:
            self.main_bin.enqueue(self.bin_5.dequeue())

        while self.bin_6.size() != 0:
            self.main_bin.enqueue(self.bin_6.dequeue())

        while self.bin_7.size() != 0:
            self.main_bin.enqueue(self.bin_7.dequeue())

        while self.bin_8.size() != 0:
            self.main_bin.enqueue(self.bin_8.dequeue())

        while self.bin_9.size() != 0:
            self.main_bin.enqueue(self.bin_9.dequeue())


def main():
    my_lst = [9, 7, 4, 8, 6]
    sort_machine = RadixSort(my_lst)
    my_lst = sort_machine.radix_sort()
    print(my_lst)


if __name__ == '__main__':
    main()
