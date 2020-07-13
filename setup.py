import setuptools


packages = setuptools.find_namespace_packages(
)

setuptools.setup(
    entry_points={
        'console_scripts': [
            'mustup-mbp = mustup.mbp.cli.main:entry_point',
        ],
    },
    name='mustup_mbp',
    packages=packages,
    python_requires='>= 3.8',
    version='0.1',
    zip_safe=False, # due to namespace package
)
