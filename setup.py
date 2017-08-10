from setuptools import setup

setup(
    name='flaskr',
    packages=['flaskr'],
    include_paxkage_data=True,
    install_requires=[
        'flask',
    ],
    setup_requires=[
        'pytest-runner',
    ],
    tests_requires=[
        'pytest',
    ],
)