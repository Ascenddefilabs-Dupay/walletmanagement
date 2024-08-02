import React from 'react';
import { useNavigate } from 'react-router-dom';
import './WalletManager.css';


const WalletManager = () => {

  const handleCreateNewWallet = () => {
    navigate('/create-new-wallet');
  };

  const handleExistingWallet = () => {
    navigate('/existing-wallet');
  };

  return (
    <div className="wallet-manager"><br/>
      <div className="wallet-icon">
        <img src='/wallet-image1.jpg' alt="DeFi Icon"/>
      </div><br/>
      <h1>Manage your<br /> DeFi</h1>
      <button onClick={handleCreateNewWallet} className="create-wallet-button">Create new wallet
      </button>
      <button onClick={handleExistingWallet} className="existing-wallet-button">
        I already have a wallet
      </button>
    </div>
  );
};

export default WalletManager;
