# poetry-aliases

[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/poetry-aliases?logo=python&logoColor=white&style=for-the-badge)](https://pypi.org/project/poetry-aliases)
[![PyPI](https://img.shields.io/pypi/v/poetry-aliases?logo=pypi&color=green&logoColor=white&style=for-the-badge)](https://pypi.org/project/poetry-aliases)
[![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/celsiusnarhwal/poetry-aliases?logo=github&color=orange&logoColor=white&style=for-the-badge)](https://github.com/celsiusnarhwal/poetry-aliases/releases)
[![PyPI - License](https://img.shields.io/pypi/l/poetry-aliases?color=03cb98&style=for-the-badge)](https://github.com/celsiusnarhwal/poetry-aliases/blob/main/LICENSE)
[![Code style: black](https://aegis.celsiusnarhwal.dev/badge/black?style=for-the-badge)](https://github.com/psf/black)

poetry-aliases is a [Poetry](https://python-poetry.org/) plugin that enables the creation of aliases for Poetry 
commands.

## Installation

```bash
poetry self add poetry-aliases
```

## Usage

First, add aliases via `poetry aliases`.

```bash
poetry aliases
```

`poetry aliases` will open a file in `$EDITOR` where you can view, add, and edit your aliases.

```toml
# Write each alias on a separate line, e.g.:

# i = "install"
# r = "remove"
# dev = "add --group dev"
# plugins = "self show plugins"

# Aliases that are not strings or conflict with other Poetry commands will be ignored.

# Save this file and close the editor when you're done.

i = "install"
r = "remove"
dev = "add --group dev"
plugins = "self show plugins"
```

Your aliases will be saved to Poetry's `config.toml` file.

Once your aliases have been saved, you can use them like any other Poetry command.

```bash
poetry i

# Installing dependencies from lock file

poetry r yapf

# Package operations: 0 installs, 0 updates, 1 removal

#  • Removing yapf (0.32.0)


poetry dev black

# Package operations: 3 installs, 0 updates, 0 removals

#  • Installing mypy-extensions (0.4.3)
#  • Installing pathspec (0.11.0)
#  • Installing black (23.1.0)


poetry plugins

#  • poetry-aliases (1.0.0) Create aliases for Poetry commands
#      1 application plugin
#
#      Dependencies
#        - click (>=8.1.3,<9.0.0)
#        - poetry (>=1.3.2,<2.0.0)
```

## License

poetry-aliases is licensed under the [MIT License](LICENSE.md).