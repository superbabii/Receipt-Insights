import React from 'react';

function ReceiptForm({ data }) {
    return (
        <div>
            <h2>Store Information</h2>
            <p><strong>Store Name:</strong> {data.storeName}</p>
            <p><strong>Address:</strong> {data.address}</p>

            <h2>Transaction Details</h2>
            <p><strong>Transaction Date:</strong> {data.transactionDate}</p>
            <p><strong>Transaction Time:</strong> {data.transactionTime}</p>
            <p><strong>CHK Number:</strong> {data.chkNumber}</p>
            <p><strong>Cashier ID:</strong> {data.cashierID}</p>

            <h2>Items Purchased</h2>
            {data.items.map((item, index) => (
                <p key={index}>{item.name} - {item.price}</p>
            ))}

            <h2>Payment Details</h2>
            <p><strong>Subtotal:</strong> {data.paymentDetails.subtotal}</p>
            <p><strong>VAT:</strong> {data.paymentDetails.vat}</p>
            <p><strong>Total Amount:</strong> {data.paymentDetails.totalAmount}</p>
            <p><strong>Payment Method:</strong> {data.paymentDetails.paymentMethod}</p>
            <p><strong>Amount Paid:</strong> {data.paymentDetails.amountPaid}</p>
            <p><strong>Change Due:</strong> {data.paymentDetails.changeDue}</p>

            <h2>Additional Information</h2>
            <p><strong>Receipt Closed Time:</strong> {data.additionalInfo.receiptClosedTime}</p>
            <p><strong>Feedback Link:</strong> {data.additionalInfo.feedbackLink}</p>
            <p><strong>VAT No.:</strong> {data.additionalInfo.vatNumber}</p>
        </div>
    );
}

export default ReceiptForm;
