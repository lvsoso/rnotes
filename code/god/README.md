[https://last9.io/blog/using-golang-package-in-python-using-gopy/](https://last9.io/blog/using-golang-package-in-python-using-gopy/)

```shell
go install github.com/go-python/gopy@latest
pip3 install pybindgen wheel
gopy build --output=py_god -vm=python3 .

#setup.py

python3 setup.py bdist_wheel
```