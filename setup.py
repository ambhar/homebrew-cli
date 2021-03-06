import setuptools

setuptools.setup(
     name='add_cli',  
     version='0.1',
     scripts=['add_cli.py'] ,
     author="amol",
     author_email="amol@snakescript.com",
     description="A Docker and AWS utility package",
    long_description_content_type="text/markdown",
     url="https://github.com/ambhar/homebrew-cli",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
