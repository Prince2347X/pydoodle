.. pydoodle documentation master file, created by
   sphinx-quickstart on Fri Apr  2 14:16:33 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to pydoodle's documentation!
====================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Look how easy it is to use:
---------------------------

.. code-block:: python

    import pydoodle
    c = pydoodle.Compiler(clientId="client-id", clientSecret="client-secret")
    output = c.execute(script="print('Hello World')", language="python3")
    usage = c.usage()
    print(usage, output, sep='\n')

Features
--------

- Easy to use.
- Over 50+ languages to compile.
- Get the credits spent information.


Installation
------------

Install pydoodle by running:

.. code-block::

    pip install pydoodle



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
