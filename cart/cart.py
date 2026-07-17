class Cart():
    def __init__(self, request):
        self.session = request.session
        cart = request.session.get('cart')
        if 'cart' not in request.session:
            cart = self.session['cart'] = {}
        self.cart = cart

    def __len__(self):
        return sum (int(item['quantity']) for item in self.cart.values())

    def add_to_cart(self, product, product_quantity):
        product_id = product.id
        if product_id in self.cart:
            self.cart[product_id]['quantity'] += product_quantity
        else:
            self.cart[product_id] = {'price': product.price, 'quantity': product_quantity}
        self.session.modified = True