from setuptools import setup, find_packages
import os
from glob import glob

package_name = "dummy_object_publisher"

setup(
    name=package_name,
    version="0.0.0",
    packages=[package_name],
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml"]),
        (
            os.path.join(os.path.join("share", package_name), "launch"),
            glob("launch/*.launch.py"),
        ),
        (
            os.path.join(os.path.join("share", package_name), "configs"),
            glob("configs/*"),
        ),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="roar",
    maintainer_email="wuxiaohua1011@berkeley.edu",
    description="TODO: Package description",
    license="TODO: License declaration",
    tests_require=["pytest"],
    entry_points={
        "console_scripts": [
            "dummy_3d_publisher_node=dummy_object_publisher.dummy_3d_publisher_node:main"
        ],
    },
)
