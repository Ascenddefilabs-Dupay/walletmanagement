'use client';
import ProgressBar from '../WalletCreation/ProgressBar';
import React, { useEffect, useState } from 'react';
import { FaArrowLeft } from "react-icons/fa";
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import './style.css';
import axios from 'axios';

const SuccessPage: React.FC = () => {
    const [recoveryWords, setRecoveryWords] = useState<string[]>([]);
    const [shuffledWords, setShuffledWords] = useState<string[]>([]);
    const [selectedIndexes, setSelectedIndexes] = useState<number[]>([]);
    const [firstSelectedIndex, setFirstSelectedIndex] = useState<number | null>(null);
    const [lastSelectedIndex, setLastSelectedIndex] = useState<number | null>(null);
    const [isSuccess, setIsSuccess] = useState<boolean | null>(null);

    useEffect(() => {
        const words = localStorage.getItem('recoveryWords');
        if (words) {
            const wordArray = words.split(' ');
            setRecoveryWords(wordArray);
            setShuffledWords(shuffleArray(wordArray));
        }
    }, []);

    const shuffleArray = (array: string[]) => {
        const shuffled = array.slice();
        for (let i = shuffled.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]];
        }
        return shuffled;
    };

    const handleButtonClick = (index: number) => {
        if (selectedIndexes.includes(index)) {
            const updatedIndexes = selectedIndexes.filter(i => i !== index);
            setSelectedIndexes(updatedIndexes);

            if (index === firstSelectedIndex) {
                setFirstSelectedIndex(null);
            }

            if (index === lastSelectedIndex) {
                setLastSelectedIndex(null);
            }
        } else {
            if (selectedIndexes.length === 0) {
                setSelectedIndexes([index]);
                setFirstSelectedIndex(index);
            } else if (selectedIndexes.length === 1 && !selectedIndexes.includes(index)) {
                setSelectedIndexes([...selectedIndexes, index]);
                setLastSelectedIndex(index);
            }
        }
    };

    const handleLeftArrowClick = () => {
        window.location.href = '../WalletSecretCode';
    };

    const handleSubmit = async () => {
        if (firstSelectedIndex !== null && lastSelectedIndex !== null) {
            const firstWord = shuffledWords[firstSelectedIndex];
            const lastWord = shuffledWords[lastSelectedIndex];

            const expectedFirstWord = recoveryWords[0];
            const expectedLastWord = recoveryWords[recoveryWords.length - 1];

            const isCorrect = 
                firstWord.toLowerCase() === expectedFirstWord.toLowerCase() &&
                lastWord.toLowerCase() === expectedLastWord.toLowerCase();

            if (isCorrect) {
                setIsSuccess(true);
                try {
                    await axios.post('http://127.0.0.1:8000/api/recovery-phrase/', { phrase: recoveryWords.join(' ') });
                    window.location.href = '../CreatePassword';
                } catch (error) {
                    console.error('Error saving phrase:', error);
                    alert('Failed to save the recovery phrase.');
                }
            } else {
                setIsSuccess(false);
            }
        }
    };

    return (
        <div className="success-wrapper">
            <div className="container">
                <div className="column left" onClick={handleLeftArrowClick}>
                    <FaArrowLeft />
                </div>
                <div className="column middle">
                    <ProgressBar currentStep={3} totalSteps={4} />
                </div>
                <div className="column right">
                    {/* Right column content */}
                </div>
            </div>
            <div className="success-header">
                You saved it, right?
            </div>
            <div className="success-paragraph">
                Verify that you saved your secret recovery phrase by clicking on the first (1st) then last (12th) word.
            </div>
            <div className="word-buttons-container">
                {Array.from({ length: 6 }).map((_, rowIndex) => (
                    <div key={rowIndex} className="word-button-row">
                        {Array.from({ length: 4 }).map((_, colIndex) => {
                            const isEvenRow = (rowIndex % 2) === 1;
                            const shouldRenderButton = (isEvenRow && (colIndex === 1 || colIndex === 3)) || (!isEvenRow && (colIndex === 0 || colIndex === 2));
                            const wordIndex = rowIndex * 2 + (shouldRenderButton ? Math.floor(colIndex / 2) : -1);

                            return (
                                <div key={colIndex} className={`word-button-placeholder col-${colIndex + 1}`}>
                                    {shouldRenderButton && wordIndex < shuffledWords.length && (
                                        <button
                                            className={`word-button ${selectedIndexes.includes(wordIndex) ? 'selected' : ''}`}
                                            onClick={() => handleButtonClick(wordIndex)}
                                        >
                                            {shuffledWords[wordIndex]}
                                            {firstSelectedIndex === wordIndex && (
                                                <span className="popup">First</span>
                                            )}
                                            {lastSelectedIndex === wordIndex && (
                                                <span className="popup">Last</span>
                                            )}
                                        </button>
                                    )}
                                </div>
                            );
                        })}
                    </div>
                ))}
            </div>
            <button onClick={handleSubmit} className="continue-button">Submit</button>
            {isSuccess === true && <div className="success-message">Success! The words are correct.</div>}
            {isSuccess === false && <div className="error-message">Warning: The words are incorrect.</div>}
        </div>
    );
};

export default SuccessPage;
