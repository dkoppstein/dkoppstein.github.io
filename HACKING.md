# Notes on the repo

There are now two separate repositories.

* root -> [davidkoppstein-source](http://github.com/dkoppstein/davidkoppstein-source)
* output -> [dkoppstein.github.io](http://github.com/dkoppstein/dkoppstein.github.io)

Remember to set `DELETE_OUTPUT_DIRECTORY = False`, otherwise the .git folder will get deleted in the output directory!

## Modified Makefile commands

`make env` ensures that a virtual environment is in place. NB: requires python3 executable. 

`make push` commits and pushes only the source.

`make github` does this push and also pushes output to dkoppstein.github.io.
