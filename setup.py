from setuptools import setup

setup(
    name='noby',
    version='1.0.0',
    author='Sakai, Masashi',
    author_email='masashi.sakai1986@gmail.com',
    url='https://github.com/massakai/koisuru_program',
    packages=['noby', ],
    install_requires=[
        'Pillow==8.0.0',
    ],
    package_data={
        'noby': ['bmps'],
    },
    entry_points={
        'console_scripts': [
            'proto = noby.cui:main',
            'noby = noby.gui:main',
        ]
    }
)
