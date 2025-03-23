import streamlit as st
from .utils import lue_nimet_kuvasta, luo_sunnuntaikela_excel

def kela_ui():
    st.header("Sunnuntai Kela -ryhmäjako")
    ryhmien_maara = st.number_input("Kuinka monta ryhmää?", min_value=1, value=2, step=1)

    ryhmadata = []
    for i in range(ryhmien_maara):
        st.subheader(f"Ryhmä {i+1}")
        nimi = st.text_input(f"Ryhmä {i+1} nimi", key=f"nimi_{i}")
        tila = st.text_input(f"Ryhmä {i+1} kokoustila", key=f"tila_{i}")
        kuva = st.file_uploader(f"Lataa kuva ryhmän {i+1} nimilistasta", type=["png", "jpg", "jpeg"], key=f"kuva_{i}")

        nimet = []
        if kuva:
            nimet = lue_nimet_kuvasta(kuva)
            st.text_area("Esikatselu & muokkaa nimet (yksi per rivi):", value="\n".join(nimet), height=200, key=f"edit_{i}")

        if nimi and tila and kuva:
            nimet_muokattu = st.session_state.get(f"edit_{i}", "").splitlines()
            nimet_muokattu = [n.strip() for n in nimet_muokattu if n.strip()]
            ryhmadata.append({
                "nimi": nimi,
                "tila": tila,
                "nimet": nimet_muokattu
            })

    if len(ryhmadata) == ryhmien_maara and st.button("Luo Sunnuntai Kela Excel"):
        excel_bytes = luo_sunnuntaikela_excel(ryhmadata)
        st.success("Sunnuntai Kela -Excel luotu!")
        st.download_button("Lataa Excel", data=excel_bytes, file_name="sunnuntai_kela.xlsx", mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
