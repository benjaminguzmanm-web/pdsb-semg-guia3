"""Análisis reproducible de sEMG cruda. No atribuye fuerza ni clasifica gestos."""
from pathlib import Path
import hashlib
import json
import platform
import sys
import numpy as np
import pandas as pd
import scipy
from scipy import signal, integrate
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

FS = 2000
CHANNELS = [f'Canal_{i}' for i in range(1, 5)]
GESTURES = ['Reposo', 'Extensión', 'Flexión', 'Desviación cubital',
            'Desviación radial', 'Agarre', 'Abducción', 'Aducción', 'Supinación', 'Pronación']
COLORS = ['#123B5D', '#E87827', '#238B8E', '#7A5195']
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 10,
                     'axes.spines.top': False, 'axes.spines.right': False,
                     'axes.titleweight': 'bold', 'figure.dpi': 120,
                     'savefig.dpi': 160, 'axes.grid': True, 'grid.alpha': .18})


def folders(root):
    root = Path(root).resolve()
    for sub in ['figuras', 'evidencias', 'notebooks', 'datos', 'src']:
        (root/sub).mkdir(parents=True, exist_ok=True)
    return root


def load_data(root):
    path = Path(root)/'datos/senal_emg.csv'
    df = pd.read_csv(path, header=None, names=CHANNELS, dtype=float)
    if df.shape != (1280000, 4) or not np.isfinite(df.to_numpy()).all():
        raise ValueError('El registro difiere del validado: revise dimensiones y valores.')
    expected = '0bf791c1d2d55f93b755f2f9566809cb4d36ba9888a25a26bf5c925294f926e6'
    actual = hashlib.sha256(df.to_numpy().astype('<f8').tobytes(order='C')).hexdigest()
    if actual != expected:
        raise ValueError('SHA256 numérico distinto: no se debe procesar silenciosamente otro registro.')
    return df


def constant_runs(x, minimum=200):
    bounds = np.r_[0, np.flatnonzero(np.diff(x) != 0)+1, len(x)]
    return [(int(a), int(b), float(x[a])) for a, b in zip(bounds[:-1], bounds[1:])
            if b-a >= minimum]


def quality_mask(x):
    mask = np.abs(x) >= 9.999  # Rango nominal documentado +/-10 mV. Indicio de recorte.
    for a, b, value in constant_runs(x):
        mask[a:b] = True
    return mask


def savefig(root, name, fig):
    fig.savefig(Path(root)/'figuras'/name, bbox_inches='tight', facecolor='white')
    plt.close(fig)


