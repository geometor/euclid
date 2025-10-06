## src/geometor/euclid/__init__.py

```py
"""
euclid
======

PHOTON platform
---------------



"""
__author__ = "PHOTON platform"
__maintainer__ = "PHOTON platform"
__email__ = "github@phiarchitect.com"
__version__ = "0.0.1"
__licence__ = "MIT"

```

## src/geometor/euclid/__main__.py

```py
"""The package entry point into the application."""

from .app import run

if __name__ == "__main__":
    run()
```

## src/geometor/euclid/app.py

```py
"""
run the main app
"""
from .euclid import Euclid


def run() -> None:
    reply = Euclid().run()
    print(reply)

```

## src/geometor/euclid/euclid.py

```py
"""
euclid
"""
```

