import streamlit as st
from valinta import valitse_toiminto
from hkp.hkp_handler import hkp_ui
from sunnuntai_kela.kela_handler import kela_ui

valinta = valitse_toiminto()

if valinta == "HKP Excel":
    hkp_ui()
elif valinta == "Sunnuntai Kela":
    kela_ui()
