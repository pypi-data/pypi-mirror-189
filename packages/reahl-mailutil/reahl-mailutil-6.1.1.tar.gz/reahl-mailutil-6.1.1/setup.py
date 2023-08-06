from setuptools import setup, Command
class InstallTestDependencies(Command):
    user_options = []
    def run(self):
        import sys
        import subprocess
        if self.distribution.tests_require: subprocess.check_call([sys.executable, "-m", "pip", "install", "-q"]+['pytest>=3.0', 'reahl-tofu', 'reahl-stubble', 'reahl-dev'])

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

setup(
    name='reahl-mailutil',
    version='6.1.1',
    description='Simple utilities for sending email from Reahl.',
    long_description='Reahl is a web application framework that allows a Python programmer to work in terms of useful abstractions - using a single programming language.\n\nReahl-mailutil is a simple library for sending emails (optionally from ReST sources). ',
    url='http://www.reahl.org',
    maintainer='Iwan Vosloo',
    maintainer_email='iwan@reahl.org',
    packages=['reahl', 'reahl.mailutil', 'reahl.mailutil_dev'],
    py_modules=[],
    include_package_data=False,
    namespace_packages=['reahl'],
    install_requires=['reahl-component>=6.1,<6.2', 'docutils>=0.14,<0.19.999', 'Pygments>=2.1.0,<2.13.999'],
    setup_requires=['pytest-runner', 'reahl-component-metadata', 'setuptools >= 51.0.0, <= 62.1.0', 'setuptools-git >= 1.1', 'toml', 'wheel'],
    tests_require=['pytest>=3.0', 'reahl-tofu', 'reahl-stubble', 'reahl-dev'],
    extras_require={},
    cmdclass={'install_test_dependencies': InstallTestDependencies}
)
