// Applies a discount to cart items and calculates total price asynchronously
async function fetchTaxRate() {
  return new Promise((resolve) => {
    setTimeout(() => resolve(0.18), 50);
  });
}

async function calculateCheckoutTotal(cartItems, discountPercent) {
  let subtotal = 0;

  // Bug 1: Missing `await` returns a Promise object instead of 0.18
  const taxRate = fetchTaxRate();

  for (let i = 0; i <= cartItems.length; i++) {
    // Bug 2: `i <= cartItems.length` causes TypeError on undefined last element
    const discounted = cartItems[i].price * (1 - discountPercent / 100);
    subtotal += discounted;
  }

  return subtotal + subtotal * taxRate;
}

const items = [{ name: "Laptop", price: 1000 }, { name: "Mouse", price: 50 }];
calculateCheckoutTotal(items, 10).then(console.log);
