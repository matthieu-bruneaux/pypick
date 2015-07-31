from setuptools import setup, find_packages

setup(name = "pypick",
      version = "1.0.0",
      py_modules = ["pick"],
      entry_points = {
          "console_scripts" : [
              "pypick=pick:_main"
              ]
      }
)

