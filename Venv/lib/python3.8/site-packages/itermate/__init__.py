import itertools

try:
    # on py27 make map/filter behave like an iterator
    map = itertools.imap
    filter = itertools.ifilter
except AttributeError:
    # py3+
    pass



def imapchain(*a, **kwa):
    """ Like map but also chains the results. """

    imap_results = map( *a, **kwa )
    return itertools.chain( *imap_results )


def iapply(function, *iterables):
    """ Like itertools.imap, but returns the iterable's item/iterables' items instead. """

    iterables = map(iter, iterables)
    while True:
        args = [next(it) for it in iterables]
        if function is None:
            yield tuple(args)
        else:
            function(*args)
            yield args[0]


def iskip( value, iterable ):
    """ Skips all values in 'iterable' matching the given 'value'. """

    for e in iterable:
        if value is None:
            if e is None:
                continue
        elif e == value:
            continue
        yield e


def unique(iterable):
    """
        Generator yielding each element only once.

        Note: May consume lots of memory depending on the given iterable.
    """

    yielded = set()
    for i in iterable:
        if i in yielded:
            continue
        yield i
        yielded.add(i)


class iprogress:
    """ Adds progress feedback to countable (len) list when iterating. """

    def __init__( self, list, callback=lambda s:sys.stdout.write(s+"\n"), mode="percent" ):
        self._list = list
        self._callback_core = callback
        self._mode = mode

        self._index = 0
        self._amount = len(self._list)
        self._callback = self._get_callback()


    def next( self ):
        try:
            result = self._list[self._index]
            self._index += 1
            self._callback()
        except IndexError:
            raise StopIteration
        return result


    def _get_callback( self ):
        if self._mode == "percent":
            result = lambda: self._callback_core( "{0} %".format(int(float(self._index)/(float(self._amount)/100))) )
        if self._mode == "percent_integer":
            result = lambda: self._callback_core( int(float(self._index)/(float(self._amount)/100)) )
        elif self._mode == "float":
            result = lambda: self._callback_core( float(self._index)/self._amount )
        elif self._mode == "count":
            result = lambda: self._callback_core( "{0}/{1}".format(self._index, self._amount) )
        return result


    def __iter__( self ):
        return self
