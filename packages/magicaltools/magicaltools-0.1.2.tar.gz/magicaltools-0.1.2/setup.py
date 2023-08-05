from setuptools import setup,find_packages

with open("README.md","r",encoding="utf-8") as fh:
    long_description = fh.read()

setup(name='magicaltools',
      version='0.1.2',
      description='magicaltools lib',
      long_description=long_description,
      long_description_content_type='text/markdown',
    #   install_requires = ['tktkrs'],
      classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
      url='https://gitee.com/w-8/tktk',
      author='bili:凿寂',
      author_email='mdzzdyxc@163.com',
      license='MIT',
      packages=find_packages(),
      zip_safe=True
     )
#python3 setup.py sdist bdist_wheel
#python3 -m twine upload dist/*