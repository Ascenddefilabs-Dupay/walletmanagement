'use client';

import React, { useEffect, useState } from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faArrowLeft } from '@fortawesome/free-solid-svg-icons';
import './style.css';

const SuccessPage: React.FC = () => {
    const [recoveryWords, setRecoveryWords] = useState<string[]>([]);
    const [selectedIndexes, setSelectedIndexes] = useState<number[]>([]);
    const [firstSelectedIndex, setFirstSelectedIndex] = useState<number | null>(null);
    const [lastSelectedIndex, setLastSelectedIndex] = useState<number | null>(null);
    const [isSuccess, setIsSuccess] = useState<boolean | null>(null); // State to track success

    useEffect(() => {
        const words = localStorage.getItem('recoveryWords');
        if (words) {
            const wordArray = words.split(' ');
            setRecoveryWords(wordArray);
        }
    }, []);

    const handleBackClick = () => {
        window.history.back();
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

    const handleSubmit = () => {
        if (firstSelectedIndex !== null && lastSelectedIndex !== null) {
            const firstWord = recoveryWords[firstSelectedIndex];
            const lastWord = recoveryWords[lastSelectedIndex];

            const expectedFirstWord = recoveryWords[0]; // Assuming the first word in the list is expected first
            const expectedLastWord = recoveryWords[recoveryWords.length - 1]; // Assuming the last word in the list is expected last

            console.log('Full recovery words:', recoveryWords);
            console.log('Selected First Word:', firstWord);
            console.log('Selected Last Word:', lastWord);
            console.log('Expected First Word:', expectedFirstWord);
            console.log('Expected Last Word:', expectedLastWord);

            const isCorrect = 
                firstWord.toLowerCase() === expectedFirstWord.toLowerCase() &&
                lastWord.toLowerCase() === expectedLastWord.toLowerCase();

            if (isCorrect) {
                setIsSuccess(true);
            } else {
                setIsSuccess(false);
            }
        }
    };

    return (
        <div className="success-wrapper">
            <span className="success-back-arrow" onClick={handleBackClick}>
                <FontAwesomeIcon icon={faArrowLeft} />
            </span>
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
                                    {shouldRenderButton && wordIndex < recoveryWords.length && (
                                        <button
                                            className={`word-button ${selectedIndexes.includes(wordIndex) ? 'selected' : ''}`}
                                            onClick={() => handleButtonClick(wordIndex)}
                                        >
                                            {recoveryWords[wordIndex]}
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
