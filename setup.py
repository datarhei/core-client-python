from setuptools import find_packages, setup

install_requirements = [
    "httpx[http2]>=0.23.0",
    "pydantic>=2",
    "PyJWT>=1.7.1",
]
tests_requirements = [
    "coverage",
    "pre-commit",
    "pytest-cov",
    "pytest",
    "pytest-asyncio",
]

setup(
    name="datarhei-mediacore-client",
    version="16.20.0",
    url="https://github.com/datarhei/core-client-python",
    description="datarhei MediaCore Python client",
    author="FOSS GmbH",
    author_email="support@datarhei.com",
    classifiers=[
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Topic :: datarhei Core Development :: Libraries",
    ],
    python_requires=">=3.11",
    keywords="datarhei mediacore core rest client http httpx asyncio pydantic",
    packages=find_packages(exclude=["tests*"]),
    setup_requires=["pytest-runner"],
    install_requires=install_requirements,
    tests_require=tests_requirements,
)
