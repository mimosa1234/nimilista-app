import streamlit as st
from .utils import lue_pdf_nimet, lue_excel_nimet, luo_hkp_excel

def hkp_ui():
    st.header("HKP Excel -muotoilu")
    tiedosto = st.file_uploader("Lataa PDF- tai Excel-nimilista", type=["pdf", "xlsx"])
    maara = st.number_input("Kuinka monta nimeä mukaan?", min_value=1, value=10, step=1)

    if st.button("Luo HKP Excel"):
        if tiedosto:
            if tiedosto.name.endswith(".pdf"):
                nimet = lue_pdf_nimet(tiedosto)
            elif tiedosto.name.endswith(".xlsx"):
                nimet = lue_excel_nimet(tiedosto)
            else:
                st.error("Tiedostotyyppi ei ole tuettu.")
                return

            nimet = nimet[:maara]
            excel_bytes = luo_hkp_excel(nimet)

            st.success("Excel-tiedosto luotu!")
            st.download_button("Lataa Excel", data=excel_bytes, file_name="HKP_nimilista.xlsx", mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
        else:
            st.warning("Lataa tiedosto ensin.")
