from flask import *
import cgi
from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
from xml.dom import minidom

zipcode = ''
# radius  = 40000

app = Flask(__name__)


def hello():
    print ("hellfsjdla;fal;slkldsfkdsafklfdaskl;fdskl;fkl;asdfkdsa;o")

@app.route("/conferences.html")
def getrecs():
    auth = Oauth1Authenticator(
        consumer_key = "4mKzLgbw5zlE-O7Jle9kJg",
        consumer_secret = "xQVDkzJQmbr26heYvjmRT6vCyuY",
        token = "jStDNSrNExPPOYbafiRrnL01AphMONJH",
        token_secret = "EH3SLPVzI4qKGxPOtlYRyPgcpkI"
    )


    client = Client(auth)
    client2 = Client(auth)
    client3 = Client(auth)
    client4 = Client(auth)
    
    params = {
        'term': 'breakfast',
        'lang': 'en',
        'radius_filter': 40000
    }

    response = client.search(zipcode, **params)

    rate1 = str(response.businesses[0].rating)
    address1 = response.businesses[0].location.display_address[0] + " " + response.businesses[0].location.display_address[1]

    data = {"restaurants": [
       {"name": response.businesses[0].name, "rating": rate1, "image_url": response.businesses[0].image_url, "address": address1}]}

    params2 = {
        'term': 'park',
        'lang': 'en',
        'radius_filter': 40000
    }

    response2 = client2.search(zipcode, **params2)

    rate2 = str(response2.businesses[0].rating)
    address2 = response2.businesses[0].location.display_address[0] + " " + response2.businesses[0].location.display_address[1]

    data2 = {"restaurants": [
       {"name": response2.businesses[0].name, "rating": rate2, "image_url": response2.businesses[0].image_url, "address": address2}]}


    params3 = {
        'term': 'lunch',
        'lang': 'en',
        'radius_filter': 40000
    }

    response3 = client3.search(zipcode, **params3)

    rate3 = str(response3.businesses[0].rating)
    address3 = response3.businesses[0].location.display_address[0] + " " + response3.businesses[0].location.display_address[1]

    data3 = {"restaurants": [
       {"name": response3.businesses[0].name, "rating": rate3, "image_url": response3.businesses[0].image_url, "address": address3}]}

    params4 = {
        'term': 'beach',
        'lang': 'en',
        'radius_filter': 40000
    }

    response4 = client4.search(zipcode, **params4)

    rate4 = str(response4.businesses[0].rating)
    address4 = response4.businesses[0].location.display_address[0] + " " + response4.businesses[0].location.display_address[1]

    data4 = {"restaurants": [
       {"name": response4.businesses[0].name, "rating": rate4, "image_url": response4.businesses[0].image_url, "address": address4}]}


    return render_template('conferences.html', name1 = data, name2= data2, name3 = data3, name4 = data4)




    # print (response.businesses[0].name)
    # print (response.businesses[1].name)
    # print (response.businesses[2].name)

@app.route('/', methods=['GET', 'POST'])
def signup():

    if request.method == 'POST':

        # print request.form['zipcode']
        global zipcode
        zipcode = request.form['zipcode']

        # global radius
        # radius = (request.form['distance'] + 0.0) * 40000.0/25.0
        # print radius

        # return render_template('conferences.html')

        return getrecs();

    else:
        return render_template('signup.html')

# @app.route("/JSON")
# def test(zipcode = 95129):
#     return getrecs(zipcode)

if __name__ == "__main__":
    app.run()

print (zipcode)






# getrecs('94089')
