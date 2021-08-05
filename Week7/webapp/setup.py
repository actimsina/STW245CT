from setuptools import setup, find_packages

setup(
    name="245_XSSTrainer",
    author="Dan Goldsmith",
    author_email="djgoldsmith@googlemail.com",
    version="0.0.2",
    packages=find_packages(),
    include_package_data=True,
    install_requires = ["selenium",
                        "requests",
                        "flask-redis",
                        "jinja-markdown"]

)
