from setuptools import setup, Command
class InstallTestDependencies(Command):
    user_options = []
    def run(self):
        import sys
        import subprocess
        if self.distribution.tests_require: subprocess.check_call([sys.executable, "-m", "pip", "install", "-q"]+['pytest>=3.0'])

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

setup(
    name='reahl-stubble',
    version='6.1.1',
    description='Stub tools for use in unit testing',
    long_description='Reahl is a web application framework that allows a Python programmer to work in terms of useful abstractions - using a single programming language.\n\nStubble (a part of the Reahl development tools) is a collection of tools for writing stubs in unit tests. Stubble can be used independently of the Reahl web framework.\n\nUsing stubs allows one to decouple one unit test from real code unrelated to it - you write a fake class to take the place of a real one (which this test is not testing).\n\nStubble ensures, however, that the test will break should the interface of the stub differ from that of the real class it is a stub for. ',
    url='http://www.reahl.org',
    maintainer='Iwan Vosloo',
    maintainer_email='iwan@reahl.org',
    packages=['examples', 'reahl', 'reahl.stubble', 'reahl.stubble_dev'],
    py_modules=[],
    include_package_data=False,
    namespace_packages=['reahl'],
    install_requires=['setuptools>=51.0.0'],
    setup_requires=['pip >= 21.1', 'pytest-runner', 'reahl-component-metadata', 'setuptools >= 51.0.0, <= 62.1.0', 'setuptools-git >= 1.1', 'toml', 'wheel'],
    tests_require=['pytest>=3.0'],
    extras_require={},
    cmdclass={'install_test_dependencies': InstallTestDependencies}
)
