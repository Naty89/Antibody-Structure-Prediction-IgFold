FROM continuumio/miniconda3

WORKDIR /app
COPY .. /app

# Set environment variables
ENV CONDA_ENV=igfold-env
ENV PYTHONDONTWRITEBYTECODE=1

# Create conda environment and install bioconda + pip packages
RUN conda create -n ${CONDA_ENV} python=3.8 \
    && conda run -n ${CONDA_ENV} conda install -c bioconda anarci abnumber -y \
    && conda run -n ${CONDA_ENV} pip install pyrosetta-installer \
    && conda run -n ${CONDA_ENV} python -c "import pyrosetta_installer; pyrosetta_installer.install_pyrosetta()" \
    && conda run -n ${CONDA_ENV} pip install -r requirements.txt

# Use conda env as shell
SHELL ["conda", "run", "-n", "igfold-env", "/bin/bash", "-c"]

# Expose Streamlit port
EXPOSE 7860

# Run the Streamlit app
CMD ["conda", "run", "--no-capture-output", "-n", "igfold-env", "streamlit", "run", "app.py", "--server.port=7860", "--server.address=0.0.0.0"]
