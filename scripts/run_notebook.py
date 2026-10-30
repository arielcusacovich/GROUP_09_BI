"""Run every notebook cell in a fresh local Python process, without a server."""
from pathlib import Path
import argparse
import os
import sys
import traceback
import nbformat

parser = argparse.ArgumentParser()
parser.add_argument('--quick', action='store_true', help='Use verified supplied extracts instead of scanning original ZIPs.')
args = parser.parse_args()
root = Path(__file__).resolve().parents[1]
run_dir = root / '.run'
for variable, folder in [('IPYTHONDIR', 'ipython'), ('MPLCONFIGDIR', 'matplotlib'), ('TEMP', 'temp'), ('TMP', 'temp')]:
    destination = run_dir / folder
    destination.mkdir(parents=True, exist_ok=True)
    os.environ[variable] = str(destination)
os.environ['MPLBACKEND'] = 'module://matplotlib_inline.backend_inline'
os.chdir(root)

from IPython.core.interactiveshell import InteractiveShell
from IPython.utils.capture import capture_output
from matplotlib_inline.backend_inline import configure_inline_support

path = root / 'notebooks/W2_project.ipynb'
notebook = nbformat.read(path, as_version=4)
shell = InteractiveShell.instance()
configure_inline_support(shell, 'inline')
count = 0
try:
    for cell in notebook.cells:
        if cell.cell_type != 'code':
            continue
        if 'REBUILD_FROM_SOURCE = ' in cell.source:
            cell.source = cell.source.replace('REBUILD_FROM_SOURCE = False', 'REBUILD_FROM_SOURCE = True')
            if args.quick:
                cell.source = cell.source.replace('REBUILD_FROM_SOURCE = True', 'REBUILD_FROM_SOURCE = False')
        count += 1
        cell.execution_count = count
        cell.outputs = []
        print(f'Running code cell {count}...', flush=True)
        with capture_output(stdout=True, stderr=True, display=True) as captured:
            result = shell.run_cell(cell.source, store_history=True)
        if captured.stdout:
            cell.outputs.append(nbformat.v4.new_output('stream', name='stdout', text=captured.stdout))
        if captured.stderr:
            cell.outputs.append(nbformat.v4.new_output('stream', name='stderr', text=captured.stderr))
        for output in captured.outputs:
            cell.outputs.append(nbformat.v4.new_output('display_data', data=output.data, metadata=output.metadata))
        error = result.error_before_exec or result.error_in_exec
        if error is not None:
            cell.outputs.append(nbformat.v4.new_output('error', ename=type(error).__name__, evalue=str(error), traceback=traceback.format_exception(error)))
            raise RuntimeError(f'Notebook failed in code cell {count}: {error}') from error
finally:
    nbformat.write(notebook, path)
print(f'Completed all {count} code cells. Notebook, tables and figures saved.', flush=True)
