import requests
import datetime
import time
#import sqlalchemy

# Database
#engine = sqlalchemy.create_engine('mysql+pymysql://root:15001500@localhost/shopify')

# API
response = requests.get('https://apps.shopify.com/product-upsell/reviews.json')
data = response.json()

#hora_ini = datetime.datetime.now()



while True:
    # API
    response = requests.get('https://apps.shopify.com/product-upsell/reviews.json')

    data = response.json()

    for i in data["reviews"]:

        # Get values from each row
        v_author = str(i['author'])
        v_body = str(i['body'])
        v_created_at = datetime.datetime.strptime( i['created_at'][0:19], "%Y-%m-%dT%H:%M:%S" )
        v_shop_domain = str(i['shop_domain'])
        v_shop_name = str(i['shop_name'])
        v_star_rating = int(i['star_rating'])

        # Show on screen
        print('### author ###')
        print('')
        print(str(v_author))
        print('')
        print('### body ###')
        print('')
        print(v_body)
        print('')
        print('### created_at ###')
        print('')
        print(v_created_at)
        print('')
        print('### shop_domain ###')
        print('')
        print(v_shop_domain)
        print('')
        print('### shop_name ###')
        print('')
        print(v_shop_name)
        print('')
        print('### star_rating ###')
        print('')
        print(v_star_rating)
        print('')
        print('############################################################')
        print('')

        # Save in Database
        #engine.execute(
        #"""
        #INSERT INTO shopify.shopify_product_upsell (author, body, created_at, shop_domain, shop_name, star_rating)
        #VALUES (%s, %s, %s, %s, %s, %s)
        #""",
        #(v_author, v_body, v_created_at, v_shop_domain, v_shop_name, v_star_rating)
        #)

    print('Waiting 30 seconds to update...')
    print('')

    time.sleep( 30 )
