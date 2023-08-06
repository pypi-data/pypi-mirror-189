from distutils.core import setup

setup(
    name='prakashcv',
    packages=['prakashcv'],
    version='0.0.1',
    license='MIT',
    description='Computer Vision Helping Library',
    author='Krishna Prakash',
    author_email='krishnaprakash603@gmail.com',
    keywords=['ComputerVision', 'HandTracking', 'FaceMesh'],
    install_requires=[
        'opencv-python',
        'numpy',
        'mediapipe'
    ],
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)