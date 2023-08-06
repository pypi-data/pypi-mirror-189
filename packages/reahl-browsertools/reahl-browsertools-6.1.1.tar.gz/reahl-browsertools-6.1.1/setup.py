from setuptools import setup, Command
class InstallTestDependencies(Command):
    user_options = []
    def run(self):
        import sys
        import subprocess
        if self.distribution.tests_require: subprocess.check_call([sys.executable, "-m", "pip", "install", "-q"]+['pytest>=3.0', 'reahl-tofu', 'reahl-stubble', 'reahl-doc', 'reahl-postgresqlsupport'])

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

setup(
    name='reahl-browsertools',
    version='6.1.1',
    description='An alternative API for working with Selenium and WebTest.',
    long_description='Reahl is a web application framework that allows a Python programmer to work in terms of useful abstractions - using a single programming language.\n\nReahl-browsertools provides an interface to Selenium WebDriver that simplifies tests that deal with ajax. It also includes programmatically composable XPaths that are easy to read in code. ',
    url='http://www.reahl.org',
    maintainer='Iwan Vosloo',
    maintainer_email='iwan@reahl.org',
    packages=['reahl', 'reahl.browsertools', 'reahl.browsertools_dev'],
    py_modules=[],
    include_package_data=True,
    namespace_packages=['reahl'],
    install_requires=['lxml>=4.2,<4.9.999', 'WebTest>=2.0,<3.0.999', 'selenium>=2.42,<4.7.9999'],
    setup_requires=['pytest-runner', 'reahl-component-metadata', 'setuptools >= 51.0.0, <= 62.1.0', 'setuptools-git >= 1.1', 'toml', 'wheel'],
    tests_require=['pytest>=3.0', 'reahl-tofu', 'reahl-stubble', 'reahl-doc', 'reahl-postgresqlsupport'],
    extras_require={},
    cmdclass={'install_test_dependencies': InstallTestDependencies}
)
