from setuptools import setup, find_packages


setup(
    name='pysrec',
    version='1.0.0',
    license='MIT',
    author="Nandhan K",
    author_email='developer.nandhank@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='',
    keywords='python',
    install_requires=[
          'scikit-learn',
          'pyttsx3',
          'gtts',
          'playsound',
          'speech_recognition',
          'pipwin',
      ],

)