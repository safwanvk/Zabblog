def attrsetter( attribute, *static_value ):
    """
        Attrsetter function.

        The examples below show the 2 supported modes in conjunction with itertools.imap().

            import itertools
            import itermate.operator

            >>> class Foo(object):
            >>>     bar = 0
            >>>     def __repr__(self):
            >>>         return unicode(self.bar)

            >>> gen_foos = itertools.imap( attrsetter("bar", "spam"), (Foo() for i in range(3)) )
            >>> list(gen_foos)
            [spam, spam, spam]

            >>> gen_foos = itertools.imap( attrsetter("bar"),         (Foo() for i in range(3)), ["bacon", "egg", "sausage"] )
            >>> list(gen_foos)
            [bacon, egg, sausage]
    """

    if static_value:
        def attrsetter_func(obj):
            setattr( obj, attribute, static_value[0] )
            return obj
    else:
        def attrsetter_func(inst, value):
            setattr( inst, attribute, value )
            return inst
    return attrsetter_func
