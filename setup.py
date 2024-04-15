from setuptools import find_packages, setup

setup(
    name="pr_horizen",
    packages=find_packages(exclude=["pr_horizen_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
