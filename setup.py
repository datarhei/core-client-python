from setuptools import find_packages, setup

install_requirements = [
    "httpx[http2]>=0.23.0",
    "pydantic>=1.10.2",
    "pydantic-collections>=0.3.0",
]
tests_requirements = [
    "coverage",
    "pre-commit",
    "pytest-cov",
    "pytest",
    "pytest-asyncio",
]

setup(
    name="core_client",
    version="1.2.0",
    url="https://github.com/datarhei/core-client-python",
    description="datarhei Core PyClient",
    author="FOSS GmbH",
    author_email="support@datarhei.com",
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: datarhei Core Development :: Libraries",
    ],
    keywords="datarhei core rest client http httpx asyncio pydantic",
    packages=find_packages(exclude=["tests*"]),
    setup_requires=["pytest-runner"],
    install_requires=install_requirements,
    tests_require=tests_requirements,
)
