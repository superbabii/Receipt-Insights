import React, { useState } from 'react';
import SpendingChart from './SpendingChart';
import { uploadReceipt } from '../utils/api';

function Dashboard() {
    const [data, setData] = useState(null);

    const handleFileChange = async (e) => {
        const file = e.target.files[0];
        try {
            const result = await uploadReceipt(file);
            console.log("Upload successful:", result.data);  // Log success response
        } catch (error) {
            console.error("Upload error:", error.response?.data || error.message);  // Log error details
        }
    };

    return (
        <div>
            <input type="file" onChange={handleFileChange} />
            {data && <SpendingChart data={data} />}
        </div>
    );
}

export default Dashboard;
