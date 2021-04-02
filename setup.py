import setuptools
import re

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open('pydoodle/__init__.py') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)


with open("requirements.txt", "r") as req:
    requirements = req.read().splitlines()

setuptools.setup(
    name="pydoodle",
    version=version,
    author="Prince2347X",
    author_email="prince.raj29042004@gmail.com",
    description="An API wrapper of Jdoodle.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Prince2347X/pydoodle",
    license="MIT",
    packages=setuptools.find_packages(),
    keywords=["compiler", "compiler api", "jdoodle", "jdoodle api", "pydoodle", "jdoodle python"],
    python_requires=">=3.5.1",
    install_requires=requirements,
    project_urls={
        "Source Code": "https://github.com/Prince2347X/pydoodle",
        "Issue Tracker": "https://github.com/Prince2347X/pydoodle/issues",
        "Documentation": "https://pydoodle.readthedocs.io/",
    },
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Compilers',
        'Topic :: Documentation :: Sphinx',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Natural Language :: English'
    ]

)
