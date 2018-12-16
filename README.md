# LibTerm-Packages

[LibTerm](https://github.com/ColdGrub1384/LibTerm) has a package manager. You can submit your all commands by opening a pull request.

## Contributing

All commands are written in Python 3.7. For submitting your command (you can only submit commands), you have to put your main Python script and other modules inside a zip file. The name of the command will be the name of the script.

### Example

**command_name.py**

```python
import amodule

print(amodule.str)
```

**amodule.py**

```python
str = "Hello World!"
```

The name of the command will be `command_name`. Zip all files into a zip file. The name of the zip file will be used for installing the package. If the file is called `command_name.zip`, the user can install the command by typing `package install command_name`.

Submit a pull request containing the zip file.
