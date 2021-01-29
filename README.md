# Locker
Application created in Python 3 to protect folders and files in a specific directory on **Windows OS**.

# Getting Started
Install all dependencies using the command below on the terminal:
```
$ pip install -r requirements.txt
```
To create an executable, install the [PyInstaller](https://pypi.org/project/pyinstaller/) package and run the command below:
```
$ pyinstaller app.py -F
```

# Basic Usage:

**1.** Register your password.
```
$ app.py <your_password>
```

**2.** Using the argument `-r`, register the directory you want to lock and a namespace for it.
```
$ app.py <your_password> <namespace> -r "<directory>"
```

**3.** To lock the folder, enter your password and directory namespace using the argument `-l`.
```
$ app.py <your_password> <namespace> -l
```

**4.** Use the argument `-u` to unlock the folder.
```
$ app.py <your_password> <namespace> -u
```

Type `app.py -h` in terminal for more information about the program.
