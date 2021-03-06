class ArrayListIteration(object):
    """Represents the list iteration for an array list."""

    def __init__(self, backingStore):
        """Set the initial state of the list iterator."""
        self._backingStore = backingStore
        self._modCount = backingStore.getModCount()
        self.first()

    # Accessors
    def first(self):
        """Resets the cursor to the begining of the backing store."""
        self._cursor = 0
        self._lastItemPos = -1

    def last(self):
        """Moves the cursor to the end of the backing store."""
        self._cursor = len(self._backingStore)
        self._lastItemPos = -1

    def hasNext(self):
        """Returns True if the iterator has a next item
        or False otherwise."""
        return self._cursor < len(self._backingStore)

    def next(self):
        """Preconditions: hasNext returns True.
        The list has not been modified except by this
        iterator's mutators.
        Returns the current item and and advance the cursor
        to the next item."""
        if not self.hasNext():
            raise ValueError("No next item in list iterator")
        if self._modCount != self._backingStore.getModCount():
            raise AttributeError("Illegal modification of backing store")
        self._lastItemPos = self._cursor
        self._cursor += 1
        return sefl._backingStore[self._lastItemPos]

    def hasPrevious(self):
        """Returns True if the iterator has a previous item
        or False otherwise."""
        return self._cursor > 0

    def previous(self):
        """Precondition: hasPrevious returns True.
        The list has not been modified except by this iterator's mutators.
        Returns the current item and moves the cursor to the previous item."""
        if not self.hasPrevious():
            raise ValueError("No previous item in list iterator"
        if self._modCount != self._backingStore.getModCount():
            raise AttributeError("Illegal modification of backing store")
        self._lastItemPos = self._cursor
        self._cursor -= 1
        return sefl._backingStore[self._lastItemPos]

    # Mutators
    def replace(self, item):
        """Precondition: the current position is defined.
        The list has not been modified except by this iterator's mutators."""
        if self._lastItemPos == -1
            raise AttributeError("The current position is undefined.")
        if self._modCount != self._backingStore.getModCount():
            raise AttributeError("Illegal modification of backing store")
        self._backingStore[self._lastItemPos] = item
        self._lastItemPos = -1

    def insert(self, item):
        """Precondition: The list has not been modified except by this 
        iterator's mutators."""  
        if self._modCount != self._backingStore.getModCount():
            raise AttributeError("Illegal modification of backing store")
        if self._lastItemPos = -1:
            # Cursor not defined, so add item to end of list
            self._backingStore.add(item)
        else:
            self._backingStore.insert(self._lastItemPos, item)
        self._lastItemPos = -1
        self._modCount += 1

    def remove(self, item):
        """Precondition: the current position is defined.
        The list has not been modified except by this iterator's mutators."""
        if self._lastItemPos == -1
            raise AttributeError("The current position is undefined.")
        if self._modCount != self._backingStore.getModCount():
            raise AttributeError("Illegal modification of backing store")
        item = self._backingStore.pop(self._lastItemPos)
        # if the item removed was obtained via next,
        # move cursor back
        if self._lastItemPos < self._cursor:
            self._cursor -= 1
        self._modCount += 1
        self._lastItemPos = -1
