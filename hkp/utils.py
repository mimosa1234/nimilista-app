import pandas as pd
import PyPDF2
from io import BytesIO

def lue_pdf_nimet(uploaded_file):
    nimet = []
    reader = PyPDF2.PdfReader(uploaded_file)
    for sivu in reader.pages:
        teksti = sivu.extract_text()
        if teksti:
            for rivi in teksti.split("\n"):
                if " " in rivi:
                    nimet.append(rivi.strip())
    return nimet

def lue_excel_nimet(uploaded_file):
    df = pd.read_excel(uploaded_file)
    return df.iloc[:, 0].dropna().tolist()

def luo_hkp_excel(nimilista):
    columns = ['Nimi', 'hkp a', 'hkp l', 'R aik', 'U aik', 'R L', 'U L']
    df = pd.DataFrame(nimilista, columns=['Nimi'])
    for col in columns[1:]:
        df[col] = ''

    sum_row = ['=SUM(B2:B{})'.format(len(df)+1),
               '=SUM(C2:C{})'.format(len(df)+1),
               '=SUM(D2:D{})'.format(len(df)+1),
               '=SUM(E2:E{})'.format(len(df)+1),
               '=SUM(F2:F{})'.format(len(df)+1),
               '=SUM(G2:G{})'.format(len(df)+1)]
    df.loc[len(df)] = [''] * len(columns)
    df.loc[len(df)] = ['Yhteensä'] + sum_row

    buffer = BytesIO()
    with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Nimilista')
        sheet = writer.sheets['Nimilista']
        sheet.freeze_panes = 'A2'
    buffer.seek(0)
    return buffer
