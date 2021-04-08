.. pydoodle documentation master file, created by
   sphinx-quickstart on Fri Apr  2 14:16:33 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to pydoodle's documentation!
====================================

- pydoodle is an API wrapper of online compiler jdoodle.com written in python.
- Requires python 3.5 or above.

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


Look how easy it is to use:
---------------------------

.. code-block:: python

    import pydoodle
    c = pydoodle.Compiler(clientId="client-id", clientSecret="client-secret")
    result = c.execute(script="print('Hello World')", language="python3")
    usage = c.usage()
    print(usage, result.output, sep='\n')

.. toctree::
   :maxdepth: 2

   api

Indices and tables
==================

* :ref:`genindex`
* :ref:`search`
