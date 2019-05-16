# python-restapi-example
An small example of a RESTful API using Python 3 and the Bottle web framework.

## Development
* Python 3.x
* Virtualenv (optional)

## Dependencies
* [bottle](https://bottlepy.org/docs/dev/index.html)
* [unittest](https://docs.python.org/3.5/library/unittest.html)
* [unittest-xml-reporting](https://github.com/xmlrunner/unittest-xml-reporting)
* [WebTest](http://webtest.pythonpaste.org/en/latest)

To ensure the dependencies are installed, run `pip` as follows from the root folder of the project;

```bash
pip install -r dependencies.txt
```

## Sample end points

```
/v1/hello/<name>
```