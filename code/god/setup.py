import setuptools

setuptools.setup(
    name="py_god",
    packages=setuptools.find_packages(include=["py_god"]),
    py_modules = ["py_god.god"],
    package_data={"py_god": ["*.so"]},
    include_package_data=True,
)