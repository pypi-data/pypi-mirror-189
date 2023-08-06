from setuptools import setup, Command
class InstallTestDependencies(Command):
    user_options = []
    def run(self):
        import sys
        import subprocess
        if self.distribution.tests_require: subprocess.check_call([sys.executable, "-m", "pip", "install", "-q"]+['pytest>=3.0', 'reahl-tofu', 'reahl-stubble', 'reahl-dev', 'reahl-webdev', 'reahl-browsertools', 'reahl-postgresqlsupport'])

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

setup(
    name='reahl-domain',
    version='6.1.1',
    description='End-user domain functionality for use with Reahl.',
    long_description='Reahl is a web application framework that allows a Python programmer to work in terms of useful abstractions - using a single programming language.\n\nThis Reahl component includes functionality modelling user accounts, some simple workflow concepts and more. ',
    url='http://www.reahl.org',
    maintainer='Iwan Vosloo',
    maintainer_email='iwan@reahl.org',
    packages=['reahl', 'reahl.domain', 'reahl.domain_dev', 'reahl.messages'],
    py_modules=[],
    include_package_data=True,
    namespace_packages=['reahl', 'reahl.messages'],
    install_requires=['reahl-component>=6.1,<6.2', 'reahl-mailutil>=6.1,<6.2', 'reahl-sqlalchemysupport>=6.1,<6.2', 'reahl-web-declarative>=6.1,<6.2', 'passlib>=1.7.1,<1.7.9999'],
    setup_requires=['pytest-runner', 'reahl-component-metadata', 'setuptools >= 51.0.0, <= 62.1.0', 'setuptools-git >= 1.1', 'toml', 'wheel'],
    tests_require=['pytest>=3.0', 'reahl-tofu', 'reahl-stubble', 'reahl-dev', 'reahl-webdev', 'reahl-browsertools', 'reahl-postgresqlsupport'],
    extras_require={},
    cmdclass={'install_test_dependencies': InstallTestDependencies}
)
