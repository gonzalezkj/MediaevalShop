class Carro:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carro = self.session.get("carro")
        if not carro:
            carro = self.session["carro"] = {}
        self.carro = carro

    def add(self, product):
        if (str(product.id) not in self.carro.keys()):
            self.carro[product.id] = {
                "product_id": product.id,
                "name": product.name,
                "quantity": 1,
                "price": str(product.price),
                "image": product.image.url,
            }
        else:
            for key, value in self.carro.items():
                if key == str(product.id):
                    value["quantity"] = value["quantity"] + 1
                    value["price"]=float(value["price"])+product.price
                    break 
        self.save()

    def save(self):
        self.session["carro"] = self.carro
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.carro:
            del self.carro[product_id]
            self.save()
        
    def decrement(self, product):
        for key, value in self.carro.items():
            if key == str(product.id):
                value["quantity"] = value["quantity"] - 1
                value["price"]=float(value["price"])-product.price
                if value["quantity"] < 1:
                    self.remove(product)
                else:
                    self.save()
                break
            else:
                print("The product doesn't exist in the car")

    def clear(self):
        self.session["carro"] = {}
        self.session.modified = True
            
