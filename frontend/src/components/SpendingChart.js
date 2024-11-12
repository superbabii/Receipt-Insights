import React from 'react';
import { Bar } from 'react-chartjs-2';

function SpendingChart({ data }) {
    const chartData = {
        labels: data.items.map(item => item.name),
        datasets: [
            {
                label: 'Price',
                data: data.items.map(item => item.price)
            }
        ]
    };

    return <Bar data={chartData} />;
}

export default SpendingChart;
