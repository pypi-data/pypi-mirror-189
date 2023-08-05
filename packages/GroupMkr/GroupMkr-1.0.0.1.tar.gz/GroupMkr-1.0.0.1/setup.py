from distutils.core import setup

try:
    import pypandoc
    long_description = pypandoc.convert_file('README.md', 'rst')
except(IOError, ImportError):
    long_description = open('README.md').read()

setup(
  name = 'GroupMkr',         # How you named your package folder (MyLib)
  packages = ['GroupMkr'],   # Chose the same as "name"
  version = '1.0.0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'GroupMkr is a module that simplifies creation of user groups and permissions in the terminal',   # Give a short description about your library
  long_description=long_description,
  long_description_content_type='text/markdown',
  author = 'Mezard Dini',                   # Type in your name
  author_email = 'mezardini@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/mezardini/GroupMkr.git',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/mezardini/GroupMkr/archive/refs/tags/1.0.0.1.tar.gz',    # I explain this later on
  keywords = ['Group', 'User Model', 'Django'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'django',
          
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
  
)