def eda(root):
    root = folders(root)
    df = load_data(root)
    x = df.to_numpy()
    stats = df.describe(percentiles=[.05, .25, .5, .75, .95]).T
    stats['nan'] = df.isna().sum()
    stats['no_finitos'] = (~np.isfinite(x)).sum(axis=0)
    stats['iqr'] = stats['75%']-stats['25%']
    stats['candidatos_iqr'] = [int(((x[:,c] < stats.iloc[c]['25%']-1.5*stats.iloc[c]['iqr']) |
                                 (x[:,c] > stats.iloc[c]['75%']+1.5*stats.iloc[c]['iqr'])).sum())
                                 for c in range(4)]
    stats['muestras_cerca_riel'] = (np.abs(x) >= 9.999).sum(axis=0)
    stats['maximo_repetido'] = [(x[:,c] == x[:,c].max()).sum() for c in range(4)]
    stats.to_csv(root/'evidencias/resumen_calidad.csv', index_label='canal')
    anomalies = []
    for c in range(4):
        for a, b, v in constant_runs(x[:,c]):
            anomalies.append({'canal':CHANNELS[c], 'inicio_indice':a, 'fin_indice_exclusivo':b,
                              'inicio_s':a/FS, 'fin_s_exclusivo':b/FS, 'muestras':b-a,
                              'duracion_s':(b-a)/FS, 'valor_mV':v,
                              'decision':'Conservar original; marcar y excluir ventanas afectadas de resumen de actividad',
                              'hipotesis':'Tramo plano; posible recorte, causa física no demostrada'})
    pd.DataFrame(anomalies).to_csv(root/'evidencias/anomalias.csv', index=False)
    time = {'muestras_por_canal':len(df), 'canales':4, 'fs_documentada_Hz':FS,
            'Ts_s':1/FS, 'duracion_soporte_s':len(df)/FS, 'tiempo_ultima_muestra_s':(len(df)-1)/FS,
            'marcas_tiempo_observadas':False, 'filas_completas_duplicadas':int(df.duplicated().sum()),
            'discontinuidades_adquisicion':'No verificables: no hay timestamps independientes',
            'uniformidad':'Documentada en metadatos; eje t=n/fs construido, no medido',
            'regla_tramo_plano':'Valores exactamente iguales durante al menos 200 muestras (0.1 s)',
            'regla_riel':'abs(x)>=9.999 mV; umbral exploratorio cercano al rango +/-10 mV',
            'rango_nominal_mV':[-10,10], 'canal_principal':'Canal_4',
            'criterio_canal':'Media próxima a cero y ausencia de tramos planos >=0.1s; no representa superioridad fisiológica'}
    (root/'evidencias/control_tiempo.json').write_text(json.dumps(time,indent=2,ensure_ascii=False),encoding='utf-8')
    pd.DataFrame([{'campo':c,'significado':f'Canal sEMG crudo {i+1}', 'tipo':'float64', 'unidad':'mV',
                   'fuente':f'1_raw.mat: labels[{i}]', 'faltantes':0,
                   'limitacion':'Sin asignación anatómica individual verificada'} for i,c in enumerate(CHANNELS)] +
                 [{'campo':'tiempo_s','significado':'Índice de muestra / fs documentada', 'tipo':'float64 derivado',
                   'unidad':'s','fuente':'fs=2000 Hz, start_sample=0 del MAT', 'faltantes':0,
                   'limitacion':'No es timestamp observado; no detecta pérdidas previas a exportación'}]).to_csv(root/'datos/diccionario.csv',index=False)
    fig, axes = plt.subplots(4,1,figsize=(11,8),sharex=True)
    # Envolvente min/max por bloques de 0.5 s: representación, sin alterar los datos del análisis.
    for c, ax in enumerate(axes):
        blocks=x[:,c].reshape(-1,1000); t=(np.arange(len(blocks))+.5)*.5
        ax.fill_between(t, blocks.min(axis=1), blocks.max(axis=1),alpha=.65,color=COLORS[c])
        ax.axhline(x[:,c].mean(),color='black',lw=.7,ls='--')
        ax.set_ylabel(f'CH{c+1} (mV)')
    axes[0].set_title('Registro crudo: envolvente mínima/máxima cada 0,5 s')
    axes[-1].set_xlabel('Tiempo derivado de metadatos (s)');fig.tight_layout()
    savefig(root,'eda_global.png',fig)
    fig, axes=plt.subplots(1,2,figsize=(11,3.5))
    a,b=int(532*FS),int(537*FS); t=np.arange(a,b)/FS
    axes[0].plot(t,x[a:b,0],lw=.7,color=COLORS[0]);axes[0].axvspan(533.3845,536,color='#E87827',alpha=.25)
    axes[0].set(xlabel='Tiempo (s)',ylabel='Canal 1 (mV)',title='5.231 muestras constantes en el máximo')
    for c in range(4):
        # muestreo determinista solo para histograma. Estadísticos usan todas las muestras.
        axes[1].hist(x[::20,c]-x[:,c].mean(),bins=100,histtype='step',density=True,
                     label=f'CH{c+1}',color=COLORS[c])
    axes[1].set(xlabel='Amplitud centrada globalmente (mV)',ylabel='Densidad (1/mV)',yscale='log',title='Distribuciones de los cuatro canales')
    axes[1].legend(ncol=2);fig.tight_layout();savefig(root,'calidad_meseta_distribucion.png',fig)
    print('Registro:',df.shape,'fs:',FS,'Hz; duración:',len(df)/FS,'s')
    print(stats[['mean','std','min','max','nan','muestras_cerca_riel']].to_string())
    print('Tramos planos >=0,1 s:',len(anomalies),'\n',pd.DataFrame(anomalies).to_string(index=False))
    print('El tiempo procede de metadatos; no se verifican saltos con timestamps independientes.')
    return stats


def spectral_features(v, fs=FS):
    v = np.asarray(v, dtype=float)
    y = v-v.mean()
    rms = float(np.sqrt(np.mean(y*y))); mav = float(np.mean(np.abs(y)))
    if rms == 0:
        return rms,mav,np.nan,np.nan,0.0
    f,p=signal.welch(y,fs=fs,window='hann',nperseg=2000,noverlap=1000,
                     detrend='constant',scaling='density',return_onesided=True)
    cumulative=integrate.cumulative_trapezoid(p,f,initial=0)
    power=float(cumulative[-1])
    if power <= 0: return rms,mav,np.nan,np.nan,power
    median=float(np.interp(power*.5,cumulative,f))
    mean=float(integrate.trapezoid(f*p,f)/power)
    return rms,mav,median,mean,power


