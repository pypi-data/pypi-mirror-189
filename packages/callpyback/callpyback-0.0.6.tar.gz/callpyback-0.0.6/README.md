# callpyback

[![Build Status](https://app.travis-ci.com/samuelgregorovic/callpyback.svg?branch=main)](https://app.travis-ci.com/samuelgregorovic/callpyback)
[![Coverage Status](https://coveralls.io/repos/github/samuelgregorovic/callpyback/badge.svg)](https://coveralls.io/github/samuelgregorovic/callpyback)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Features

- on_call callback
- on_success callback
- on_failure callback
- on_end callback
- default return
- using local variables of function in on_end
- support for async/sync callbacks with auto-detect
- support for omitting callback functions parameters with auto-detect
- pre-defining custom callback with creating class instance and using it as decorator
- TBD

### Instalation
`pip install callpyback`

### Usage

#### 1. ```CallPyBack``` callback class
```python
@CallPyBack(on_success=func_on_success, on_fail=func_on_fail, on_end=func_on_end)
def method()
    pass

method()
```
Will produce the same results as `callpyback` decorator. Can be extended further.

#### 2. Preconfigured ```CallPyBack``` callback custom class
```python
custom_callpyback = CallPyBack(
    on_success=func_on_success, on_fail=func_on_fail, on_end=func_on_end
)

@custom_callpyback
def method():
    pass

method()
```
Will produce the same results as `callpyback` decorator and `CallPyBack` class. Can be preconfigured to use specific callback functions with initiating a `CallPyBack` class instance.
