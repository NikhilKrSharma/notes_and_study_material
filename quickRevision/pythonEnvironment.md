# Python Environment


## Important Terms


## Resources
[Resource 1](https://towardsdatascience.com/create-virtual-environment-using-virtualenv-and-add-it-to-jupyter-notebook-6e1bf4e03415)  
[Python Virtual Environments: A Primer](https://realpython.com/python-virtual-environments-a-primer/)  
[External Tools & Libraries](https://realpython.com/effective-python-environment/)


## Quick Notes | Summary
### Inbuilt
`python  -m venv env_name`: Creates a virtual environment named `env_name`.

`source env_name/bin/activate`: Activates the virtual environment, adds its bin directory to PATH and sets the prompt accordingly.

`deactivate`: Deactivates the current virtual environment, returning you to your system’s default Python installation.


### [Using other library](https://realpython.com/effective-python-environment/)
Various libraries and tools to manage python environements are: 
#### `venv`
#### `pyenv`  
#### `conda`  
conda info —envs  
conda create -n \<envName> python=3.8 \<packageName> \<packageName>  \<packageName>  
conda remove --name <<envName>> --all [-y]  
conda create --name connectedComponent --clone copyme

#### `pyenv-virtualenv`
#### `pipenv`
#### `poetry`
#### `ipykernel`


### IPYTHON KERNALS

`pip install ipykernel`  
`python -m ipykernel install --user --name=<<vEnvName>>`  
`jupyter kernelspec list`  
`jupyter kernelspec uninstall <my_env_name>`  

`python3 -m venv /path/to/new/virtual/environmentName`

`jupyter nbconvert --execute exploreTiltOptimization.ipynb`  
`jupyter nbconvert --execute exploreTiltOptimization.ipynb --to notebook`

