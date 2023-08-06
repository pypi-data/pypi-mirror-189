import codecs
import os
import setuptools


def local_file(file):
    return codecs.open(
        os.path.join(os.path.dirname(__file__), file), 'r', 'utf-8'
    )

setuptools.setup(
    name="faqs_google_results",
    version="1.0",
    author="Dídac Anton, LE Van Tuan",
    author_email="dinerofacil.x.paypal@gmail.com",
    packages=setuptools.find_packages(),
    long_description=local_file('README.md').read(),
    long_description_content_type="text/markdown",
    url="",
    classifiers=[
	"Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
        "Development Status :: 5 - Production/Stable",
        "Operating System :: MacOS",
        "Operating System :: Microsoft",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Typing :: Typed",
    ],
    install_requires=[
        "beautifulsoup4",
        "requests",
        "jinja2",
    ],
    python_requires=">=3.6"
)