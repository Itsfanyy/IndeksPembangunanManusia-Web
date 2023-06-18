# Flask API for IPM Detection

This web application is designed to classify the Human Development Index (HDI) into four classes based on certain input features. It utilizes a pre-trained Random Forest model to make predictions on user inputs.

## Modules and Packages

The following modules and packages are required for running the web application:

- Flask
- pandas
- joblib
- os

Make sure you have these packages installed in your environment before running the application.

## Global Variables

- `app`: Flask application object.

## Routing

### Home Page

- Route: `/`
- Method: GET
- Description: Renders the index.html template for the home page.

### API Endpoint

- Route: `/api/deteksi`
- Method: POST
- Description: Accepts POST requests containing user inputs and returns the predicted HDI class and corresponding image path.

#### Parameters

The API expects the following parameters in the request body:

- `Harapan_Lama_Sekolahh` (float): Average years of schooling.
- `Pengeluaran_Perkapita` (float): Per capita expenditure.
- `Rerata_Lama_Sekolah` (float): Mean years of schooling.
- `Usia_Harapan_Hidup` (float): Life expectancy at birth.

#### Response

The API returns a JSON response containing the predicted HDI class and the corresponding image path.

Example response:

```json
{
  "prediksi": "High",
  "gambar_prediksi": "/static/images/2.png"
}
```

## Main

The main part of the code loads the pre-trained Random Forest model and starts the Flask application.

Make sure to specify the correct path to your pre-trained model file (`model_ipm_rf.model`) before running the application.

To run the web application, execute the script in your Python environment.

```bash
python app.py
```

The application will be available at `http://localhost:8080`.

Note: The application can also be deployed on a remote server by modifying the `host` and `port` arguments in the `app.run()` function.
