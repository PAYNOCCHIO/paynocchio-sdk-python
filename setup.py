from setuptools import setup, find_packages


def readme():
  with open('README.md', 'r') as f:
    return f.read()


setup(
  name='paynocchio-sdk',
  version='0.0.1',
  author='Semyon Berezovsky',
  author_email='s.berezovsky@paynocchio.com',
  description='Paynocchio python SDK.',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='https://github.com/PAYNOCCHIO/paynocchio-api-alpha/tree/main',
  packages=find_packages(),
  install_requires=['requests>=2.31'],
  classifiers=[
    'Programming Language :: Python :: 3.11',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='paynocchio sdk wallet',
  project_urls={
    'GitHub': 'https://github.com/PAYNOCCHIO/paynocchio-api-alpha/tree/main'
  },
  python_requires='>=3.11'
)