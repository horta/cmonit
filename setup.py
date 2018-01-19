from setuptools import setup

if __name__ == '__main__':
    setup(entry_points={
        'console_scripts': ['cmonit=cmonit.cmonit:entry_point'],
    })
