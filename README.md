
# 🧬 Antibody Structure Prediction App (IgFold-based)

This project is a web-based tool that predicts and visualizes antibody structures using [**IgFold**](https://github.com/Graylab/IgFold). Users can input **heavy and light chain sequences**, refine structures using **OpenMM** or **PyRosetta**, and download:
- 3D structure files (.pdb)
- Amino acid sequences (.fasta)
- RMSD plots (predicted uncertainty across residues)


---

## 🚀 Features

- 🧠 Antibody prediction with **IgFold**
- 🔍 Structure refinement with **OpenMM** or **PyRosetta**
- 📉 RMSD plots for both heavy/light chains
- 🧬 Downloadable PDB + FASTA
- 🖥️ Streamlit-based frontend with Docker deployment

---

## 📦 Installation & Usage (Docker)

1. **Clone the repository**
```bash
git clone https://github.com/Naty89/Antibody-Structure-Prediction-IgFold.git
cd Antibody-Structure-Prediction-IgFold
```

2. **Build the Docker image**
```bash
docker build -t igfold-app .
```

3. **Run the container**
```bash
docker run -p 7860:7860 igfold-app
```

4. **Access the app**
Open your browser and go to:  
[http://localhost:7860](http://localhost:7860)

---

## 🛠 Requirements (for local setup without Docker)

- Python 3.8
- torch==2.2.2
- pytorch-lightning==1.8.6
- igfold
- streamlit
- biopython, py3Dmol, seaborn, matplotlib, numpy, tqdm

Install with:
```bash
pip install -r requirements.txt
```

---

## 📂 File Structure

| File             | Description                                     |
|------------------|-------------------------------------------------|
| `app.py`         | Main Streamlit app                              |
| `Dockerfile`     | For containerized deployment                    |
| `requirements.txt` | Python package dependencies                   |
| `README.md`      | You're here :)                                  |

---

## 🧠 Acknowledgments

- [IgFold](https://github.com/Graylab/IgFold) - Antibody structure prediction
- [OpenMM](https://openmm.org/) - Molecular mechanics refinement
- [PyRosetta](http://www.pyrosetta.org/) - Structure refinement toolkit

---

## 📫 Contact

Feel free to reach out via [LinkedIn]([https://www.linkedin.com/in/atnatiwos-gebremedhin-397920191/]) or submit issues/ideas via GitHub!
