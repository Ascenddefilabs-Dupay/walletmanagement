import React, { useState } from 'react';
import axios from 'axios';
import './PasswordForm.css';
import ProgressBar from '../WalletCreation/ProgressBar';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faEye, faEyeSlash } from '@fortawesome/free-solid-svg-icons';

const PasswordForm = () => {
    const [password, setPassword] = useState('');
    const [verifyPassword, setVerifyPassword] = useState('');
    const [passwordMatch, setPasswordMatch] = useState(false);
    const [passwordStrength, setPasswordStrength] = useState('');
    const [showPassword, setShowPassword] = useState(false);
    const [isChecked, setIsChecked] = useState(false);
    const [modalContent, setModalContent] = useState('');
    const [showModal, setShowModal] = useState(false);
    const [message, setMessage] = useState(''); // State for messages
    const [messageType, setMessageType] = useState(''); // State for message type ('success' or 'error')

    const handlePasswordChange = (e) => {
        const value = e.target.value;
        setPassword(value);

        // Password strength logic
        if (value.length > 8) {
            setPasswordStrength('good');
        } else if (value.length > 4) {
            setPasswordStrength('medium');
        } else {
            setPasswordStrength('weak');
        }
    };

    const handleLeftArrowClick = () => {
        window.location.href = './WalletCreation';
    };

    const handleVerifyPasswordChange = (e) => {
        const value = e.target.value;
        setVerifyPassword(value);
        setPasswordMatch(password === value);
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        if (passwordMatch && isChecked) {
            try {
                const response = await axios.post('http://127.0.0.1:8000/api/password/', { password });
                setMessage('Password saved :)');
                setMessageType('success');
                window.location.href = 'http://localhost:3000/WalletManagement/WalletSubmit';
            } catch (error) {
                setMessage('Password not saved!');
                setMessageType('error');
                console.error('Error saving password', error);
            }
        }
    };

    const showTerms = () => {
        setModalContent("Sample Terms and Conditions:\n\n1. You must be at least 18 years old to use this service.\n2. You agree to use the service only for lawful purposes.\n3. We reserve the right to terminate your account if you violate these terms.");
        setShowModal(true);
    };

    const showPrivacyPolicy = () => {
        setModalContent("Sample Privacy Policy:\n\n1. We collect personal data to improve our services.\n2. Your data will not be shared with third parties without your consent.\n3. We use secure methods to protect your data from unauthorized access.");
        setShowModal(true);
    };

    const closeModal = () => {
        setShowModal(false);
        setModalContent('');
    };

    return (
        <div className="wallet-manager">
            <div className="card">
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
                <h1 className='heading'>Create Password</h1>
                <p>Set a password to unlock your wallet each time you use your computer. It can't be used to recover your wallet.</p>
                <form onSubmit={handleSubmit}>
                    <div>
                        <label>Password</label>
                        <div className="password-input">
                            <input
                                type={showPassword ? 'text' : 'password'}
                                value={password}
                                onChange={handlePasswordChange}
                            />
                            <button type="button" onClick={() => setShowPassword(!showPassword)}>
                                <FontAwesomeIcon icon={showPassword ? faEye : faEyeSlash} />
                            </button>
                        </div>
                        <div className={`strength ${passwordStrength}`}>
                            {[...Array(5)].map((_, i) => (
                                <div key={i} className="strength-bar"></div>
                            ))}
                            {passwordStrength.charAt(0).toUpperCase() + passwordStrength.slice(1)}
                        </div>
                    </div>
                    <div>
                        <label>Verify Password</label>
                        <div className="password-input">
                            <input
                                type={showPassword ? 'text' : 'password'}
                                value={verifyPassword}
                                onChange={handleVerifyPasswordChange}
                                id="password-input-field"
                            />
                            <button
                                type="button"
                                onClick={() => setShowPassword(!showPassword)}
                                className="toggle-password-button"
                            >
                                <FontAwesomeIcon icon={showPassword ? faEye : faEyeSlash} />
                            </button>
                        </div>
                        <div className="verify">{passwordMatch ? "It's a match!" : 'Passwords do not match'}</div>
                    </div>
                    <div className='terms'>
                        <input
                            type="checkbox"
                            checked={isChecked}
                            onChange={() => setIsChecked(!isChecked)}
                        />
                        <label className='cond'>
                            I agree to the <a href="#terms" onClick={(e) => { e.preventDefault(); showTerms(); }}>terms</a> and <a href="#privacy-policy" onClick={(e) => { e.preventDefault(); showPrivacyPolicy(); }}>privacy policy</a>
                        </label>
                    </div>
                    <button type="submit" disabled={!passwordMatch || !isChecked}>Submit</button>
                </form>
                {message && (
                    <div className={`message ${messageType}`}>
                        {message}
                    </div>
                )}
            </div>

            {showModal && (
                <div className="modal">
                    <div className="modal-content">
                        <span className="close-button" onClick={closeModal}>×</span>
                        <pre>{modalContent}</pre>
                    </div>
                </div>
            )}
        </div>
    );
};

export default PasswordForm;
