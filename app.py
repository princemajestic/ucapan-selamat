import streamlit as str

# Mengatur judul halaman web
str.set_page_config(page_title="Pesan Semangat", page_icon="✨")

str.title("✨ Kotak Semangat untukmu ✨")
str.write("Tulis namamu di bawah ini untuk mengambil energi positif hari ini!")

# Membuat menu input nama yang bersih
nama = str.text_input("Masukkan nama Anda:", placeholder="Ketik nama di sini...")

# Ketika tombol diklik atau setelah mengetik nama
if nama:
    str.markdown("---")
    str.success(f"### Halo {nama}, this is little gift from me Nizamm tetap semangat ya praktikumnya zul wkwkkwk!")
    str.info("💡 **Ingat:** Jangan menyerah, hehe!")
    str.markdown("---")
