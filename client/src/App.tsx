import { BrowserRouter, Routes, Route } from 'react-router'
import HomePage from './pages/HomePage'
import VideoPage from './pages/VideoPage'
import './App.css'

function App() {

  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<HomePage/>}/>
        <Route path="/video/:pk" element={<VideoPage />}/>
      </Routes>
    </BrowserRouter>
  );
}

export default App
