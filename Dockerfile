# Base image with Python 3.8
FROM continuumio/miniconda3

# Set working directory
WORKDIR /app

# Copy project files into the image
COPY . /app

# Environment name
ENV CONDA_ENV=igfold-env

# Create environment and install dependencies
RUN conda create -n ${CONDA_ENV} python=3.8 -y \
    && conda run -n ${CONDA_ENV} conda install -c bioconda anarci abnumber -y \
    && conda run -n ${CONDA_ENV} pip install --no-cache-dir pyrosetta-installer \
    && conda run -n ${CONDA_ENV} python -c "import pyrosetta_installer; pyrosetta_installer.install_pyrosetta()" \
    && conda run -n ${CONDA_ENV} pip install --no-cache-dir -r requirements.txt

# Make sure conda is used in the shell
SHELL ["conda", "run", "-n", "igfold-env", "/bin/bash", "-c"]

# Expose the default Streamlit port
EXPOSE 7860

# Start Streamlit app
CMD ["conda", "run", "--no-capture-output", "-n", "igfold-env", "streamlit", "run", "app.py", "--server.port=7860", "--server.address=0.0.0.0"]
