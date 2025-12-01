Funnel analysis is marketing technique used to track and analyze the user journey as they move through a series of steps towards a specific goal, like purchase. It visually maps out the customer path, often in a narrowing "funnel" shape, to identify where users drop off so businesses can optimize the experience, improve conversion rates, and fix points of friction. 

In this repo, we explore eCommerce purchase history from kaggle with following goals:
- Check journey of user from view to purchase.
- Create streamlit dashboard with plots explaining funnel analysis, retention rate etc.

Data:

Downloaded eCommerce purchase history in cosmetic shop (`https://www.kaggle.com/datasets/mkechinov/ecommerce-events-history-in-cosmetics-shop`).  

Each row in the file represents an event. All events are related to products and users. There are different types of events.

The file contains following columns:
event_time: when event was happened
event_type: one of view, cart, remove_from_cart, purchase
product_id: Product ID
category_id: Product category ID
category_code: Category meaningful name
brand: Brand
price: Product price
user_id: permanent user ID
user_session: User session ID

Requirements:

Requirements are managed in poetry `pyproject.toml`. To create a virtual environment with dependencies installed, run:
`poetry install; source .venv/bin/activate`

Download kaggle data from `https://www.kaggle.com/datasets/mkechinov/ecommerce-events-history-in-cosmetics-shop` and save it as `data/archive.zip`

Dashboard:

Run `streamlit run ./app/streamlit_app.py`. Load the data from `./data/archive.zip`


