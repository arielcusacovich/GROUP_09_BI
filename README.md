# Group 09 Workshop 2

**Respiratory emergency visits among children under 15 · Metropolitan Region, 2023–2024**  
**Ariel Cusacovich and Ana Peris Diaz-Varela · Business Intelligence IIB423T-1 · Universidad del Desarrollo**  
Prepared for the 29 October 2026, 23:59 Chile submission.

Our executable notebook is [`notebooks/W2_project.ipynb`](notebooks/W2_project.ipynb). We continue our W1/C1 project, address the three C1 feedback items, and implement data validation, sampling, a leakage audit and chronological train/validation/test subsets. No predictive model is required or fitted. The final section presents our management summary.

## Read and reproduce

1. Open the saved notebook to inspect its code, explanations, tables and four figures. All cells have saved outputs.
2. **Windows x64, complete offline package:** extract the entire ZIP and double-click `EJECUTAR_W2.cmd`. Python 3.12 and the required libraries are included under `runtime/`; no installation, download, account or external data folder is needed. Keep all folders together. The notebook, tables and figures are regenerated from the original sources. A portable runtime is supplied for Windows x64 only.
3. **Other systems or an existing Python environment:** use Python 3.12 and install the tested packages:

```text
python -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
python scripts/run_notebook.py
```

On macOS/Linux, replace the activation line with `source .venv/bin/activate`. The runner uses the same Python interpreter that launches it and executes every code cell in order in a fresh local process, saving text, tables and embedded figures back to the notebook. It does not start a server or require a global Jupyter kernel. The notebook can also be run normally in Jupyter or VS Code. It works from any folder because the runner resolves the project root. In a notebook interface, select the installed environment, start from `notebooks/` or the project root, and use **Restart Kernel and Run All**. A notebook interface such as VS Code or JupyterLab is optional; the automated route does not require it.

**Full-source mode is the delivered default.** It checks fingerprints, scans all **17,872,309** original national CSV rows in chunks of 200,000, recreates the **37,976** scope-filtered cause rows, validates the transformations and exports results. No network access is required once dependencies are installed and the supplied source ZIPs are present. Execution time depends on the machine; allow several minutes and adequate disk space.

**Quick/offline extract mode:** `python scripts/run_notebook.py --quick`. This verifies and uses the included reduced input CSVs. It produces the same analytical results, but its execution record explicitly states that the national files were not rescanned. The runner saves that mode in the notebook. Running the command again without `--quick` automatically restores full-source mode. The dictionary is always supplied. The reduced CSV fingerprint normalizes line endings for cross-platform use.

## Data provenance and access

Original DEIS/MINSAL snapshots and their SHA-256 hashes are recorded in [`data/source/sources.csv`](data/source/sources.csv). That inherited register dates the original retrieval/verification to **25 September 2026**; W2 verifies the supplied local versions, not a new online download.

- [DEIS annual 2023 source](https://repositoriodeis.minsal.cl/SistemaAtencionesUrgencia/AtencionesUrgencia2023.zip)
- [DEIS annual 2024 source](https://repositoriodeis.minsal.cl/SistemaAtencionesUrgencia/AtencionesUrgencia2024.zip)
- [Official dataset catalogue](https://datos.gob.cl/dataset/atenciones-de-urgencia)
- [Official dictionary resource](https://datos.gob.cl/dataset/atenciones-de-urgencia/resource/79c05b22-391b-4dbd-a362-ba088fecabab)

The complete offline delivery includes both annual ZIPs. The portable Windows runtime and these large ZIPs are excluded from ordinary Git tracking. The 2023 source file is excluded because it exceeds GitHub's 100 MiB per-file limit. A clone retains the verified extracts, dictionary, provenance, code, all current outputs and earlier artifacts. For a full rebuild after cloning, copy the retained annual ZIPs into `data/source/`, or retrieve the exact versions from the source links and verify their recorded hashes. If a remote version changes, use the retained offline snapshot or quick mode. Do not substitute new data without reviewing all conclusions. [GitHub file-size documentation](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github).

Source scope: `CodigoRegion=13`, `GLOSATIPOESTABLECIMIENTO=Hospital`, `IdCausa in {1,2}`. Under 15 is `Menores_1 + De_1_a_4 + De_5_a_14`. Provider region is not residence. Source rows are hospital-date-cause aggregates, not individual patient data. The dictionary's historical establishment annex is not merged.

## Folder contents

- `notebooks/`: the executable English notebook and all explanations.
- `data/source/`: original data, dictionary and provenance.
- `data/inputs/`: uncleaned extracts and fingerprints.
- `data/clean/`: prepared records and sample.
- `data/splits/`: training, validation, test and preprocessing parameters.
- `data/outputs/`: regenerated supporting tables and figures.
- `legacy/`: preserved W1/C1 artifacts and source mapping.
- `runtime/`, `EJECUTAR_W2.cmd` and `scripts/run_notebook.py`: independent Windows execution.
- `requirements.txt`: dependencies for another Python environment.

## Continuity and submission status

Our group is 09. The Group 10 label in the W1 package and C1 slide cover was incorrect; we correct it in W2. Historical artifacts retain their original labels and the erroneous KPI slide for traceability. Their shared identical source files are stored once at project level; `legacy/preservation_manifest.json` maps all 68 original files to their retained locations and hashes.

We previously kept W1 and C1 as submission folders rather than in GitHub. We now preserve both in this project. The local W2 revision is tagged **`W2`**. Once the repository is published, the submission will include its URL and this tag or the corresponding commit. The original files are retained; the local revision history does not represent earlier GitHub submissions.

## AI use

We used OpenAI Codex extensively for code, data checks, figures and English explanations. The notebook includes executable checks of the calculations and data handling. We remain responsible for verifying the results and explaining the assumptions and limitations of our analysis.
