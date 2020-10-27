from setuptools import setup

setup(
    name='noby',
    version='1.0.0',
    author='Sakai, Masashi',
    author_email='masashi.sakai1986@gmail.com',
    url='https://github.com/massakai/koisuru_program',
    packages=['noby', ],
    entry_points={
        'console_scripts': [
            'proto = noby.cui:main',
        ]
    }
)
