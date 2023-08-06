from setuptools import setup
setup(
    name='vpitools',
    version='0.1.2',
    description='Testing installation of First Package',
    url='https://vpi.pvn.vn/',
    author='DnA Teams',
    author_email='dna.teams@vpi.pvn.vn',
    license='MIT',
    packages=['vpitools'],
    zip_safe=False,
    install_requires=['matplotlib', 'seaborn', 'plotly', 'altair', 
                      'numpy', 'pandas',
                      ]
)
