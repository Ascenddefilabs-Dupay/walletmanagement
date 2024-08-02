import React from 'react';
import { useNavigate } from 'react-router-dom';
import './WalletReady.css';

function WalletReady() {

  const handleClaim = () => {
    navigate('/claim');
  };

  const handleLater = () => {
    navigate('/later');
  };

  return (
    <div className="wallet-container">
      <div className="wallet-content">
        <div className="checkmark">✔️</div>
        <h1>Your wallet is ready</h1>
        <p>Join and claim your free username.</p>
        <button className="claim-button" onClick={handleClaim}>Claim for free</button>
        <button className="later-button" onClick={handleLater}>I'll do it later</button>
      </div>
    </div>
  );
}

export default WalletReady;
