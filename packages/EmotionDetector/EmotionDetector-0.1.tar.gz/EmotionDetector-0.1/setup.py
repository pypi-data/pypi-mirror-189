from setuptools import setup, find_packages

setup(
    name='EmotionDetector',
    version='0.1',
    packages=find_packages(),
    url='https://github.com/alaesahbou/EmotionDetector',
    author='Alae-Eddine Sahbou',
    author_email='alae.shb147@gmail.com',
    description='This is the code repository for Alae-Eddine Sahbou Emotion Detector project. This program uses computer vision and facial analysis techniques to detect and recognize emotions in real-time video feed.',
    install_requires=['opencv-python', 'numpy', 'deepface'],
    include_package_data=True,
    package_data={'': ['haarcascade_frontalface_default.xml']}
)
