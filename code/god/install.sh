gopy build --output=py_god -vm=python3 .
python setup.py bdist_wheel
pip install dist/py_god-0.0.0-py3-none-any.whl