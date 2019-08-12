# EComp
An Easy Way To Distribute Multiple Python Scripts Faster!

# ABOUT
EComp is very useful if you just don't like compiling over and over again or if you need python to work in a machine with no need of python being already installed. or you may need to work with python from other languages.

# USAGE
To use EComp, first compile it with python compilers like [Pyinstaller](https://www.pyinstaller.org) or [Nuitka](https://nuitka.net).

Then, either make a file under same directory with name of "c.e" and write the script you wish to compile or you can run the script with first argument being the name of script without `.py` and `.` instead of `/` and `\`.

example:

`./EComp my_script`

__NOTE__: Only scripts below or on same directory can be found and not above current directory!

And all you have to change in your normal scripts is to make a function called `comp`. This function will be run! Think of it as equivalent of `if __name__ == "__main__"`
