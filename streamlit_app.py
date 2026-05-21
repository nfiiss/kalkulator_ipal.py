import streamlit as st

st.title("KALKULATOR IPAL")
import streamlit as st

# =========================
# JUDUL
# =========================

st.title("Kalkulator IPAL Sederhana")
st.write("Perhitungan efisiensi penyisihan BOD dan volume bak aerasi")

# =========================
# INPUT
# =========================

st.header("Input Data")

Q = st.number_input(
    "Debit limbah (m3/hari)",
    min_value=0.0,
    value=120.0
)

bod_awal = st.number_input(
    "BOD awal (mg/L)",
    min_value=0.0,
    value=300.0
)

bod_target = st.number_input(
    "Target BOD akhir (mg/L)",
    min_value=0.0,
    value=50.0
)

hrt = st.number_input(
    "Waktu tinggal / HRT (jam)",
    min_value=0.0,
    value=8.0
)

# =========================
# TOMBOL HITUNG
# =========================

if st.button("Hitung"):

    # =========================
    # PERHITUNGAN
    # =========================

    efisiensi = ((bod_awal - bod_target) / bod_awal) * 100

    volume = Q * (hrt / 24)

    bod_hilang = bod_awal - bod_target

    oksigen = Q * bod_hilang / 1000

    # =========================
    # OUTPUT
    # =========================

    st.header("Hasil Perhitungan")

    st.success(f"Efisiensi penyisihan BOD : {efisiensi:.2f}%")

    st.info(f"Volume bak aerasi : {volume:.2f} m3")

    st.write(f"BOD yang dihilangkan : {bod_hilang:.2f} mg/L")

    st.write(f"Kebutuhan oksigen : {oksigen:.2f} kg O2/hari")

    # =========================
    # STATUS BAKU MUTU
    # =========================

    baku_mutu = 50

    if bod_target <= baku_mutu:
        st.success("Memenuhi baku mutu")
    else:
        st.error("Tidak memenuhi baku mutu") 

