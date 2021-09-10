<p align="center">
   <img src="https://user-images.githubusercontent.com/68418241/132795336-ec92639b-096d-429f-9d7f-1a1fa45fb3d8.gif" width=440>
</p>

<h1 align="center"> pydoodle: <p>An API wrapper of online compiler jdoodle.com written in python.</p> </h1>


## Stats
 - [![PyPI - Downloads](https://img.shields.io/pypi/dm/pydoodle)](https://pypi.org/project/pydoodle)
[![Documentation Status](https://readthedocs.org/projects/pydoodle/badge/?version=master)](https://pydoodle.readthedocs.io)
![PyPI - License](https://img.shields.io/pypi/l/pydoodle)
 - ![GitHub top language](https://img.shields.io/github/languages/top/Prince2347X/pydoodle)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/Prince2347X/pydoodle)
 - ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pydoodle)
 - ![GitHub Repo stars](https://img.shields.io/github/stars/Prince2347X/pydoodle?style=social)
![GitHub forks](https://img.shields.io/github/forks/Prince2347X/pydoodle?style=social)




## Features
 - Easy to use.
 - Over 50+ languages to compile.
 - Get the credits spent information.


## How to install?
Install pydoodle by running 
```
pip install pydoodle
```

### Documentation
 - Documentation is hosted on [pydoodle.readthedocs.io](https://pydoodle.readthedocs.io)

### Example
 - Look how easy it is to use:
 
    ```python
    import pydoodle
    c = pydoodle.Compiler(clientId="client-id", clientSecret="client-secret")
    result = c.execute(script="print('Hello World')", language="python3")
    usage = c.usage()
    print(usage, result.output, sep='\n')
    ```
 - [example.py](https://github.com/Prince2347X/pydoodle/blob/master/examples/example.py) -> Basic example on how to use!
 - [example_stdIn.py](https://github.com/Prince2347X/pydoodle/blob/master/examples/example_stdIn.py) -> Example on how to use stdIn (inputs).
 - [example_links.py](https://github.com/Prince2347X/pydoodle/blob/master/examples/example_links.py) -> Example on how to use links as script.


### Misc 
 - Star [this repo](https://github.com/Prince2347X/pydoodle/) if you're using this wrapper 😄
 - Head over to [jdoodle](https://jdoodle.com/compiler-api) to get clientId and clientSecret.
 - Read the FAQs of the API [here.](https://docs.jdoodle.com/compiler-api/compiler-api)

#### Facing any Issue?
 - Feel free to [create an issue.](https://github.com/Prince2347X/pydoodle/issues/new)
