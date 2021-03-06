import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example-package-YOUR-USERNAME-HERE",
    version="0.0.1",
    author="Ronald Johnson",
    author_email="lightarrow@icloud.com",
    description="Understanging data structures",
    long_description='Understanging data structures',
    long_description_content_type="text/markdown",
    url="https://github.com/lightarrow/",
    project_urls={
        "Bug Tracker": "https://github.com/lightarrow/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)