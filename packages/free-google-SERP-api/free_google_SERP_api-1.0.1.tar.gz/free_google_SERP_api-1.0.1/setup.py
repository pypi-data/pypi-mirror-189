import codecs
import os
import setuptools


def local_file(file):
    return codecs.open(
        os.path.join(os.path.dirname(__file__), file), 'r', 'utf-8'
    )

setuptools.setup(
    name="free_google_SERP_api",
    version="1.0.1",
    author="Dídac Anton",
    author_email="",
    website="https://twitter.com/seo_torch",
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
        "requests",
        "urllib",
        "pandas",
        "numpy",
        "requests_html",
        "faqs_google_results",
    ],
    python_requires=">=3.6"
)