# Python classnames

[![pypi](https://img.shields.io/pypi/v/classnames.svg)](https://pypi.org/project/classnames/)
[![python](https://img.shields.io/pypi/pyversions/classnames.svg)](https://pypi.org/project/classnames/)
[![Build Status](https://github.com/lucafaggianelli/python-classnames/actions/workflows/dev.yml/badge.svg)](https://github.com/lucafaggianelli/python-classnames/actions/workflows/dev.yml)
[![codecov](https://codecov.io/gh/lucafaggianelli/python-classnames/branch/main/graphs/badge.svg)](https://codecov.io/github/lucafaggianelli/python-classnames)

Utility to create CSS class strings from a multitude of values without poking around with string templates and lengthy logic.

## Show me the code!

```bash
pip install classnames
```

```python
from classnames import class_names

# render_button() -> "btn btn--red"
# render_button(rounded=True) -> "btn btn--rounded btn--red"
def render_button(rounded: bool = False, color = "red"):
    class_names("btn", f"btn--{color}", {
        "btn--rounded": rounded
    })
```

* Documentation: <https://lucafaggianelli.github.io/python-classnames>
* GitHub: <https://github.com/lucafaggianelli/python-classnames>
* PyPI: <https://pypi.org/project/python-classnames/>

## Features

* TODO

## Credits

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [waynerv/cookiecutter-pypackage](https://github.com/waynerv/cookiecutter-pypackage) project template.