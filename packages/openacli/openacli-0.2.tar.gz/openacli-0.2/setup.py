from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.readlines()

with open('README.md') as f:
    long_desc = f.read()

setup(
    name='openacli',
    version='0.2',
    description='OpenAI CLI Interface',
    long_description=long_desc,
    long_description_content_type='text/markdown',
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
