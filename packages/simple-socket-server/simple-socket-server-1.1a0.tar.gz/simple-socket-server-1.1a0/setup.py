from setuptools import setup

setup(name='simple-socket-server',
      version='1.1a',
      url='https://github.com/webtoucher/simple-socket-server',
      license='BSD-3-Clause',
      author='Alexey Kuznetsov',
      author_email='mirakuru@webtoucher.ru',
      description='Simple TCP socket server with select',
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'Topic :: Internet :: WWW/HTTP :: HTTP Servers',
          'License :: OSI Approved :: BSD License',
          'Programming Language :: Python :: 3',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: POSIX',
          'Operating System :: Unix',
          'Operating System :: MacOS',
      ],
      packages=['simple_socket_server'],
      long_description=open('README.md').read(),
      long_description_content_type='text/markdown',
      zip_safe=False)
