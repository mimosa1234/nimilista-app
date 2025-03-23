from PIL import Image
import pytesseract
import pandas as pd
from io import BytesIO

def lue_nimet_kuvasta(kuvatiedosto):
    image = Image.open(kuvatiedosto)
    teksti = pytesseract.image_to_string(image)
    rivit = [rivi.strip() for rivi in teksti.split('\n') if rivi.strip()]
    nimet = [rivi for rivi in rivit if " " in rivi]
    return nimet

def luo_sunnuntaikela_excel(ryhmadata):
    rows = []
    for ryhma in ryhmadata:
        rows.append([f"Ryhmä: {ryhma['nimi']} | Tila: {ryhma['tila']}"])
        for nimi in ryhma['nimet']:
            rows.append([nimi])
        rows.append([""])

    df = pd.DataFrame(rows, columns=[""])

    buffer = BytesIO()
    with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Sunnuntai Kela')
        sheet = writer.sheets['Sunnuntai Kela']
        sheet.freeze_panes = 'A2'
    buffer.seek(0)
    return buffer
