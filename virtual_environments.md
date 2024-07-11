pip -- Is the package manager that installs and updates packages
venv -- allows you to manage separate package installations for different projects 

Reference: https://docs.python.org/3/tutorial/venv.html 

Python applications will often use packages and modules that don’t come as part of the standard library. Applications will sometimes need a specific version of a library, because the application may require that a particular bug has been fixed or the application may be written using an obsolete version of the library’s interface.

This means it may not be possible for one Python installation to meet the requirements of every application. If application A needs version 1.0 of a particular module but application B needs version 2.0, then the requirements are in conflict and installing either version 1.0 or 2.0 will leave one application unable to run.

The solution for this problem is to create a virtual environment, a self-contained directory tree that contains a Python installation for a particular version of Python, plus a number of additional packages.

A virtual environment is a built-in way to create an environment. A virtual environment creates a folder that contains a copy (or symlink) to a specific interpreter. When you install packages into a virtual environment it will end up in this new folder, and thus isolated from other packages used by other workspaces.

An "environment" in Python is the context in which a Python program runs that consists of an interpreter and any number of installed packages.

The module used to create and manage virtual environments is called venv. venv will install the Python version from which the command was run 

To create a virtual environment, decide upon a directory where you want to place it, and run the venv module as a script with the directory path:

`python -m venv tutorial-env`

This will create the tutorial-env directory if it doesn’t exist, and also create directories inside it containing a copy of the Python interpreter and various supporting files.

Once you’ve created a virtual environment, you may activate it.
`source tutorial-env/bin/activate`

To deactivate a virtual environment, type:

`deactivate`

You can install, upgrade, and remove packages using a program called pip. By default pip will install packages from the Python Package Index. You can browse the Python Package Index by going to it in your web browser.

pip has a number of subcommands: “install”, “uninstall”, “freeze”, etc. (Consult the Installing Python Modules guide for complete documentation for pip.)

You can install the latest version of a package by specifying a package’s name:
`(tutorial-env) $ python -m pip install novas`



You can also install a specific version of a package by giving the package name followed by == and the version number:

`python -m pip install requests==2.6.0`

You can supply a different version number to get that version, or you can run python -m pip install --upgrade to upgrade the package to the latest version:

`$ python -m pip install --upgrade requests`


python -m pip uninstall followed by one or more package names will remove the packages from the virtual environment.

python -m pip show will display information about a particular package:
`(tutorial-env) $ python -m pip show requests`

`python -m pip list` will display all of the packages installed in the virtual environment:

python -m pip freeze will produce a similar list of the installed packages, but the output uses the format that python -m pip install expects. A common convention is to put this list in a requirements.txt file:

`python -m pip freeze > requirements.txt`

The requirements.txt can then be committed to version control and shipped as part of an application. Users can then install all the necessary packages with install -r:

`(tutorial-env) $ python -m pip install -r requirements.txt`
pip -- Is the package manager that installs and updates packages
venv -- allows you to manage separate package installations for different projects 

command + shift + P -> python create environment
command + shift + P -> Select Interpreter

python3 -m venv .venv