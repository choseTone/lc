__author__ = 'wangqc'

'''
284. Peeking Iterator

Given an Iterator class interface with methods: next() and hasNext(), design and implement a PeekingIterator that 
support the peek() operation -- it essentially peek() at the element that will be returned by the next call to next().

Example:

Assume that the iterator is initialized to the beginning of the list: [1,2,3].

Call next() gets you 1, the first element in the list.
Now you call peek() and it returns 2, the next element. Calling next() after that still return 2. 
You call next() the final time and it returns 3, the last element. 
Calling hasNext() after that should return false.
Follow up: How would you extend your design to be generic and work with all types, not just integer?
'''


class Iterator(object):
    def __init__(self, nums):
        self.iter = iter(nums)
        self._hasNext = None

    def hasNext(self):
        if self._hasNext is None:
            try: self._next = next(self.iter)
            except StopIteration: self._hasNext = False
            else: self._hasNext = True
        return self._hasNext

    def next(self):
        result = self._next if self._hasNext else next(self.iter)
        self._hasNext = None
        return result


class PeekingIterator(object):
    def __init__(self, iterator):
        self.iter = iterator
        self._peek = self.iter.next() if self.iter.hasNext() else None

    def peek(self):
        return self._peek

    def next(self):
        peek = self._peek
        self._peek = self.iter.next() if self.iter.hasNext() else None
        return peek

    def hasNext(self):
        return self._peek != None


if __name__ == '__main__':
    from time import time

    iter = PeekingIterator(Iterator([1, 5, 2, 1, 3]))
    t, ans = time(), []
    while iter.hasNext():
        ans.append(iter.peek())
        iter.next()
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))
