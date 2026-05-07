// cartModule.js - 模块化导出
export const cart = [];

export function addToCart(item) {
    cart.push(item);
    console.log(`添加了商品: ${item.name}`);
}

export function getCartTotal() {
    return cart.reduce((total, item) => total + item.price, 0);
}

export default function checkout() {
    const total = getCartTotal();
    console.log(`去结算，总价为: ${total}元`);
    return total;
}