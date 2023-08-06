from setuptools import find_packages
from setuptools import setup

setup(
    name="insight_python_linux",
    author="htsc",
    version="4.1.2",
    author_email="insight@htsc.com",
    description="insight_python_linux",
    long_description="insight_python_linux",
    license='insightpythonsdk',
    project_urls={
        'Documentation': 'https://packaging.python.org/tutorials/distributing-packages/',
        'Funding': 'https://donate.pypi.org',
        'Source': 'https://github.com/pypa/sampleproject/',
        'Tracker': 'https://github.com/pypa/sampleproject/issues',
    },

    packages=['insight_python_linux',
              'insight_python_linux/com',
              'insight_python_linux/com/interface',
              'insight_python_linux/com/cert',
              'insight_python_linux/com/insight',

              'insight_python_linux/com/libs/linux/python36',
              'insight_python_linux/com/libs/linux/python37',
              'insight_python_linux/com/libs/linux/python39',
              'insight_python_linux/com/libs/linux/python310',

              ],

    package_dir={
                 'insight_python_linux/com/cert': 'insight_python_linux/com/cert',
                 'insight_python': 'insight_python',
                 'insight_python_linux/com/libs/linux/python36':
                     'insight_python_linux/com/libs/linux/python36',
                 'insight_python_linux/com/libs/linux/python37':
                     'insight_python_linux/com/libs/linux/python37',
                 'insight_python_linux/com/libs/linux/python39':
                     'insight_python_linux/com/libs/linux/python39',
                 'insight_python_linux/com/libs/linux/python310':
                     'insight_python_linux/com/libs/linux/python310',
                 },

    package_data={
        'insight_python_linux/com/cert': ['HTInsightCA.crt', 'InsightClientCert.pem', 'HTISCA.crt', 'InsightClientKeyPkcs8.pem'],
        'insight_python': ['requirements.txt'],
        'insight_python_linux/com/libs/linux/python36': ['_mdc_gateway_client.so', 'libACE.so.6.4.3', 'libACE_SSL.so.6.4.3', 'libprotobuf.so.11',
                                                "libmdc_query_client.so", "mdc_gateway_client.py"],
        'insight_python_linux/com/libs/linux/python37': ['_mdc_gateway_client.so', 'libACE.so.6.4.3', 'libACE_SSL.so.6.4.3', 'libprotobuf.so.11',
                                                "libmdc_query_client.so", "mdc_gateway_client.py"],
        'insight_python_linux/com/libs/linux/python39': ['_mdc_gateway_client.so', 'libACE.so.6.4.3', 'libACE_SSL.so.6.4.3', 'libprotobuf.so.11',
                                                "libmdc_query_client.so", "mdc_gateway_client.py"],
        'insight_python_linux/com/libs/linux/python310': ['_mdc_gateway_client.so', 'libACE.so.6.4.3', 'libACE_SSL.so.6.4.3', 'libprotobuf.so.11',
                                                "libmdc_query_client.so", "mdc_gateway_client.py"],

        },

    install_requires=[],

    python_requires='>=3.6.*',
)