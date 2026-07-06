from pathlib import Path

from setuptools import find_packages, setup

long_description = Path(__file__).with_name("README.md").read_text(encoding="utf-8")

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
    version="2.10.1",
    url="https://github.com/datarhei/core-client-python",
    project_urls={
        "Source": "https://github.com/datarhei/core-client-python",
        "Changelog": "https://github.com/datarhei/core-client-python/blob/main/CHANGELOG.md",
        "Issues": "https://github.com/datarhei/core-client-python/issues",
    },
    description="datarhei MediaCore Python client",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    author="livespotting GmbH",
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
