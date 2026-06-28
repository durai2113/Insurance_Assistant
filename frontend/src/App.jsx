import { useState } from 'react'
import { ShieldCheck } from 'lucide-react'
import FileUpload from './components/FileUpload'
import ChatBox from './components/ChatBox'
import './App.css'

function App() {
  const [hasUploaded, setHasUploaded] = useState(false);
  const [sessionId] = useState(
    () => `session-${crypto.randomUUID()}`
  );

  return (
    <div className="app-layout">
      <nav className="sidebar glass-panel">
        <div className="brand">
          <div className="logo">
            <ShieldCheck size={28} />
          </div>
          <h1>Insurance Assistant</h1>
        </div>
        
        <div className="nav-info">
          <p>Welcome to your intelligent insurance policy assistant. Upload a document to get started.</p>
        </div>
      </nav>

      <main className="main-content">
        <div className="dashboard-grid">
          <div className="upload-section">
            <FileUpload onUploadSuccess={() => setHasUploaded(true)} />
          </div>
          
          <div className={`chat-section ${!hasUploaded ? 'disabled' : ''}`}>
            {!hasUploaded && (
              <div className="chat-overlay">
                <p>Upload a policy document first to start chatting.</p>
              </div>
            )}
            <ChatBox sessionId={sessionId} />
          </div>
        </div>
      </main>
    </div>
  )
}

export default App
