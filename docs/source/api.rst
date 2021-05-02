API Reference
=============

Compiler
---------
.. autoclass:: pydoodle.Compiler
    :members:

.. note::
    All types of links aren't yet supported and not to be provided in the ``script`` parameter.
    Currently, supported links are: `pastebin.com`_, `hatstebin.com`_, `textbin.net`_ and `pastie.org`_.
    Working on to add more of them. Want to suggest? `Start a new discussion`_ on github repo.

.. Attention:: Only provide links which can be visible by everyone without any kind of password.

    .. _pastebin.com: https://pastebin.com
    .. _hatstebin.com: https://hastebin.com
    .. _textbin.net: https://textbin.net
    .. _pastie.org: https://pastie.org
    .. _Start a new discussion: https://github.com/Prince2347X/pydoodle/discussions/new

Output
--------

.. autoclass:: pydoodle.jdoodle.Output
    :members:
    .. confval:: output
        The output of the script.
    .. confval:: statusCode
        The status code of the executed program.
    .. confval:: memory
        The memory used to execut the script.
    .. confval:: cpuTime
        Time taken to execut the script (in seconds).

.. _here:
    https://docs.jdoodle.com/compiler-api/compiler-api#what-languages-and-versions-supported
