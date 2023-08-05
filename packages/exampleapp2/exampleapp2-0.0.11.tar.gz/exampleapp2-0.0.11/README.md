
Note: write your logic code in `exampleapp` directory then write your tests file in `tests` directory.
Note: you have to choose suitable package_name because of test.pypi won't accept any repeated package_name.
Note: replace exist links in `project_urls` in `setup.py` with your own links.
Note: fill `requirements.txt` with dependencies that your package need.

## Local Install

Before uploading our package to PyPI we can confirm that our package can be installed via pip install by navigating to our package directory and entering:

```bash
pip install .
```
or 
```bash
pip install -e .
```
if you want make it editable.

This should then install our package like any other package install via pip:



## Build
Once we’ve written our code files, setup configuration, and tested the install — we’re ready to build our package distribution.

The build process creates a new directory `dist` which will contain a `.tar.gz` and `.whl` file — this is what we need to publish our package to PyPI.

To build our `dist` files, we use a tool creatively named `build`. First, we type:
```bash
pip install build
```
then, while in our package directory — type:

```bash
python -m build
```

Once this is complete, we should find a new /dist directory inside our package directory.


## Publish to TestPyPI
Finally, we are ready to publish our new Python package! Again, we make use of another package called `twine`. We install this with:

```bash
pip install twine
```

Once installed, we upload to TestPyPI — a ‘test’ version of PyPI so that we can double-check that we have set everything up correctly. We do this by typing:

```bash
python -m twine upload --repository testpypi dist/*
```

At this point, we’ll need to login to TestPyPI — if you don’t have an account, sign up for one [here](https://test.pypi.org/account/register/). If everything is set up correctly, our package will be uploaded:


Now, we can test that our new package works through another pip install — but this time from TestPyPI:

```bash
pip install -i https://test.pypi.org/simple/ exampleapp
```

(If you find that the package is already installed — just `pip uninstall exampleapp`).


## PyPI
Once we’ve confirmed that the package works — we take our final step, publishing to PyPI. Again, you’ll need to register [here](https://pypi.org/account/register/).

Next, we upload our package to PyPI with:
```bash
python -m twine upload --repository pypi dist/*
```


And we’re done!


That’s our first Python package deployment — it’s surprisingly straightforward. We can go ahead and `pip install exampleapp` to use the package.