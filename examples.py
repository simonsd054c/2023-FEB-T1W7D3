# API

# product1 = {
#     "id": 1,
#     "title": "Fjallraven - Foldsack No. 1 Backpack, Fits 15 Laptops",
#     "price": 109.95,
#     "description": "Your perfect pack for everyday use and walks in the forest. Stash your laptop (up to 15 inches) in the padded sleeve, your everyday",
#     "category": "men's clothing",
#     "image": "https://fakestoreapi.com/img/81fPKd-2AYL._AC_SL1500_.jpg",
#     "rating": {
#         "rate": 3.9,
#         "count": 120
#     }
# }

# print(product1["title"])
# print(product1["rating"]["rate"])


# user1 = {
#   "address": {
#     "geolocation": {
#       "lat": "-37.3159",
#       "long": "81.1496"
#     },
#     "city": "kilcoole",
#     "street": "new road",
#     "number": 7682,
#     "zipcode": "12926-3874"
#   },
#   "id": 1,
#   "email": "john@gmail.com",
#   "username": "johnd",
#   "password": "m38rmF$",
#   "name": {
#     "firstname": "john",
#     "lastname": "doe"
#   },
#   "phone": "1-570-236-7033",
#   "__v": 0
# }

# print(user1["address"]["zipcode"])
# print(user1["address"]["geolocation"]["long"])


cart1 = {
  "id": 5,
  "userId": 3,
  "date": "2020-03-01T00:00:00.000Z",
  "products": [
    {
      "productId": 7,
      "quantity": 1
    },
    {
      "productId": 8,
      "quantity": 1
    }
  ],
  "__v": 0
}

print(cart1["products"])

for product in cart1["products"]:
    print(f"ProductId: {product['productId']}")
    print(f"Quantity: {product['quantity']} \n")