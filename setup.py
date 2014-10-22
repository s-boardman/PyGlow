from distutils.core import setup

classifiers = ['Development Status :: 4 - Beta',
               'Operating System :: POSIX :: Linux',
               'License :: OSI Approved :: MIT License',
               'Intended Audience :: Developers',
               'Programming Language :: Python :: 2.6',
               'Programming Language :: Python :: 2.7',
               'Programming Language :: Python :: 3',
               'Topic :: Software Development',
               'Topic :: System :: Hardware']

setup(name= 'PyGlow',
      version= '0.5',
      author= 'Ben',
      author_email= 'ben@email.goes.here',
      description= 'A module to control the PiGlow Raspberry Pi Addon Board',
      long_description= 'A module to control the PiGlow Raspberry Pi Addon Board',
      license= 'MIT',
      keywords= 'Raspberry Pi PiGlow',
      url= 'https://github.com/benleb/PyGlow',
      classifiers = classifiers,
      py_modules= ['PyGlow'],
      install_requires= ['rpi.gpio >= 0.5.4']
)