def feature_row(x,c,a,b,mask,**extra):
    rms,mav,mdf,mnf,power=spectral_features(x[a:b,c])
    flags=int(mask[a:b].sum())
    return {'canal':CHANNELS[c], 'inicio_s':a/FS,'fin_s_exclusivo':b/FS,
            'muestras':b-a,'rms_ac_mV':rms,'mav_ac_mV':mav,
            'frecuencia_mediana_Hz':mdf,'frecuencia_media_Hz':mnf,
            'potencia_psd_mV2':power,'muestras_marcadas':flags,
            'valida_calidad':flags==0 and np.isfinite(mdf),**extra}


def characteristics(root):
    root=folders(root);df=load_data(root);x=df.to_numpy()
    masks=[quality_mask(x[:,c]) for c in range(4)]
    rows=[]
    for c in range(4):
        for a in range(0,len(x),4000): rows.append(feature_row(x,c,a,a+4000,masks[c]))
    features=pd.DataFrame(rows);features.to_csv(root/'evidencias/caracteristicas_ventanas.csv',index=False)
    valid=features[features.valida_calidad]
    summary=valid.groupby('canal')[['rms_ac_mV','mav_ac_mV','frecuencia_mediana_Hz','frecuencia_media_Hz']].agg(['median','min','max'])
    summary.to_csv(root/'evidencias/resumen_caracteristicas.csv')
    # Traducción del script oficial: MATLAB a*fs+1:b*fs = Python [a*fs:b*fs].
    events=[];protocol=[]
    for rep,start in enumerate([4,138,272,406,540],1):
        for gesture,label in enumerate(GESTURES):
            onset=start+gesture*10
            protocol.append({'ciclo':rep,'gesto_id':gesture,'condicion_nominal':label,'inicio_tarea_s':onset,'fin_tarea_s_exclusivo':onset+6,
                             'inicio_ventana_s':onset+2,'fin_ventana_s_exclusivo':onset+4,
                             'fuente':'EMG_gesture_segmentation.m; etiqueta de tarea programada, sin verificación cinemática'})
            for c in range(4):
                events.append(feature_row(x,c,int((onset+2)*FS),int((onset+4)*FS),masks[c],
                                          ciclo=rep,gesto_id=gesture,condicion_nominal=label))
    pd.DataFrame(protocol).to_csv(root/'datos/protocolo_gestos.csv',index=False)
    event_df=pd.DataFrame(events);event_df.to_csv(root/'evidencias/caracteristicas_protocolo.csv',index=False)
    ch4=event_df[(event_df.canal=='Canal_4') & event_df.valida_calidad]
    gs=ch4.groupby(['gesto_id','condicion_nominal'])[['rms_ac_mV','mav_ac_mV','frecuencia_mediana_Hz']].agg(['median','min','max'])
    gs.to_csv(root/'evidencias/resumen_gestos_canal4.csv')
    compare=event_df[(event_df.canal=='Canal_4') & (event_df.ciclo==1) & event_df.gesto_id.isin([0,5])]
    compare.to_csv(root/'evidencias/comparacion_reposo_agarre.csv',index=False)
    fig,axes=plt.subplots(1,2,figsize=(11,3.7))
    psd_export={}
    for i,row in enumerate(compare.itertuples()):
        a,b=int(row.inicio_s*FS),int(row.fin_s_exclusivo*FS);v=x[a:b,3];v=v-v.mean()
        axes[0].plot(np.arange(len(v))/FS,v,lw=.55,alpha=.8,color=COLORS[i],label=f'{row.condicion_nominal} ({row.inicio_s:g}-{row.fin_s_exclusivo:g} s)')
        f,p=signal.welch(v,fs=FS,window='hann',nperseg=2000,noverlap=1000,detrend='constant',scaling='density')
        psd_export['frecuencia_Hz']=f
        psd_export[f'{row.condicion_nominal}_mV2_Hz']=p
        axes[1].semilogy(f,p,color=COLORS[i],label=row.condicion_nominal)
    axes[0].set(xlabel='Tiempo desde inicio de ventana (s)',ylabel='CH4 centrado localmente (mV)',title='Ventanas centrales de tareas programadas')
    axes[0].legend(fontsize=8);axes[1].set(xlabel='Frecuencia (Hz)',ylabel='PSD (mV²/Hz)',xlim=(0,1000),title='Welch: Hann, 1 s, solapamiento 50%')
    axes[1].legend();fig.tight_layout();savefig(root,'comparacion_reposo_agarre_psd.png',fig)
    pd.DataFrame(psd_export).to_csv(root/'evidencias/psd_comparacion.csv',index=False)
    fig,axes=plt.subplots(1,2,figsize=(11,3.6))
    for ax,column,title in zip(axes,['rms_ac_mV','frecuencia_mediana_Hz'],['RMS AC (mV)','Frecuencia mediana (Hz)']):
        groups=[ch4[ch4.gesto_id==i][column].to_numpy() for i in range(10)]
        ax.boxplot(groups,showfliers=True)
        ax.set_xticks(np.arange(1,11),GESTURES)
        ax.tick_params(axis='x',rotation=55,labelsize=8);ax.set(ylabel=title,title='CH4: cinco ciclos del mismo participante')
    fig.tight_layout();savefig(root,'caracteristicas_gestos.png',fig)
    env={'python':platform.python_version(),'numpy':np.__version__,'pandas':pd.__version__,'scipy':scipy.__version__,'matplotlib':matplotlib.__version__,
         'ventana_s':2,'solapamiento_ventanas_s':0,'welch_nperseg':2000,'welch_noverlap':1000,'welch_window':'hann periódica',
         'welch_detrend':'constant por subsegmento','welch_scaling':'density unilateral', 'dominio_Hz':[0,1000],
         'paso_frecuencias_welch_Hz':1,'integracion':'trapecios; mediana interpolada en potencia acumulada',
         'filas_ventanas':len(features),'filas_ventanas_validas':int(features.valida_calidad.sum()),
         'filas_protocolo':len(event_df),'filas_protocolo_validas':int(event_df.valida_calidad.sum()),
         'nota':'RMS y MAV de señal centrada por ventana. No equivalen a fuerza. Etiquetas describen protocolo nominal.'}
    (root/'evidencias/parametros_analisis.json').write_text(json.dumps(env,indent=2,ensure_ascii=False),encoding='utf-8')
    print('Ventanas totales/aceptadas:',len(features),int(features.valida_calidad.sum()))
    print('Ventanas marcadas (se conservan, se omiten del resumen de actividad):\n',features[~features.valida_calidad].to_string(index=False))
    print('Comparación CH4, ciclo 1:\n',compare.to_string(index=False))
    print('Protocolo nominal:',len(protocol),'tareas,',len(event_df),'filas canal-tarea (50 por canal); corresponden a un participante.')
    return features,event_df


