Use `anaconda-project run` to run the project (from within the same folder as this file).

To use the enviornment as a jupyter kernel, activate the enviornment (`source activate envs/default` from the same folder as this file), then add the kernelspec. E.g.:

```
source activate envs/default
python -m ipykernel install --user --name pyro-sandbox --display-name "Pyro Sandbox (3.7)"
```

You can Verify that the path to the executable is correct by running `jupyter kernelspec list --json`. 

