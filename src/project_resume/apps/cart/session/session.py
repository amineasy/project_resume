from project_resume.apps.menu.models import Dish

CART_SESSION_ID = 'cart'


class Cart:
    def __init__(self,request):
        self.session = request.session
        cart =self.session.get(CART_SESSION_ID)
        if not cart:
            cart = self.session[CART_SESSION_ID] = {}
        self.cart = cart


    def add_cart(self,dish,quantity=1):
        dish_id = str(dish.id)
        if dish_id not in self.cart:
            self.cart[dish_id] = {'quantity':quantity,'price':dish.get_total_price()}
        else:
            self.cart[dish_id]['quantity'] += quantity

        self.save_cart()




    def remove_all(self,dish):
        dish_id = str(dish.id)
        if dish_id in self.cart:
            del self.cart[dish_id]
            self.save_cart()









    def remove_single(self,dish):
        dish_id = str(dish.id)
        if dish_id in self.cart:
            if self.cart[dish_id]['quantity'] > 1:
                self.cart[dish_id]['quantity'] -= 1
            else:
                del self.cart[dish_id]
            self.save_cart()







    def __iter__(self):
        dish_ids = self.cart.keys()
        dishes = Dish.objects.filter(id__in=dish_ids)


        cart = self.cart.copy()
        for dish in dishes:
            cart[str(dish.id)]['dish'] = dish


        for item in cart.values():
            item['price'] = int(item['price'])
            item['total_price'] = int(item['price']) * item['quantity']
            yield item





    def get_total_price(self):
        return sum(
            int(item['price']) * int(item['quantity'])
            for item in self.cart.values()
        )














    def save_cart(self):
        self.session.modified = True
