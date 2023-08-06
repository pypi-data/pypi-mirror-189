from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.readlines()

setup(
    name='openacli',
    version='0.1',
    description='OpenAI CLI Interface',
    url='https://github.com/cdrew3/openacli',
    author='Chris Drew',
    author_email='chris.drew.cd@gmail.com',
    license='MIT',
    zip_safe=False,
    packages=find_packages(),
    entry_points = {
        'console_scripts': [
            'oacli = openacli.openacli:main'
        ]
    },
    install_requires=requirements
)
