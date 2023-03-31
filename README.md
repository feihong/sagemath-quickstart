# Feihong's SageMath Quickstart

## Prerequisites

[Install conda](https://github.com/feihong/conda-quickstart)

## Installation

### Linux

Create new conda environment and install SageMath into it

    mamba create -n sage
    mamba activate sage
    mamba install sage jupyterlab

If you use VS Code to edit Sage notebooks, you must install the [Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter) extension.

### Mac

It's easiest to just download a binary: https://github.com/3-manifolds/Sage_macOS/releases

Before you can use Sage from Jupyter, you must run `sage` from the command line at least once.

## Commands

Start JupyterLab server

    jupyter-lab

## Notes

Running Sage in VS Code works fine, but syntax highlighting will be a little off because VS Code thinks you're editing normal Python code.

It's not yet possible to import `.sage` files as modules. The only officially-supported way to create reusable modules right now is to create a `.py` file and import it the same way you do in Python. However, `.py` files cannot access the Sage preparser, meaning that you must import things explicitly. To find how how to import a function for statement, use the handy `import_statements` function, e.g.

    sage: import_statements(pi)
    from sage.symbolic.constants import pi

