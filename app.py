# =[Modules dan Packages]========================

from flask import Flask,render_template,request,jsonify
import pandas as pd
from joblib import load
import os

# =[Variabel Global]=============================

app   = Flask(__name__, static_url_path='/static')
#model = None

# =[Routing]=====================================

# [Routing untuk Halaman Utama atau Home]	
@app.route("/")
def beranda():
    return render_template('index.html')

# [Routing untuk API]    
@app.route("/api/deteksi", methods=['POST'])
def apiDeteksi():
    # Nilai default untuk variabel input atau features (X) ke model
    input_Harapan_Lama_Sekolahh = 5.0
    input_Pengeluaran_Perkapita = 9572
    input_Rerata_Lama_Sekolah = 7
    input_Usia_Harapan_Hidup = 70

    if request.method == 'POST':
        # Set nilai untuk variabel input atau features (X) berdasarkan input dari pengguna
        input_Harapan_Lama_Sekolahh = float(request.form['Harapan_Lama_Sekolahh'])
        input_Pengeluaran_Perkapita = float(request.form['Pengeluaran_Perkapita'])
        input_Rerata_Lama_Sekolah = float(request.form['Rerata_Lama_Sekolah'])
        input_Usia_Harapan_Hidup = float(request.form['Usia_Harapan_Hidup'])

        # Prediksi kelas atau spesies bunga iris berdasarkan data pengukuran yg diberikan pengguna
        df_test = pd.DataFrame(data={
            "Harapanlamasekolah": [input_Harapan_Lama_Sekolahh],
            "Pengeluaranperkapita": [input_Pengeluaran_Perkapita],
            "Reratalamasekolah": [input_Rerata_Lama_Sekolah],
            "Usiaharapanhidup": [input_Usia_Harapan_Hidup]
        })

        hasil_prediksi = model.predict(df_test[0:1])[0]

        # Set Path untuk gambar hasil prediksi
        if hasil_prediksi == 0:
            hasil_prediksi_label = "High"
            gambar_prediksi = '/static/images/2.png'
        elif hasil_prediksi == 1:
            hasil_prediksi_label = "Low"
            gambar_prediksi = '/static/images/4.png'
        elif hasil_prediksi == 2:
            hasil_prediksi_label = "Normal"
            gambar_prediksi = '/static/images/3.png'
        else:
            hasil_prediksi_label = "Very High"
            gambar_prediksi = '/static/images/1.png'

        # Return hasil prediksi dengan format JSON
        return jsonify({
            "prediksi": hasil_prediksi_label,
            "gambar_prediksi": gambar_prediksi
        })

# =[Main]========================================

if __name__ == '__main__':
	
	# Load model yang telah ditraining
	model = load('model_ipm_rf.model')

	# Run Flask di localhost 
	app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 8080)))
	
	


