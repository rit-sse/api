# Development Guide

## Virtual Environment
### pipenv
This project uses [pipenv](https://pipenv.pypa.io/en/latest/) for virtual environment handling. Some useful commands:
- `pipenv install` - creates a virtual environment if needed and installs all packages
- `pipenv add <package>` - install a new package
- `pipenv run <command>` - run the given command inside the virtual environment
- `pipenv shell` - spawn a shell inside the virtual environment
#### Installation
It is reccomended to install pipenv with [pipx](https://pypa.github.io/pipx/). 

To install **pipx**, run `python3 -m pip install --user pipx`. You will then need to append `export PATH="$PATH:$HOME/.local/bin"` to your shell rc file (`~/.bashrc` for bash, `~/.zshrc` for zsh, etc.) and then source your rc file (`source ~/.bashrc`) to be able to run pipx. 

To install **pipenv**, run `pipx install pipenv`. To update pipenv, run `pipx upgrade pipenv`

## Code Format
### Black
This project uses [black](https://black.readthedocs.io/en/stable/) to ensure a consistent format for all source files within the project. Run `black .` to format all files, or `black path/to/file` to format a specific file.
#### Installation
It is reccomended to install black with [pipx](https://pypa.github.io/pipx/). 

To install **pipx**, run `python3 -m pip install --user pipx`. You will then need to append `export PATH="$PATH:$HOME/.local/bin"` to your shell rc file (`~/.bashrc` for bash, `~/.zshrc` for zsh, etc.) and then source your rc file (`source ~/.bashrc`) to be able to run pipx. 

To install **black**, run `pipx install black`. To update black, run `pipx upgrade black`
