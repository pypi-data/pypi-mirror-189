# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cppygen']

package_data = \
{'': ['*']}

install_requires = \
['clang>=14.0,<15.0',
 'colorlog>=6.7.0,<7.0.0',
 'pytest>=7.1.3,<8.0.0',
 'toml>=0.10.2,<0.11.0']

entry_points = \
{'console_scripts': ['cppygen = cppygen.__main__:run']}

setup_kwargs = {
    'name': 'cppygen',
    'version': '0.1.4',
    'description': 'A simple c++ code generator for pybind11',
    'long_description': '# CPPYGEN\n\nAutomatic code generation for pybind11.\n\nPybind11 is a powerful library that exposes C++ types in Python and vice versa, \n\nThis generator will be generate c++ code for pybind11, and make it easy to\nwrite a python module using c++.\n\n## Installation\n```\npip install cppygen\n```\n\n## Usage Guide\n\nAfter installing cppygen, you can use `cppygen` command.\n\n```\ncppygen --config_file /path/to/cppygenconfig.toml --cwd /path/to/cwd\n```\n\nThis command will load config file, and parse C++ code and generate\nC++ pybind11 Code.\n\nAfter generating the code. Include the generated header to your program and\njust write in pybind11 manner. Be sure to link the generated cpp code.\n\n```cpp\nPYBIND11_MODULE(pyshell, m) {\n  CPPyGen::CPPyGenExport(m);\n}\n```\n\n### CMake\n\nUse `add_custom_command` to auto generate.\n\n```cmake\nset(cppygen_generated_hpp ${CMAKE_CURRENT_BINARY_DIR}/cppygen_generated.hpp)\nset(cppygen_generated_cpp ${CMAKE_CURRENT_BINARY_DIR}/cppygen_generated.cpp)\n\nfind_program(_CPPYGEN_GENERATOR cppygen)\n\nadd_custom_command(\n  OUTPUT ${cppygen_generated_hpp} ${cppygen_generated_cpp}\n  COMMAND\n    ${_CPPYGEN_GENERATOR} ARGS #\n    --config_file ${CMAKE_CURRENT_LIST_DIR}/cppygenconfig.toml #\n    --cwd ${CMAKE_CURRENT_LIST_DIR}\n  DEPENDS ${SHELL_SOURCES}\n  COMMENT\n    "Generating CPPyGen Code To ${cppygen_generated_hpp} and ${cppygen_generated_cpp}"\n  VERBATIM)\n```\n\n## Config\n`cppygen` command does not work without configuration.\nUse toml format configuration file.\n\n**sources** [array of path, **required**]\nPaths with `cppygen` will parse. `cppygen` can extract functions from\nsources.\n\n**headers** [array of path, **required**]\nPaths with `cppygen` will parse.`cppygen` can extract structs or classes from\nheaders.\n\n**output_dir** [path, **required**]\nOutput directory of generated code.\n\n**search_namespace** [string, optional]\nDefault is "cppygen", this option will define the namespace witch\nwill be parsed by `cppygen`. Outside of this namespace would be ignored.\n\n**include_headers** [array of filename, optional]\n`cppygen` does not resolve include paths, thus if you want to export C++\nclasses you should specify include filenames.\n\n**include_directories** [array of dir, optional]\nThese directories will be passed as absolute paths to parser include flags.\nSame as `flags =["-I/abs_path/to/dir"]`\n\n**flags** [array of string, optional]\nParser compile options.\n\n**libclang_path** [path, optional]\nPath to `libclang` shared library.\n\n## Examples\nSee the `examples` directry for sample projects.\n\n### Function\n```cpp\nnamespace cppygen {\n/**\n * pyname: py_foo\n * description: some description\n **/\nvoid foo() {\n\n}\n\n}\n```\nThis function will export to python as "py_foo".\n`description` would be python docstring.\n\n\n## Env\n\n```bash\nPYGEN_LIBCLANG_PATH # Path to clang shared library\nPYGEN_COMPILE_FLAGS # additional flags to parse file\n```\n',
    'author': 'Gen740',
    'author_email': 'keener_slimier_0m@icloud.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
