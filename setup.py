import setuptools

setuptools.setup(
    name="jupyter-podcast-proxy",
    version='0.0.2',
    url="https://gitlab.mpcdf.mpg.de/khr/jupyter-streamlit-proxy",
    author="Klaus Reuter",
    description="klaus.reuter@mpcdf.mpg.de",
    packages=setuptools.find_packages(),
	keywords=['Jupyter'],
	classifiers=['Framework :: Jupyter'],
    install_requires=[
        'jupyter-server-proxy'
    ],
    entry_points={
        'jupyter_serverproxy_servers': [
            'podcast = jupyter_podcast_proxy:setup_podcast_proxy',
        ]
    },
    package_data={
        'jupyter_podcast_proxy': ['icons/*'],
    },
)
