# 🧬 Antibody Structure Prediction App (IgFold-based)

This project is a web-based tool that predicts and visualizes antibody structures using [**IgFold**](https://github.com/Graylab/IgFold). Users can input **heavy and light chain sequences**, refine structures using **OpenMM** or **PyRosetta**, and download:
- 3D structure files (.pdb)
- Amino acid sequences (.fasta)
- RMSD plots (predicted uncertainty across residues)

![RMSD Example](./example_rmsd.png)

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
