
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
    
REQUIREMENTS = ["numpy", "chumpy", "opencv-python"]

setuptools.setup(
     name='star',  
     version='0.0.1',
     author="Ahmed A. A. Osman",
     author_email="ahmed.osman@tuebingen.mpg.de",
     install_requires=REQUIREMENTS,
     description="STAR: Sparse Trained Articulated Human Body Regressor",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/ahmedosman/STAR",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 2",
         "Programming Language :: Python :: 3",
         "License :: Other/Proprietary License",
         "Operating System :: OS Independent",
     ],
     

 )
