from setuptools import find_packages, setup


setup(
    name='kiki_utils_image',
    classifiers=[
        'License :: Freely Distributable'
    ],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
    version='1.0.3',
    description='Utils image functions.',
    author='kiki-kanri',
    author_email='a470666@gmail.com',
    keywords=['Utils'],
    install_requires=[
        'kiki-utils',
        'opencv-python',
        'pillow',
        'requests'
    ],
    python_requires=">=3.8"
)
