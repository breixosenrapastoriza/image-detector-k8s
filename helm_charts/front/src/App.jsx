import { useState } from 'react';
import './App.css';

function App() {
  const [image, setImage] = useState(null);
  const [preview, setPreview] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleImageUpload = (e) => {
    const file = e.target.files[0];
    if (file) {
      setImage(file);
      setPreview(URL.createObjectURL(file));
      setResult(null);
    }
  };

  const handleAnalyze = async () => {
    if (!image) {
      alert('Por favor, selecciona una imagen.');
      return;
    }

    setLoading(true);
    const formData = new FormData();
    formData.append('file', image);

    try {
      const response = await fetch('/api/predict', {
        method: 'POST',
        body: formData,
      });

      if (!response.ok) throw new Error('Error en el backend');

      const data = await response.json();
      setResult(data);
    } catch (error) {
      console.error(error);
      alert('Error al procesar la imagen.');
    } finally {
      setLoading(false);
    }
  };

  const reset = () => {
    setImage(null);
    setPreview(null);
    setResult(null);
    setLoading(false);
  };

  return (
  <div className="app-container">
    <div className="card two-column-card">
      {/* Columna izquierda: Imagen o preview */}
      <div className="card-column left-column">
        {preview ? (
          <img src={preview} alt="preview" className="preview-large" />
        ) : (
          <div className="preview-placeholder">Vista previa</div>
        )}
      </div>

      {/* Columna derecha: formulario o resultados */}
      <div className="card-column right-column">
        {!result ? (
          <>
            <h1>Descubre lo que hay en tu imagen</h1>
            <label htmlFor="imageUpload" className="custom-file-upload">
              Seleccionar imagen
            </label>
            <input
              id="imageUpload"
              type="file"
              accept="image/*"
              onChange={handleImageUpload}
              style={{ display: 'none' }}
            />

            {image && (
              <button onClick={handleAnalyze} disabled={loading}>
                {loading ? 'Analizando...' : 'Analizar'}
              </button>
            )}
          </>
        ) : (
          <>
            <h2>Resultado: {result.Description}</h2>
            <p><strong>Código:</strong> {result['Predicted class']}</p>
            <p><strong>Probabilidad:</strong> {result.Probability}</p>
            <button onClick={reset}>Analizar otra imagen</button>
          </>
        )}
      </div>
    </div>
  </div>
);

}

export default App;
