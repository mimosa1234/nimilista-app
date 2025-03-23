
# Ryhmalaatturi – Nimilista- ja ryhmätyökalu Streamlitillä

Tämä sovellus auttaa luomaan ja hallinnoimaan nimilistoja eri tarkoituksiin. Sovellus tukee sekä **"HKP Excel"** -muotoilua että **"Sunnuntai Kela"** -ryhmien hallintaa. Kaikki toimii kätevästi selaimessa Streamlitin avulla.

## 🚀 Sovelluksen käynnistys

1. Asenna riippuvuudet:
```bash
pip install -r requirements.txt
```

2. Käynnistä sovellus:
```bash
streamlit run app.py
```

3. Avaa selaimessa osoite:
```
http://localhost:8501
```

## 🔧 Toiminnot

### 🟦 HKP Excel
- Luo nimilistan Excel-muotoon, jossa sarakkeet:
  `Nimi`, `hkp a`, `hkp l`, `R aik`, `U aik`, `R L`, `U L`
- Automaattinen summakaava jokaiselle sarakkeelle
- Voit ladata nimet PDF- tai Excel-tiedostosta

### 🟩 Sunnuntai Kela
- Käyttäjä määrittää montako ryhmää luodaan
- Jokaiselle ryhmälle annetaan nimi, kokoustila ja nimilista
- Nimet voidaan ladata **kuvasta (PNG/JPG)** OCR:n avulla
- Tuloksena syntyy Excel-tiedosto, jossa ryhmät listattu siististi

## 🧰 Teknologiat

- Python 3
- Streamlit
- pandas
- PyPDF2
- pytesseract
- openpyxl
- Pillow (kuvien käsittelyyn)

## 📝 Lisähuomiot

- OCR toimii parhaiten, kun kuvat ovat selkeitä ja nimet erottuvat hyvin.
- Jos suomenkielinen OCR tarvitaan, voit lisätä `fin.traineddata` Tesseractin tessdata-kansioon.

---

**Projektin tekijä:** [@mimosa1234](https://github.com/mimosa1234)
