import React, { useState } from 'react';
import './RecoveryPhraseForm.css';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faEye, faEyeSlash } from '@fortawesome/free-solid-svg-icons';
import axios from 'axios';

const RecoveryPhraseForm = () => {
    const [phrases, setPhrases] = useState(Array(12).fill(''));
    const [showPhrases, setShowPhrases] = useState(Array(12).fill(false));
    const [errorMessage, setErrorMessage] = useState('');

    const handleChange = (index, value) => {
        const newPhrases = [...phrases];
        newPhrases[index] = value;
        setPhrases(newPhrases);
    };

    const toggleVisibility = (index) => {
        const newShowPhrases = [...showPhrases];
        newShowPhrases[index] = !newShowPhrases[index];
        setShowPhrases(newShowPhrases);
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            console.log(phrases);
            
            const response = await axios.post('http://127.0.0.1:8000/api/check-recovery-phrase/', {
                phrases,
            });

            if (response.data.success) {
                // Extract the wallet_id from the response
                const { wallet_id } = response.data;
                // Store wallet_id in sessionStorage and redirect to the next page
                sessionStorage.setItem('wallet_id', wallet_id);
                console.log(wallet_id);
                setTimeout(() => {
                    window.location.href = './UpdatePassword/';
                }, 2000);
                
            } else {
                setErrorMessage('Password words are incorrect');
            }
        } catch (error) {
            console.error('There was an error!', error);
            setErrorMessage('An error occurred. Please try again.');
        }
    };

    return (
        <div className="wallet-manager">
            <div className="recovery-phrase-form">
                <h2>WALLET SETUP</h2>
                <h3>Add Existing Account</h3>
                <p>Enter your 12-word Recovery Phrase</p>
                <form onSubmit={handleSubmit}>
                    <div className="phrase-grid">
                        {phrases.map((phrase, index) => (
                            <div key={index} className="phrase-input">
                                <div className="password-input">
                                    <input
                                        type={showPhrases[index] ? 'text' : 'password'}
                                        value={phrase}
                                        onChange={(e) => handleChange(index, e.target.value)}
                                        placeholder="Password"
                                    />
                                    <button
                                        type="button"
                                        onClick={() => toggleVisibility(index)}
                                    >
                                        <FontAwesomeIcon
                                            icon={showPhrases[index] ? faEye : faEyeSlash}
                                        />
                                    </button>
                                </div>
                            </div>
                        ))}
                    </div>
                    {errorMessage && <p className="error">{errorMessage}</p>}
                    <button type="submit">Add Account</button>
                </form>
                <button className="cancel" onClick={() => window.history.back()}>Cancel</button>
            </div>
        </div>
    );
};

export default RecoveryPhraseForm;
