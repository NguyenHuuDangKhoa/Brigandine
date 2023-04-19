install-mamba:
	@conda install mamba -n base -c conda-forge

setup-environment:
	@echo "Install requirements"
	@mamba env create -f environment.yaml