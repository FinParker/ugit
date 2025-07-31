# ugit

## use venv

```bash
python -m venv venv

# Windows(PowerShell)
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
venv\Scripts\activate

# Unix/MacOS
source venv/bin/activate
```

## develop

```bash
pip install -e .
```

## usage

```bash
ugit --help
```

## example

```bash
ugit --debug init

ugit --debug hash-object <file>

ugit --debug cat-file <object>
```

## notes

In Git's lingo a "tree" means a directory.

## tree object
A tree object is a ugit object that represents a directory.

