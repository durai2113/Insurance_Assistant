import { useState, useRef, useEffect } from 'react';
import { Send, Bot, User, Loader2 } from 'lucide-react';
import './ChatBox.css';

export default function ChatBox({ sessionId }) {
  const [messages, setMessages] = useState([
    {
      id: 'welcome',
      type: 'ai',
      text: "Hello! I'm your Insurance Policy Assistant. I've analyzed your document. What would you like to know?"
    }
  ]);
  const [input, setInput] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const messagesEndRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const handleSend = async (e) => {
    e?.preventDefault();
    
    if (!input.trim() || isLoading) return;

    const userMessage = input.trim();
    setInput('');
    setMessages(prev => [...prev, { id: Date.now().toString(), type: 'user', text: userMessage }]);
    setIsLoading(true);

    try {
      const response = await fetch('/chat/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          session_id: sessionId || 'default-session',
          question: userMessage
        })
      });

      if (!response.ok) throw new Error('Chat request failed');

      const data = await response.json();
      
      setMessages(prev => [...prev, {
        id: (Date.now() + 1).toString(),
        type: 'ai',
        text: data.answer
      }]);
    } catch (error) {
      setMessages(prev => [...prev, {
        id: (Date.now() + 1).toString(),
        type: 'ai',
        text: "I'm sorry, I encountered an error while processing your request. Please try again.",
        isError: true
      }]);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="glass-panel chat-container">
      <div className="chat-header">
        <div className="ai-avatar-small">
          <Bot size={20} />
        </div>
        <h2>Assistant</h2>
      </div>

      <div className="chat-messages">
        {messages.map(msg => (
          <div key={msg.id} className={`message-wrapper ${msg.type}`}>
            <div className={`message-avatar ${msg.type}`}>
              {msg.type === 'ai' ? <Bot size={18} /> : <User size={18} />}
            </div>
            <div className={`message-bubble ${msg.type} ${msg.isError ? 'error' : ''}`}>
              {msg.text}
            </div>
          </div>
        ))}
        {isLoading && (
          <div className="message-wrapper ai">
            <div className="message-avatar ai">
              <Bot size={18} />
            </div>
            <div className="message-bubble ai typing">
              <div className="typing-dot"></div>
              <div className="typing-dot"></div>
              <div className="typing-dot"></div>
            </div>
          </div>
        )}
        <div ref={messagesEndRef} />
      </div>

      <form className="chat-input-form" onSubmit={handleSend}>
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Ask a question about your policy..."
          disabled={isLoading}
        />
        <button type="submit" disabled={!input.trim() || isLoading} className="send-btn">
          {isLoading ? <Loader2 size={20} className="spin" /> : <Send size={20} />}
        </button>
      </form>
    </div>
  );
}
