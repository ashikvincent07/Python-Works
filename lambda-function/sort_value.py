cart = {
    "bluetooth speaker": 2500,
    "headphone": 2000,
    "mouse": 1000,
    "laptop": 55000,
    "keyboard": 1500
}

sorted_cart = sorted(cart, key = lambda k: cart.get(k))

print(sorted_cart)