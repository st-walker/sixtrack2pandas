from setuptools import setup, find_packages


setup(
    name="sixtrack2pandas",
    version="0.1",
    packages=find_packages(exclude=["docs", "tests", "obsolete"]),
    install_requires=["pandas"],
    python_requires="==2.7.*",
    author="Stuart Walker",
    author_email="stuartwalker1992@gmail.com",
    description="Load SixTrack output with pandas.",
    url="https://github.com/st-walker/sixtrack2pandas",
    license="MIT",
    keywords="sixtrack accelerator pandas",
)

