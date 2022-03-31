# MarketPlace User Docs

To access the documentation, please visit: [https://materials-marketplace.readthedocs.io/en/latest/](https://materials-marketplace.readthedocs.io/en/latest/).

## Local Rendering

### HTML

A server will start, generate the docs and listen for changes in the source files.
This can be done by using docker or installing the development environment directly on the you machine.
Next are installation guides for Docker and Linux OS.

#### Docker

First, build the Docker image by running the following command:

```shell
$ docker build -f local_build.Dockerfile -t mp-docs .
```

Then, start the program by running:

```shell
$ docker run --rm -v $PWD:/app -p 8000:8000 mp-docs
```

#### Linux

At an OS level (these commands work on Linux Debian):

```shell
$ sudo apt install pandoc graphviz default-jre
$ sudo apt-get install texlive-latex-recommended \
                       texlive-latex-extra \
                       texlive-fonts-recommended \
                       latexmk
```

The python dependencies:

```shell
$ pip install -r requirements.txt
```

Now you can start the server and render the docs:

```
$ sphinx-autobuild docs/source docs/build/html
```

The documentation will be available on [`http://127.0.0.1:8000`](http://127.0.0.1:8000).

### PDF (LaTeX)

To generate a PDF of the documentation, simply run (from the root project folder):

```sh
make -C docs latexpdf
```

The generated PDF can be found under docs/build/latex/marketplace_docs.pdf

## Contributing

We use [pre-commit](https://pre-commit.com/) for running some code formatting tasks.
Follow the [installation instructions](https://pre-commit.com/#install) to set it up in your system.
