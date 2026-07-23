from myapp.models import Product
from decimal import Decimal

class Cart():
    def __init__(self, request):
        self.session = request.session
        cart = request.session.get('cart')
        if 'cart' not in request.session:
            cart = self.session['cart'] = {}
        self.cart = cart

    def __len__(self):
        return sum (int(item['quantity']) for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * Decimal(item['quantity']) for item in self.cart.values())


    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(pk__in=product_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['quantity'] = Decimal(item['quantity'])
            item['total'] = item['price']*item['quantity']
            yield item


    def add(self, product, product_quantity):
        product_id = product.id
        if product_id in self.cart:
            self.cart[product_id]['quantity'] += product_quantity
        else:
            self.cart[product_id] = {'price': str(product.price), 'quantity': product_quantity}
        self.session.modified = True

    def delete(self,product_id):
        product_id = str(product_id)
        if product_id in self.cart:
            del self.cart[product_id]
        self.session.modified = True

    def update(self, product_id, product_quantity):
        product_id = str(product_id)
        product_quantity = str(product_quantity)
        if product_id in self.cart:
            self.cart[product_id]['quantity'] = product_quantity
        self.session.modified = True