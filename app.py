import os
import html
import streamlit as st
import torch
from igfold import IgFoldRunner
from igfold.utils.visualize import plot_prmsd

# Optional: comment this out on Hugging Face if PyRosetta is unavailable
try:
    from igfold.refine.pyrosetta_ref import init_pyrosetta
    init_pyrosetta()
except:
    st.warning("PyRosetta not available — skipping refinement.")

# Set prediction output directory
pred_dir = "../my_antibody"
os.makedirs(pred_dir, exist_ok=True)

default_light = "DVVMTQTPFSLPVSLGDQASISCRSSQSLVHSNGNTYLHWYLQKPGQSPKLLIYKVSNRFSGVPDRFSGSGSGTDFTLKISRVEAEDLGVYFCSQSTHVPYTFGGGTKLEIK"
default_heavy = "EVQLVQSGPEVKKPGTSVKVSCKASGFTFMSSAVQWVRQARGQRLEWIGWIVIGSGNTNYAQKFQERVTITRDMSTSTAYMELSSLRSEDTAVYYCAAPYCSSISCNDGFDIWGQGTMVTVS"

st.title("🧬 IgFold Antibody Structure Prediction")

light_seq = st.text_area("Light Chain Sequence", default_light, height=100)
heavy_seq = st.text_area("Heavy Chain Sequence", default_heavy, height=100)

col1, col2, col3 = st.columns(3)
with col1:
    use_light = st.checkbox("Use Light Chain", value=True)
with col2:
    use_heavy = st.checkbox("Use Heavy Chain", value=True)
with col3:
    refine = st.checkbox("Refine Structure", value=True)

if st.button("Predict Structure"):
    sequences = {}
    if use_light and light_seq.strip():
        sequences["L"] = light_seq.strip()
    if use_heavy and heavy_seq.strip():
        sequences["H"] = heavy_seq.strip()

    if not sequences:
        st.error("Please provide at least one sequence.")
    else:
        pdb_path = os.path.join(pred_dir, "structure.pdb")
        fasta_path = os.path.join(pred_dir, "structure.fasta")
        prmsd_path = os.path.join(pred_dir, "structure_prmsd.png")

        runner = IgFoldRunner()
        out = runner.fold(
            pdb_path,
            sequences=sequences,
            do_refine=refine,
            do_renum=True
        )

        # Write FASTA
        with open(fasta_path, "w") as f:
            for k, v in sequences.items():
                f.write(f">{k}\n{v}\n")

        # Plot RMSD
        plot_prmsd(sequences, out.prmsd.cpu(), prmsd_path, shade_cdr=True, pdb_file=pdb_path)

        with open(pdb_path) as f:
            pdb_data = f.read()

        escaped_pdb = html.escape(pdb_data)

        html_viewer = f"""
        <iframe height="500px" width="100%" frameborder="0" srcdoc='
        <!DOCTYPE html>
        <html>
        <head><script src="https://3Dmol.csb.pitt.edu/build/3Dmol-min.js"></script></head>
        <body>
        <div id="viewer" style="width: 100%; height: 500px; position: relative;"></div>
        <script>
            let viewer = $3Dmol.createViewer("viewer", {{ backgroundColor: "white" }});
            viewer.addModel(`{escaped_pdb}`, "pdb");
            viewer.setStyle({{}}, {{cartoon: {{color: "spectrum"}}}});
            viewer.zoomTo();
            viewer.render();
        </script>
        </body>
        </html>
        '></iframe>
        """

        st.components.v1.html(html_viewer, height=520, scrolling=True)
        st.image(prmsd_path, caption="Predicted RMSD")
        st.download_button("Download PDB", pdb_data, file_name="structure.pdb")
        st.download_button("Download FASTA", open(fasta_path).read(), file_name="structure.fasta")
