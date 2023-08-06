from setuptools import setup

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='win-pos',
    author='Liam Edwards',
    author_email='me@liamedwards.dev',
    description='Add utility methods that allow you to easily grab the position of a window',
    keywords='windows, window, position, helpers, human friendly, python',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/liam-edwards/python-window-positions',
    project_urls={
        'Documentation': 'https://github.com/liam-edwards/python-window-positions',
        'Source': 'https://github.com/liam-edwards/python-window-positions',
        'Tracker': 'https://github.com/liam-edwards/python-window-positions/issues',
    },
    packages=['WinPos'],
    license='LICENSE.txt',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3 :: Only',
        
        'License :: OSI Approved :: MIT License',
        'Operating System :: Microsoft :: Windows',
        
        'Typing :: Typed',
    ],
    install_requires=['pywin32'],
    python_requires='>=3.7'
)
