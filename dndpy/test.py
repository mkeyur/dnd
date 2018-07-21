class UniqueCharsSet(object):

    def has_unique_chars(self, string):
        if string is None:
            print string
            return False
        return len(set(string)) == len(string)

if __name__ == '__main__':
    unique_chars_set = UniqueCharsSet()
