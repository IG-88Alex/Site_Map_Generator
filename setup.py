from setuptools import setup
from setuptools import find_packages


with open("requirements.txt", encoding="utf-8") as f:
    requiered = f.readlines()
    

setup(

	author='IG-88Alex',
	author_email='@IG_88Alex (Telegram)',

    name='Python_Site_Map',
    version="0.0.2",
    description="Open and free site map generator",
    long_description="Open and free site map generator",
    long_description_content_type="text/markdown",
    python_requires=">=3.8.0",

    packages=find_packages(),
    include_package_data=True,
    install_requires = requiered,
    entry_points={ 'console_scripts': ['sitemap = src.__main__:main','map = src.__main__:main' ] },

    license="MIT License",
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: GNU/Linux :: Ubuntu (18.04 LTS +), Debian (10.0)",
        "Topic :: Internet",
        "License :: OSI Approved :: MIT License",
        ]
    )
