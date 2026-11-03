"""Ejecuta los dos notebooks desde kernels Python nuevos y registra resultados."""
from pathlib import Path
from tempfile import TemporaryDirectory
from datetime import datetime, timezone
import json, sys, time
import nbformat
from nbclient import NotebookClient
from jupyter_client import KernelManager
from jupyter_client.kernelspec import KernelSpecManager

def main():
    root=Path(__file__).resolve().parents[1]
    results=[]
    with TemporaryDirectory(prefix='pdsb-kernel-') as temp:
        spec=Path(temp)/'pdsb-ejecucion';spec.mkdir()
        (spec/'kernel.json').write_text(json.dumps({'argv':[sys.executable,'-m','ipykernel_launcher','-f','{connection_file}'],
            'display_name':'Python PDSB ejecución','language':'python'}),encoding='utf-8')
        ksm=KernelSpecManager(kernel_dirs=[temp])
        for name in ['01_eda.ipynb','02_caracteristicas.ipynb']:
            path=root/'notebooks'/name
            nb=nbformat.read(path,as_version=4)
            km=KernelManager(kernel_name='pdsb-ejecucion',kernel_spec_manager=ksm)
            start=time.monotonic()
            print('Ejecutando con kernel nuevo:',name,flush=True)
            client=NotebookClient(nb,timeout=600,km=km,resources={'metadata':{'path':str(root)}})
            try:
                client.execute()
            finally:
                if km.has_kernel: km.shutdown_kernel(now=True)
            nb.metadata.kernelspec={'display_name':'Python 3 (PDSB)','language':'python','name':'python3'}
            nbformat.validate(nb);nbformat.write(nb,path)
            record={'notebook':name,'estado':'OK','celdas_codigo':sum(c.cell_type=='code' for c in nb.cells),
                'errores':sum(o.output_type=='error' for c in nb.cells if c.cell_type=='code' for o in c.outputs),
                'duracion_s':round(time.monotonic()-start,2),'kernel_nuevo':True,'cwd':'raíz del proyecto',
                'fecha_UTC':datetime.now(timezone.utc).isoformat()}
            results.append(record);print(json.dumps(record,ensure_ascii=False),flush=True)
    (root/'evidencias/ejecucion_notebooks.json').write_text(json.dumps(results,indent=2,ensure_ascii=False),encoding='utf-8')

if __name__=='__main__':main()
