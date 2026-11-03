"""Recupera solo 1_raw.csv desde el ZIP original o desde un CSV descargado."""
from pathlib import Path
import argparse
import hashlib
import io
import zipfile
import pandas as pd
import numpy as np

MEMBER='ckwc76xr2z-2/sEMG-dataset/raw/csv/1_raw.csv'
EXPECTED='0bf791c1d2d55f93b755f2f9566809cb4d36ba9888a25a26bf5c925294f926e6'

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('origen',type=Path,help='Ruta al ZIP Mendeley v2 o a 1_raw.csv')
    args=parser.parse_args()
    if args.origen.suffix.lower()=='.zip':
        with zipfile.ZipFile(args.origen) as z:
            with z.open(MEMBER) as f: df=pd.read_csv(f,header=None)
    else:
        df=pd.read_csv(args.origen,header=None)
    digest=hashlib.sha256(df.to_numpy().astype('<f8').tobytes(order='C')).hexdigest()
    if df.shape!=(1280000,4) or not np.isfinite(df.to_numpy()).all() or digest!=EXPECTED:
        raise ValueError('El archivo no coincide con el registro 1_raw validado.')
    dest=Path(__file__).resolve().parents[1]/'datos/senal_emg.csv'
    dest.parent.mkdir(parents=True,exist_ok=True)
    if dest.exists():
        existing=pd.read_csv(dest,header=None).to_numpy()
        if hashlib.sha256(existing.astype('<f8').tobytes(order='C')).hexdigest()==EXPECTED:
            print('Datos existentes verificados; se preserva el archivo:',dest)
            return
        raise FileExistsError('Hay otro CSV en destino: respáldelo antes de importar.')
    df.to_csv(dest,index=False,header=False)
    print('Importado y verificado:',dest)

if __name__=='__main__': main()
