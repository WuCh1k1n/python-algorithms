from arraybag import ArrayBag


class ArraySortedBag(ArrayBag):
    """An array-based sorted bag implementation."""

    # Constructor
    def __init__(self, sourceCollection=None):
        """Sets the initial state of self, which includes the 
        contents of sourceCollection, if it's present."""
        ArrayBag.__init__(self, sourceCollection)

    # Accessor methods
    def __contain__(self, item):
        """Returns True if item is in self, or False otherwise."""
        left = 0
        right = len(self) - 1
        while left <= right:
            midPoint = (left + right) // 2
            if self._items[midPoint] == item:
                return True
            else if self._items[midPoint] < item:
                left = midPoint + 1
            else:
                right = midPoint - 1
        return False

    # Mutator methods
    def add(self, item):
        """Add item to self."""
        # Empty or last item, call ArrayBag.add
        if self.isEmpty() or item > self._items[len(self) - 1]:
            ArrayBag.add(self, item)
        else:
            # Resize the array if it is full here
            # Search for first item >= new item
            targetIndex = 0
            while item > self._items[targetIndex]:
                targetIndex += 1
            # Open a hole for net item
            for i in range(len(self), targetIndex, -1):
                self._items[i] = self._items[i - 1]
            self._items[targetIndex] = item
            self._size += 1
