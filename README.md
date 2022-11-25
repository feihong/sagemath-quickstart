# Feihong's SageMath Quickstart

## Prerequisites

[Install conda](https://github.com/feihong/conda-quickstart)

## Installation

Create new conda environment and install SageMath into it

    mamba create -n sage
    mamba activate sage
    mamba install sage jupyterlab

If you use VS Code to edit Sage notebooks, you must install the [Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter) extension.

## Commands

Start JupyterLab server

    jupyter-lab

## Notes

Running Sage in VS Code works fine, but syntax highlighting will be a little off because VS Code thinks you're editing normal Python code.
