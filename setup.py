import setuptools

setuptools.setup(
    name="st_jsme",
    version="0.0.1",
    author="Leiming Zhu",
    author_email="zhu_36@yahoo.com",
    description="",
    long_description="",
    long_description_content_type="text/plain",
    url="",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.6",
    install_requires=[
        # By definition, a Custom Component depends on Streamlit.
        # If your component has other Python dependencies, list
        # them here.
        "streamlit >= 0.63",
    ],
)
