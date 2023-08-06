from setuptools import setup, find_packages


setup(
    name='kafka-client-decorator',
    version='1.0',
    license='MIT',
    description='A wrapper for confluent-kafka producer and consumer',
    author="Quantrium",
    author_email='firoz.mohammad@quantrium.ai',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://www.quantrium.ai/',
    keywords=['confluent-kafka', 'Kafka-producer', 'Kafka-consumer'],
    python_requires = ">=3.6",
    install_requires=[
          'confluent-kafka==2.0.2',
      ],

)