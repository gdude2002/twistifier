from setuptools import setup

setup(
    name='twistifier',
    version='0.0.2',
    packages=[
        'twistifier',
        'twistifier.client',
        'twistifier.common',
        'twistifier.examples',
        'twistifier.server'
    ],
    url='https://github.com/gdude2002/twistifier',
    license='Artistic License 2.0',
    author='Gareth Coles',
    author_email='gdude2002@gmail.com',
    description='Twisted protocol for the Minecraft Votifier protocol',
    install_requires=['twisted', 'rsa', 'pyasn1'],
    requires=['twisted', 'rsa', 'pyasn1'],
    provides=['twistifier']
)
