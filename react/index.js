import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';

const app = document.getElementById('react');
ReactDOM.render(
    <React.StrictMode>
        <App />
    </React.StrictMode>,
    app,
);
