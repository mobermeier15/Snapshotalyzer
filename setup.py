from setuptools import setup

setup(
    name="Snapshotalyzer",
    version="0.1",
    author="Fred Obermeier",
    author_email="fred.obermeier@gmail.com",
    description="A tool to manage AWS EC2 snapshots",
    license="GPL 3",
    packages=['shotty'],
    url="https://github.com/mobermeier15/Snapshotalyzer",
    install_requires=[
        'click'
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        shotty=shotty.shotty:cli
    ''',
)