# Control M REST API package

This is package for rest service for Control M, if you wanna know more about the Control M, please visit http://www.bmcsoftware.com.au/it-solutions/control-m.html

## Cores
All the api endpoints are managed by core.py sits under /controlm-rest-api/library

To initiate the class CoreAPI, you will need the `username`, `password`, and `controlM server url`


make the tar.gz file
`python setup.py sdist bdist_wheel`

upload the package
`twine upload  --repository-url https://test.pypi.org/legacy/ dist/*`
`twine upload dist/*`

