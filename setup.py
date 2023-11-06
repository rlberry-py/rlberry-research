from setuptools import setup, find_packages
import os


#ver_file = os.path.join("rlberry", "_version.py")
#with open(ver_file) as f:

with open("_version.py") as f:
    exec(f.read())

#packages = find_packages(exclude=["docs", "notebooks", "assets"])
packages = find_packages(exclude=["docs"])

#
# Base installation (interface only)
#
install_requires = [
     "rlberry"
#    "numpy>=1.17",
#    "scipy>=1.6",
#    "pygame-ce",
#    "matplotlib",
#    "seaborn",
#    "pandas",
#    "gymnasium",
#    "dill",
#    "docopt",
#    "pyyaml",
#    "tqdm",
]

#
# Extras
#

## default installation
default_requires = [
#    "numba",
#    "optuna",
#    "ffmpeg-python",
#    "PyOpenGL",
#    "pyvirtualdisplay",
#    "gymnasium",
]

# tensorboard must be installed manually, due to conflicts with
# dm-reverb-nightly[tensorflow] in jax_agents_requires
torch_agents_requires = default_requires + [
#    "torch>=1.6.0",
#    "opencv-python",
#    "gymnasium[atari,accept-rom-license]",
#    "ale-py>=0.8.0",
#    "stable-baselines3",
    # 'tensorboard'
]

jax_agents_requires = default_requires + [
#    "jax[cpu]",
#    "chex",
#    "dm-haiku",
#    "optax",
#    "dm-reverb[tensorflow]==0.6.1",
#    "dm-tree",
#    "rlax",
]

extras_require = {
    "default": default_requires,
    "jax_agents": jax_agents_requires,
    "torch_agents": torch_agents_requires,
    "deploy": ["sphinx", "sphinx_rtd_theme"],
}

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="rlberry-research",
    version=__version__,
    description="Algorithms and envs for research with rlberry",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="SCOOL Team",
    url="https://github.com/rlberry-rlberry-research",
    license="MIT",
    packages=packages,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Education",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=install_requires,
    extras_require=extras_require,
    zip_safe=False,
)
