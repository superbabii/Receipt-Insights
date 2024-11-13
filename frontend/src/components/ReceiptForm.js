import React from 'react';
import './ReceiptForm.css';

function ReceiptForm({ data }) {
    return (
        <div className="ReceiptForm">
            <h2>Store Information</h2>
            <p><strong>Store Name:</strong> <span>{data.storeName}</span></p>
            <p><strong>Address:</strong> <span>{data.address}</span></p>

            <h2>Transaction Details</h2>
            <p><strong>Transaction Date:</strong> <span>{data.transactionDate}</span></p>
            <p><strong>Transaction Time:</strong> <span>{data.transactionTime}</span></p>
            <p><strong>CHK Number:</strong> <span>{data.chkNumber}</span></p>
            <p><strong>Cashier ID:</strong> <span>{data.cashierID}</span></p>

            <h2>Items Purchased</h2>
            <div className="items">
                {data.items.map((item, index) => (
                    <p key={index}><strong>{item.name}</strong> - <span>{item.price}</span></p>
                ))}
            </div>

            <h2>Payment Details</h2>
            <p><strong>Subtotal:</strong> <span>{data.paymentDetails.subtotal}</span></p>
            <p><strong>VAT:</strong> <span>{data.paymentDetails.vat}</span></p>
            <p><strong>Total Amount:</strong> <span>{data.paymentDetails.totalAmount}</span></p>
            <p><strong>Payment Method:</strong> <span>{data.paymentDetails.paymentMethod}</span></p>
            <p><strong>Amount Paid:</strong> <span>{data.paymentDetails.amountPaid}</span></p>
            <p><strong>Change Due:</strong> <span>{data.paymentDetails.changeDue}</span></p>

            <h2>Additional Information</h2>
            <p><strong>Receipt Closed Time:</strong> <span>{data.additionalInfo.receiptClosedTime}</span></p>
            <p><strong>Feedback Link:</strong> <a href={`https://${data.additionalInfo.feedbackLink}`} target="_blank" rel="noopener noreferrer">{data.additionalInfo.feedbackLink}</a></p>
            <p><strong>VAT No.:</strong> <span>{data.additionalInfo.vatNumber}</span></p>
        </div>
    );
}

export default ReceiptForm;
