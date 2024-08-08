"use client"
import React from 'react';
import './Account.css';

const AddAccount = () => {

    const handleClose = () => {
        window.location.href = './';
      };

    const handleImport = () => {
      window.location.href = '../WalletSecretCode';
    };

  return (
    <div className="wallet-manager">
    <div className="add-account-container">
            <div className="add-account-header">
                <h1>Add Account</h1>
            </div>
            <div className="add-account-body">
                {/* <button className="add-account-button ledger">Set up Ledger</button> */}
                {/* <div className="divider">CREATE NEW</div>
                <button className="add-account-button">Create a new Passphrase Account</button> */}
                <div className="divider">IMPORT EXISTING ACCOUNTS</div>
                <button className="add-account-button" onClick={handleImport}>Import Passphrase</button>
                <button className="add-account-button">Import Private Key</button>
            </div>
            <button className="close-button" onClick={handleClose}>&times;</button>
            </div>
    </div>
  );
}

export default AddAccount;
