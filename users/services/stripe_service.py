import stripe
stripe.api_key = "STRIPE_SECRET_KEY"

def create_product(name):
    return stripe.Product.create(name=name)

def create_price(product_id, amount):
    return stripe.Price.create(
        product=product_id,
        currency="rub",
        unit_amount=amount * 100,
    )

def create_checkout_session(price_id, success_url, cancel_url):
    return stripe.checkout.Session.create(
        payment_method_types=["card"],
        mode="payment",
        line_items=[{
            "price": price_id,
            "quantity": 1,
        }],
        success_url=success_url,
        cancel_url=cancel_url,
    )

def retrieve_session(session_id):
    return stripe.checkout.Session.retrieve(session_id)
