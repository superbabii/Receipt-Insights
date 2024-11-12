import React, { useState } from 'react';
import SpendingChart from './SpendingChart';
import { uploadReceipt } from '../utils/api';

function Dashboard() {
    const [data, setData] = useState(null);

    const handleFileChange = async (e) => {
        const file = e.target.files[0];
        const result = await uploadReceipt(file);
        setData(result);
    };

    return (
        <div>
            <input type="file" onChange={handleFileChange} />
            {data && <SpendingChart data={data} />}
        </div>
    );
}

export default Dashboard;
