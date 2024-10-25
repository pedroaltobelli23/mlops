# Documentation

## Sphinx

1. Install Sphinx

```Bash
pip install sphinx==7.2.6
```

2. Create a docs folder and inside it use the command:

```Bash
sphinx-quickstart
```

warning: Separate source and build directories (y/n) [n]: n

3. make html documentation file:

```Bash
make html
```

4. Create a src folder in the root folder and paste the following content into src/spectral.py:

```Python
"""
Spectral Clustering Module

This is a sample module to demonstrate autodoc
"""


class SpectralClustering:
    """
    SpectralClustering Class

    Does spectral clustering.
    """

    def train(self):
        """Class method to train the model"""
        pass


def my_func():
    """Module function example"""
    pass
```

5. In the docs/conf.py file:

```Python
import sys
import os

sys.path.insert(0, os.path.abspath("../src"))

extensions = ["sphinx.ext.autodoc"]
```

6. Then go to the folder docs and run the comand to create ***reSctructuredText*** for our Python modules

```Bash
sphinx-apidoc -o ./ ../src/
```

7. Rebuild it to see the new version

```Bash
make html
```

8. Install a new theme:

```Bash
pip install sphinx_rtd_theme
```

9. Then, change html_theme variable in the docs/config.py file from html_theme = "alabaster" to html_theme = "sphinx_rtd_theme". Rebuild the project