def temporal_and_validation(root):
    root=folders(root);x=load_data(root).Canal_4.to_numpy();x=x-x.mean()
    taps=signal.firwin(161,450,window=('kaiser',8.6),fs=FS)
    reduced=signal.resample_poly(x,up=1,down=2,window=taps,padtype='line')
    naive=x[::2]
    for name,values,fs_out in [('original',x,FS),('reducida',reduced,FS//2)]:
        a,b=int(56*fs_out),int(56.15*fs_out)
        pd.DataFrame({'tiempo_s':np.arange(a,b)/fs_out,'amplitud_mV':values[a:b]}).to_csv(root/f'evidencias/temporal_{name}.csv',index=False)
    f,p=signal.welch(x,fs=FS,window='hann',nperseg=4000,noverlap=2000,scaling='density')
    high=f>=500; fraction=integrate.trapezoid(p[high],f[high])/integrate.trapezoid(p,f)
    resp_f,resp=signal.freqz(taps,worN=32000,fs=FS)
    stop=float(20*np.log10(np.max(np.abs(resp[resp_f>=500]))))
    table=pd.DataFrame([{'version':'Original CH4 centrado','muestras':len(x),'fs_Hz':FS,'duracion_s':len(x)/FS,'desv_mV':np.std(x,ddof=1)},
                        {'version':'Remuestreo FIR antialias x2','muestras':len(reduced),'fs_Hz':FS/2,'duracion_s':len(reduced)/(FS/2),'desv_mV':np.std(reduced,ddof=1)},
                        {'version':'Selección cada 2 filas sin filtro (contraste)','muestras':len(naive),'fs_Hz':FS/2,'duracion_s':len(naive)/(FS/2),'desv_mV':np.std(naive,ddof=1)}])
    table.to_csv(root/'evidencias/comparacion_temporal.csv',index=False)
    temporal={'canal':'Canal_4','metodo':'resample_poly up=1 down=2; FIR explícito', 'numtaps':161,'fir_cutoff_Hz':450,
              'window':'Kaiser beta=8.6','padtype':'line','banda_aprox_conservada_Hz':[0,400],
              'nyquist_salida_Hz':500,'atenuacion_maxima_banda_stop_desde_500_dB':stop,
              'fraccion_potencia_entrada_500_1000_Hz':float(fraction),
              'limitacion':'Reduce contenido cercano a 450 Hz y superior. No se usa para las características principales. Bordes afectados por extensión y FIR.'}
    (root/'evidencias/parametros_temporales.json').write_text(json.dumps(temporal,indent=2,ensure_ascii=False),encoding='utf-8')
    fig,axes=plt.subplots(1,2,figsize=(11,3.7));a,b=56,56.15
    axes[0].plot(np.arange(int(a*FS),int(b*FS))/FS,x[int(a*FS):int(b*FS)],lw=.9,label='Original 2.000 Hz',color=COLORS[0])
    axes[0].plot(np.arange(int(a*1000),int(b*1000))/1000,reduced[int(a*1000):int(b*1000)],lw=.8,label='FIR + 1.000 Hz',color=COLORS[1])
    axes[0].set(xlabel='Tiempo (s)',ylabel='Amplitud (mV)',title='Comparación temporal del CH4');axes[0].legend(fontsize=8)
    axes[1].plot(resp_f,20*np.log10(np.maximum(np.abs(resp),1e-8)),color=COLORS[2]);axes[1].axvline(500,color='black',ls='--',lw=.8)
    axes[1].set(xlabel='Frecuencia (Hz)',ylabel='Ganancia FIR (dB)',ylim=(-120,5),xlim=(0,1000),title='Filtro antialias explícito de 161 coeficientes')
    fig.tight_layout();savefig(root,'comparacion_decimacion.png',fig)
    n=4000;t=np.arange(n)/FS;known=50.;synthetic=np.sin(2*np.pi*known*t)
    w=signal.windows.hann(n,sym=False);f=np.fft.rfftfreq(n,1/FS)
    amp=np.abs(np.fft.rfft((synthetic-synthetic.mean())*w))/w.sum();amp[1:-1]*=2
    peak=float(f[1+np.argmax(amp[1:])]);error=abs(peak-known)
    pd.DataFrame({'frecuencia_Hz':f,'amplitud_mV':amp}).to_csv(root/'evidencias/fft_sintetica.csv',index=False)
    assert error<=FS/n
    assert np.isclose(amp[np.argmax(amp)],1,atol=1e-8)
    # Caso independiente: 700 Hz se pliega a 300 Hz si se omite filtro al bajar a 1000 Hz.
    ts=np.arange(40000)/FS;tone=np.sin(2*np.pi*700*ts)
    filtered=signal.resample_poly(tone,1,2,window=taps,padtype='line')
    loss=20*np.log10(np.sqrt(np.mean(filtered[200:-200]**2))/np.sqrt(np.mean(tone[400:-400]**2)))
    unfiltered=tone[::2];freqout=np.fft.rfftfreq(len(unfiltered),1/1000)
    alias=float(freqout[np.argmax(np.abs(np.fft.rfft(unfiltered)))])
    assert alias == 300 and loss < -60
    validation={'tipo':'SINTÉTICA: verificación de código, separada de los datos reales',
                'fs_Hz':FS,'N':n,'duracion_s':n/FS,'f_conocida_Hz':known,'f_fft_Hz':peak,'error_Hz':error,
                'amplitud_entrada_mV':1,'amplitud_fft_mV':float(amp.max()),'delta_f_Hz':FS/n,
                'ventana':'Hann periódica; amplitud unilateral corregida por suma de ventana, DC y Nyquist sin duplicar',
                'prueba_alias_entrada_Hz':700,'alias_sin_filtro_Hz':alias,'atenuacion_tono_700_dB':float(loss),
                'pruebas_superadas':True}
    (root/'evidencias/validacion_sintetica.json').write_text(json.dumps(validation,indent=2,ensure_ascii=False),encoding='utf-8')
    fig,ax=plt.subplots(figsize=(7,2.8));ax.plot(f,amp,color=COLORS[0]);ax.set(xlim=(0,100),xlabel='Frecuencia (Hz)',ylabel='Amplitud (mV)',title=f'Prueba sintética FFT: {peak:g} Hz, error {error:g} Hz')
    fig.tight_layout();savefig(root,'validacion_fft_sintetica.png',fig)
    print(table.to_string(index=False));print(json.dumps(temporal,ensure_ascii=False,indent=2))
    print(json.dumps(validation,ensure_ascii=False,indent=2))
    return table,validation


if __name__ == '__main__':
    root=Path(__file__).resolve().parents[1]
    eda(root);characteristics(root);temporal_and_validation(root)
