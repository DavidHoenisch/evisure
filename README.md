# Evisure

_stupid simple hashing utility that can walk a directory tree_

## Installation

You can just git clone the repo and give relative paths to everything, however, below I provide a more convenient method


### Prerequisites

- Python3
- git
- virtualenv

### Setting up

Create a .local directory. Should exist already, but just in case...
```bash
mkidr ~/.local/bin/
```

Clone the report into `~/.local/bin`
```bash
git clone https://github.com/DavidHoenisch/evisure.git ~/.local/bin/evisure
```

Create virtualenv for script. Not required, just is nice if you have other python3 utilities you use.
```bash
virtualenv ~/.local/bin/evisure/env
```

Add an alias to your .bashrc (or .zshrc) file.
```bash
echo "alias get_hashed='~/.local/bin/evisure/env/bin/python3 ~/.local/bin/evisure/get_hashed.py" >> ~/.bashrc && source ~/.bashrc
```

Configured this way, you can run `get_hashed` from anywhere in a file system on you local machine.

## Updates

from time to time, this utility may receive updates. To update the utility, 
cd into `~/.local/bin/evisure/` and run:

```bash
git pull
```
