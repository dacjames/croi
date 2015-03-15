import os
from distutils.core import setup
from distutils.extension import Extension

setup_args = {
    'name': 'croi',
    'version': '0.1.0',
    'packages': ['croi'],
}

try:
    from Cython.Build import cythonize
    use_cython = True

except ImportError:
    use_cython = False


submodules_names = [
    'generators',
    'decorators',
    'reflection',
    'collection'
]

if use_cython:
    setup_args['ext_modules'] = cythonize([
        os.path.join("croi", filename + ".py")
        for filename in submodules_names
    ])

else:
    setup_args['ext_modules'] = [
        Extension("croi." + filename, [os.path.join("croi", filename + ".c")])
        for filename in submodules_names
    ]

setup(**setup_args)
