// Applies a discount to cart items and calculates total price asynchronously
async function fetchTaxRate() {
  return new Promise((resolve) => {
    setTimeout(() => resolve(0.18), 50);
  });
}

async function calculateCheckoutTotal(cartItems, discountPercent) {
  let subtotal = 0;

  // Fixed: Added `await` to resolve the tax rate Promise
  const taxRate = await fetchTaxRate();

  // Fixed: Used strict `<` instead of `<=` to prevent out-of-bounds access
  for (let i = 0; i < cartItems.length; i++) {
    const discounted = cartItems[i].price * (1 - discountPercent / 100);
    subtotal += discounted;
  }

  return Number((subtotal + subtotal * taxRate).toFixed(2));
}

(async () => {
  const items = [
    { name: "Laptop", price: 1000 },
    { name: "Mouse", price: 50 },
  ];
  const total = await calculateCheckoutTotal(items, 10);
  console.assert(total === 1115.1, `Expected 1115.1, got ${total}`);

  const emptyTotal = await calculateCheckoutTotal([], 10);
  console.assert(emptyTotal === 0, `Expected 0, got ${emptyTotal}`);
  console.log("All bug2_fixed.js test cases passed!");
})();
