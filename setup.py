from setuptools import setup, find_packages
setup(
    name="Tikweb",
    version="1.0.4",
    description="TikTok Web",
    author="Lariot",
    author_email="lariot.antsa@gmail.com",
    packages=find_packages(),
    install_requires=[
        "requests",
        "pyexecjs",
    ],
    entry_points={
        'console_scripts': [
            'report-tiktok=TikTok.main:main'
        ]
    },
    python_requires=">=3.6",
)
