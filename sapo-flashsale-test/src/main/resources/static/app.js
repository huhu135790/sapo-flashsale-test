import React, { useState, useEffect } from 'react';

const FlashSale = () => {
  const [product, setProduct] = useState({ id: 1, name: 'iPhone 15', price: 20000000, salePrice: 10000000, stock: 500 });
  const [message, setMessage] = useState('');

  const handleBuy = async () => {
    try {
      const response = await fetch('/api/flash-sale/order', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ productId: product.id, userId: 'user_123', quantity: 1 })
      });
      const data = await response.text();
      if (response.ok) {
        setMessage("✅ " + data);
        setProduct(prev => ({ ...prev, stock: prev.stock - 1 }));
      } else {
        setMessage("❌ " + data);
      }
    } catch (err) {
      setMessage("❌ Lỗi kết nối server");
    }
  };

  return (
    <div style={{ padding: '20px', border: '1px solid #ccc', borderRadius: '8px', width: '300px' }}>
      <h2>{product.name}</h2>
      <p>Giá gốc: <del>{product.price.toLocaleString()}đ</del></p>
      <p style={{ color: 'red', fontWeight: 'bold' }}>Giá Sale: {product.salePrice.toLocaleString()}đ</p>
      <p>Còn lại: {product.stock}</p>
      <button onClick={handleBuy} disabled={product.stock <= 0}>Mua ngay</button>
      {message && <p>{message}</p>}
    </div>
  );
};

export default FlashSale;