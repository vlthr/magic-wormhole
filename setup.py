
from setuptools import setup

import versioneer
versioneer.VCS = "git"
versioneer.versionfile_source = "src/wormhole/_version.py"
versioneer.versionfile_build = "wormhole/_version.py"
versioneer.tag_prefix = ""
versioneer.parentdir_prefix = "wormhole-sync"

commands = versioneer.get_cmdclass()

setup(name="wormhole-sync",
      version=versioneer.get_version(),
      description="Securely transfer data between computers",
      author="Brian Warner",
      author_email="warner-wormholesync@lothar.com",
      license="MIT",
      url="https://github.com/warner/wormhole-sync",
      package_dir={"": "src"},
      packages=["wormhole"],
      install_requires=["spake2", "requests"],
      test_suite="wormhole.test",
      cmdclass=commands,
      )