import { useState, useRef } from 'react';
import { UploadCloud, FileText, CheckCircle, AlertCircle } from 'lucide-react';
import './FileUpload.css';

export default function FileUpload({ onUploadSuccess }) {
  const [isDragging, setIsDragging] = useState(false);
  const [file, setFile] = useState(null);
  const [status, setStatus] = useState('idle'); // idle, uploading, success, error
  const [message, setMessage] = useState('');
  const fileInputRef = useRef(null);

  const handleDragOver = (e) => {
    e.preventDefault();
    setIsDragging(true);
  };

  const handleDragLeave = (e) => {
    e.preventDefault();
    setIsDragging(false);
  };

  const handleDrop = (e) => {
    e.preventDefault();
    setIsDragging(false);
    const droppedFile = e.dataTransfer.files[0];
    validateAndSetFile(droppedFile);
  };

  const handleFileChange = (e) => {
    const selectedFile = e.target.files[0];
    validateAndSetFile(selectedFile);
  };

  const validateAndSetFile = (selectedFile) => {
    if (selectedFile && selectedFile.type === 'application/pdf') {
      setFile(selectedFile);
      setStatus('idle');
      setMessage('');
    } else {
      setStatus('error');
      setMessage('Please select a valid PDF file.');
    }
  };

  const uploadFile = async () => {
    if (!file) return;

    setStatus('uploading');
    setMessage('Uploading and processing...');

    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await fetch('/upload/', {
        method: 'POST',
        body: formData,
      });

      const data = await response.json().catch(() => ({}));

      if (!response.ok) {
        throw new Error(data.detail || 'Upload failed');
      }

      setStatus('success');
      setMessage(data.message || 'PDF uploaded and processed successfully.');
      if (onUploadSuccess) onUploadSuccess();
    } catch (err) {
      setStatus('error');
      setMessage(err?.message || 'Error uploading file. Please try again.');
    }
  };

  return (
    <div className="glass-panel file-upload-container">
      <div className="file-upload-header">
        <h2>Upload Policy Document</h2>
        <p>Upload your insurance PDF to start asking questions.</p>
      </div>

      <div 
        className={`drop-zone ${isDragging ? 'dragging' : ''} ${file ? 'has-file' : ''}`}
        onDragOver={handleDragOver}
        onDragLeave={handleDragLeave}
        onDrop={handleDrop}
        onClick={() => fileInputRef.current?.click()}
      >
        <input 
          type="file" 
          ref={fileInputRef} 
          onChange={handleFileChange} 
          accept="application/pdf" 
          hidden 
        />
        
        {!file ? (
          <div className="drop-zone-content">
            <UploadCloud size={48} className="upload-icon" />
            <p><strong>Click to upload</strong> or drag and drop</p>
            <span className="file-hint">PDF (Max 10MB)</span>
          </div>
        ) : (
          <div className="file-info">
            <FileText size={40} className="file-icon" />
            <div className="file-details">
              <span className="file-name">{file.name}</span>
              <span className="file-size">{(file.size / 1024 / 1024).toFixed(2)} MB</span>
            </div>
          </div>
        )}
      </div>

      {file && status !== 'success' && (
        <button 
          className="upload-btn" 
          onClick={uploadFile}
          disabled={status === 'uploading'}
        >
          {status === 'uploading' ? (
            <span className="uploading-text">
              <span className="spinner"></span> Processing...
            </span>
          ) : 'Process Document'}
        </button>
      )}

      {status === 'success' && (
        <div className="status-message success">
          <CheckCircle size={20} />
          <span>{message}</span>
        </div>
      )}

      {status === 'error' && (
        <div className="status-message error">
          <AlertCircle size={20} />
          <span>{message}</span>
        </div>
      )}
    </div>
  );
}
