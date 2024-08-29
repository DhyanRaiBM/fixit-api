from setuptools import setup, find_packages

setup(
    name='my_fastapi_app',
    version='0.1.0',
    description='A FastAPI application',
    author='Your Name',
    author_email='your.email@example.com',
    packages=find_packages(),
    install_requires=[
        'fastapi>=0.68.0',
        'uvicorn[standard]>=0.15.0',
        'pydantic>=1.8.2',
        'pymongo>=3.12.0',
        'motor>=2.4.0',
        'flask>=2.0.1',
        'python-dotenv>=0.19.2',
    ],
    entry_points={
        'console_scripts': [
            'my_fastapi_app = main:app',  # Adjust according to your main file and application
        ],
    },
)
