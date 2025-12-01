def funnel_conversion(df):
    users_view = set(df[df.event_type == "view"]['user_id'].unique())
    users_cart = set(df[df.event_type == "cart"]['user_id'].unique())
    users_remove_from_cart = set(df[df.event_type == "remove_from_cart"]['user_id'].unique())
    users_purchase = set(df[df.event_type == "purchase"]['user_id'].unique())

    return {
        "view": len(users_view),
        "cart": len(users_cart),
        "remove_from_cart": len(users_remove_from_cart),
        "purchase": len(users_purchase),
        "view_to_cart": len(users_cart.intersection(users_view)) if users_view else 0,
        "cart_to_remove_from_cart": len(users_remove_from_cart.intersection(users_cart)) if users_cart else 0,
        "cart_to_purchase": len(users_cart.intersection(users_purchase)) if users_cart else 0,
        "view_to_purchase": len(users_purchase.intersection(users_view)) if users_view else 0,
        "remove_from_cart_to_purchase": len(users_purchase.intersection(users_remove_from_cart)) if users_remove_from_cart else 0
    }