import React, { useState } from 'react';
import ReceiptForm from './ReceiptForm'; // Import the new form component
import { uploadReceipt } from '../utils/api';
import './Dashboard.css';

function Dashboard() {
    const [data, setData] = useState(null);

    const handleFileChange = async (e) => {
        const file = e.target.files[0];
        try {
            const result = await uploadReceipt(file);
            setData(result);
            console.log("Upload successful:", result);
        } catch (error) {
            console.error("Upload error:", error.response?.data || error.message);
        }
    };

    return (
        <div className="Dashboard">
            <span>Choose only HEIC file</span>
            <label htmlFor="fileInput">Upload Receipt</label>
            <input
                id="fileInput"
                type="file"
                accept=".heic" // Accept only HEIC files
                onChange={handleFileChange}
            />
            {data && <ReceiptForm data={data} />}
        </div>
    );
}

export default Dashboard;
