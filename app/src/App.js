import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Home from './pages/home'; 
import Sobre from './pages/sobre'; 
import Login from './pages/login';
import Cadastro from './pages/cadastro';
import Dados from './pages/dados';

const App = () => {
    return (
        <Router>
            <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/sobre" element={<Sobre />} />
                <Route path="/login" element={<Login />} />
                <Route path="/cadastro" element={<Cadastro />} />
                <Route path="/dados" element={<Dados />} />
            </Routes>
        </Router>
    );
};

export default App;
