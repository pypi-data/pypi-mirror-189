from setuptools import setup

requirements = ["gitpython"]
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name="LRFutils",
    version = "0.1.0",
    description = 'Just a custom library to share with some colleagues. Use it at your own risks.',
    author = 'Leirof',
    author_email = 'vince.lrf@gmail.com',
    url = 'https://github.com/LeiRoF/Utils',
    packages=['LRFutils'],
    install_requires=requirements,
    python_requires='>=3.7.0',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Intended Audience :: Developers'
    ]
)