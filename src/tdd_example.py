class TDDExample():
    def __init__(self):
        pass

    def reverse_string(self, input_str: str) -> str:
        """
        Reverses order of characters in string input_str.
        """
        return input_str[::-1]

    def find_longest_word(self, sentence: str) -> str:
        """
        Returns the longest word in string sentence.
        In case there are several, return the first.
        """
        sentence = list(sentence.split(" "))
        s = sorted(sentence, key = len)
        return s[-1]

    def reverse_list(self, input_list: list) -> list:
        """
        Reverses order of elements in list input_list.
        """

        return input_list[::-1]

    def count_digits(self, input_list: list, number_to_be_counted: int) -> int:
        """
        Return count of digits
        """
        cnt = 0
        for i in input_list:
            if i == number_to_be_counted:
                cnt+=1
        return cnt