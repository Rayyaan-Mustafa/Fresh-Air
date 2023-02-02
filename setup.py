from distutils.core import setup

setup(name='FreshAir',
      version='0.4',
      py_modules=['FreshAir'],
      author='Rayyaan Mustafa',
      description='Need some fresh air? Get instant access to the weather in your command line!',
      install_requires=['requests'],
      entry_points={
        'console_scripts': [
            'FreshAir=FreshAir:main',
        ],}
      )
      