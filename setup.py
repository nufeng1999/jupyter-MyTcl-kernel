from setuptools import setup

setup(name='jupyter_MyTcl_kernel',
      version='0.0.1',
      description='Minimalistic Tcl kernel for Jupyter',
      author='nufeng',
      author_email='18478162@qq.com',
      license='MIT',
      classifiers=[
          'License :: OSI Approved :: MIT License',
      ],
      url='https://github.com/nufeng1999/jupyter-MyTcl-kernel/',
      download_url='https://github.com/nufeng1999/jupyter-MyTcl-kernel/tarball/0.0.1',
      packages=['jupyter_MyTcl_kernel'],
      scripts=['jupyter_MyTcl_kernel/install_MyTcl_kernel'],
      keywords=['jupyter', 'notebook', 'kernel', 'makefile','rs'],
      include_package_data=True
      )
