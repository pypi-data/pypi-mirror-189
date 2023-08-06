from setuptools import find_packages, setup

setup(
    name="PygameBuiltins",
    packages=find_packages(include=["PygameBuiltins"]),
    version="0.1.0",
    description="A pygame wrapper with usefull classes and functions.",
    author="MrCatNerd#0669",
    license="MIT",
    install_requires=["pygame"],
    setup_requires=["pytest-runner"],
    tests_require=["pytest==4.4.1"],
    test_suite="tests",
)
