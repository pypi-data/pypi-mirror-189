from setuptools import setup, Command
class InstallTestDependencies(Command):
    user_options = []
    def run(self):
        import sys
        import subprocess
        if self.distribution.tests_require: subprocess.check_call([sys.executable, "-m", "pip", "install", "-q"]+['pytest>=3.0', 'reahl-tofu', 'reahl-stubble'])

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

setup(
    name='reahl-commands',
    version='6.1.1',
    description='The component framework of Reahl.',
    long_description='Reahl is a web application framework that allows a Python programmer to work in terms of useful abstractions - using a single programming language.\n\nReahl-commands contains useful command line commands for reahl components. ',
    url='http://www.reahl.org',
    maintainer='Iwan Vosloo',
    maintainer_email='iwan@reahl.org',
    packages=['reahl', 'reahl.commands'],
    py_modules=[],
    include_package_data=False,
    namespace_packages=['reahl'],
    install_requires=['reahl-component>=6.1,<6.2'],
    setup_requires=['pytest-runner', 'reahl-component-metadata', 'setuptools >= 51.0.0, <= 62.1.0', 'setuptools-git >= 1.1', 'toml', 'wheel'],
    tests_require=['pytest>=3.0', 'reahl-tofu', 'reahl-stubble'],
    extras_require={},
    cmdclass={'install_test_dependencies': InstallTestDependencies}
)
