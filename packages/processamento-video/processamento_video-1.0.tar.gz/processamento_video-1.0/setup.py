from setuptools import setup,find_packages
from pathlib import Path


setup(
    name='processamento_video',
    version=1.0,
    description='Este pacote irá fornecer ferramentas de processamento de vídeo',
    long_description=Path('README.md').read_text(),
    author='DJalme',
    author_email='dj@hotmail.com',
    keywords=['camera', 'video', 'processamento'],
    packages=find_packages()
)