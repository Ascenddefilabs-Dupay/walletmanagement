import React from 'react';
import './WalletManager.css';
import ProgressBar from './ProgressBar';

const WalletManager = () => {

  const handleCreateNewWallet = () => {
    window.location.href = './WalletSecretCode';
  };

  const handleExistingWallet = () => {
    window.location.href = '/existing-wallet';
  };

  const handleLeftArrowClick = () => {
    window.location.href = '/create-new-wallet';
  };

  return (
    <div className="wallet-manager">
      <div className='card'>
        <div className="container">
          <div className="column left" onClick={handleLeftArrowClick}>
            ←
          </div>
          <div className="column middle">
            <ProgressBar currentStep={1} totalSteps={4} />
          </div>
          <div className="column right">
            {/* Right column content */}
          </div>
        </div>
        <div className="wallet-icon">
          <img src='/wallet-image1.jpg' alt="DeFi Icon" />
        </div><br />
        <h1>Manage your<br /> DeFi</h1>
        <button onClick={handleCreateNewWallet} className="create-wallet-button">
          Create new wallet
        </button>
        <button onClick={handleExistingWallet} className="existing-wallet-button">
          I already have a wallet
        </button>
      </div>
    </div>
  );
};

export default WalletManager;
