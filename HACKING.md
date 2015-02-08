Makefile has been modified somewhat. `.PHONY` target "publish" now creates another target "env" which creates a virtual environment using requirements.txt.

Two separate repositories. Remember, set `DELETE_OUTPUT_DIRECTORY = False.` 

`make push` commits and pushes only the source.

`make github` does this push and also pushes output to dkoppstein.github.io.
