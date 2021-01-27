from setuptools import setup, find_packages
from os.path import abspath, dirname, join

README_MD = open(join(dirname(abspath(__file__)), "README.md")).read()

setup(
    name = "robotframework-netaddr",
    version = "0.0.1",
    author = "Niels Keulen",
    author_email = "nkeulen@gmail.com",
    packages = find_packages(include=["robotframework_netaddr"], exclude=["tests"]),
    include_package_data=True,
    description = "Robotframework keyword for the python netaddr library",
    long_description = README_MD,
    long_description_content_type = "text/markdown",
    url = "https://github.com/nkeulen/robotframework-netaddr",
    classifiers = [
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3 :: Only",
        "Framework :: Robot Framework",
        "Framework :: Robot Framework :: Library",
        "Topic :: System :: Networking",
        "Topic :: Software Development :: Testing",
        "Topic :: Software Development :: Testing :: Acceptance"
    ],
    keywords = "netaddr, robotframework, ip address, ipv4, ipv6, mac address, network",
    install_requires = ["netaddr"],
    python_requires='>=3.5'
)

