'use client'; // Add this line

import React, { useState, useEffect } from 'react';
import { useRouter } from 'next/navigation';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faEye, faEyeSlash, faCopy } from '@fortawesome/free-solid-svg-icons';
import './style.css'; // Ensure this path is correct
import { faArrowLeft } from '@fortawesome/free-solid-svg-icons';
import axios from 'axios';

function Wallet2() {
  const [isTextVisible, setIsTextVisible] = useState(false);
  const [isClient, setIsClient] = useState(false);
  const [isCheckboxChecked, setIsCheckboxChecked] = useState(false);
  const [randomWords, setRandomWords] = useState('');
  const router = useRouter();

  const wordList = [
  "abandon", "balance", "cathedral", "diligent", "eclipse", "fidelity", "gather", "horizon",
  "inspire", "jovial", "knight", "leverage", "modern", "navigate", "oracle", "pioneer",
  "quasar", "resolve", "synergy", "tactile", "unison", "vanguard", "wavelength", "xenon", 
  "yield", "zephyr", "apex", "brilliance", "catalyst", "dedication", "ethos", "fortitude", 
  "genesis", "harmony", "innovation", "journey", "keystone", "luminary", "momentum", 
  "nexus", "optimism", "precision", "quest", "resilience", "serenity", "trajectory", 
  "unity", "valor", "wisdom", "zenith"
];

  useEffect(() => {
    setIsClient(true);
    generateRandomWords();
  }, []);

  const generateRandomWords = () => {
    const shuffled = wordList.sort(() => 0.5 - Math.random());
    const selected = shuffled.slice(0, 12).join(' ');
    setRandomWords(selected);
    localStorage.setItem('recoveryWords', selected); // Store in localStorage
  };

  const toggleVisibility = () => {
    setIsTextVisible(!isTextVisible);
  };

  const handleCopyClick = () => {
    navigator.clipboard.writeText(randomWords).then(() => {
      alert('Text copied to clipboard!');
    }).catch(err => {
      console.error('Failed to copy text: ', err);
    });
  };

  const handleCheckboxChange = (event) => {
    setIsCheckboxChecked(event.target.checked);
  };

  const handleContinueClick = async () => {
    if (isCheckboxChecked) {
      const response = await axios.post('')
      router.push('./WalletSecretCode/success'); // Navigate to the success page
    } else {
      alert('Please check the checkbox before continuing.');
    }
  };

  return (
    <div className="wrapper">
      <span className="back-arrow" onClick={() => window.history.back()}>
        <FontAwesomeIcon icon={faArrowLeft} />
      </span>
      <h1 className="header">Back up your wallet</h1>
      <p className="description">
        Save these 12 words to a password manager, or write down and store in a secure place.
        Do not share with anyone.
      </p>
      <div className="textbox">
        <div className="text-line">
          {isClient && (isTextVisible ? randomWords : "• • • • • • • • • • • • • • • • • • • • • • • •  • • • • • • • • • • • • •  • • • • •")}
        </div>
        <div className="icon-container">
          <span className="icon" onClick={toggleVisibility}>
            <FontAwesomeIcon icon={isTextVisible ? faEye : faEyeSlash } />
          </span>
        </div>
      </div>
      <p className="description2">
        <FontAwesomeIcon icon={faCopy} className="copy-icon" onClick={handleCopyClick} />
        copy to clipboard
      </p>
      <div className="checkbox-container">
        <label>
          <input type="checkbox" className="checkbox" onChange={handleCheckboxChange} />
          I understand that if I lose my recovery phrase, I’ll lose all of the crypto in my wallet.
        </label>
      </div>
      <button className="continue-button" onClick={handleContinueClick}>Continue</button>
    </div>
  );
}

export default Wallet2;
