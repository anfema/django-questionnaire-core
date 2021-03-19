import os
import setuptools

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django-questionnaire-core",
    version="1.2.1",
    author="anfema GmbH",
    author_email="contact@anfe.ma",
    description="A django application which can be used as a base / starting point for questionnaire functionality in your project.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/anfema/django-questionnaire-core",
    packages=setuptools.find_packages(),
    classifiers=[
        "Framework :: Django :: 1.11",
        "Framework :: Django :: 2.0",
        "Framework :: Django :: 2.1",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    test_suite='runtests.run_tests',
    zip_safe=False,
)
