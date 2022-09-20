# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 15:12:05 2022

@author: usuario
"""

import streamlit as st

st.title("EL MEJOR DÍA DE TU VIDA")

my_text2 = st.text("SALVAME!")


my_text = st.text("Yo quería ser veterinario y aquí estoy, sinceramente que bien estaría con mis cabriñas!")

my_button = st.button("Quieres ser tu propio jefe?")

if my_button:
    st.title("Pues abra cadabra, tápate guarra!")

