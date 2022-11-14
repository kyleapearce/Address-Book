import uuid # used for a unique identifier
from flask import Flask, jsonify, request
from flask_cors import CORS # to make cross-origin requests

# next two imports are used for USPS API
import urllib.request
import xml.etree.ElementTree as ET

# list of contacts
CONTACTS = [
    {
        'id': uuid.uuid4().hex,
        'firstName': 'Kyle',
        'lastName': 'Pearce',
        'email': 'kylepearce56@gmail.com',
        'phoneNumber': '(847) 363-3373',
        'zipCode': '80302',
        'city': 'BOULDER',
        'state': 'CO'
    },
    {
        'id': uuid.uuid4().hex,
        'firstName': 'Sedona',
        'lastName': 'Decint',
        'email': 'sfd.2018@gmail.com',
        'phoneNumber': '(571) 236-8817',
        'zipCode': '22003',
        'city': 'ANNANDALE',
        'state': 'VA'
    },
    {
        'id': uuid.uuid4().hex,
        'firstName': 'Kristine',
        'lastName': 'Pearce',
        'email': 'krispearce@icloud.com',
        'phoneNumber': '(847) 772-5473',
        'zipCode': '60060',
        'city': 'MUNDELEIN',
        'state': 'IL'
    }
]

# config
DEBUG = True

# instantiate app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# getCity helper using zip code lookup API
def getCity(z):
    requestXML = """
    <?xml version="1.0"?>
    <CityStateLookupRequest USERID="092NA0002149">
        <ZipCode ID="0">
            <Zip5>{0}</Zip5>
        </ZipCode>
    </CityStateLookupRequest>
    """
    # prepare xml string doc for query string
    docString = requestXML.format(z)
    docString = docString.replace('\n', '').replace('\t', '')
    docString = urllib.parse.quote_plus(docString)
    # url with XML for City State Lookup Request
    url = "https://secure.shippingapis.com/ShippingAPI.dll?API=CityStateLookup&XML=" + docString
    #print(url +"\n\n")
    # make API call and check for errors
    response = urllib.request.urlopen(url)
    if response.getcode() != 200:
        print("Error making HTTP call:")
        print(response.info())
        exit()
    # get content of response
    resContents = response.read()
    #print(contents)
    # parse XML result
    APIroot = ET.fromstring(resContents)
    for zipcode in APIroot.findall('ZipCode'):
        #print("City: " + zipcode.find("City").text)
        return zipcode.find("City").text

# getState helper using zip code lookup API
def getState(z):
    requestXML = """
    <?xml version="1.0"?>
    <CityStateLookupRequest USERID="092NA0002149">
        <ZipCode ID="0">
            <Zip5>{0}</Zip5>
        </ZipCode>
    </CityStateLookupRequest>
    """
    # prepare xml string doc for query string
    docString = requestXML.format(z)
    docString = docString.replace('\n', '').replace('\t', '')
    docString = urllib.parse.quote_plus(docString)
    # url with XML for City State Lookup Request
    url = "https://secure.shippingapis.com/ShippingAPI.dll?API=CityStateLookup&XML=" + docString
    #print(url +"\n\n")
    # make API call and check for errors
    response = urllib.request.urlopen(url)
    if response.getcode() != 200:
        print("Error making HTTP call:")
        print(response.info())
        exit()
    # get content of response
    resContents = response.read()
    #print(contents)
    # parse XML result
    APIroot = ET.fromstring(resContents)
    for zipcode in APIroot.findall('ZipCode'):
        #print("State: " + zipcode.find("State").text)
        return zipcode.find("State").text


# check route to ensure method works
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

def remove_contact(contact_id):
    for contact in CONTACTS:
        if contact['id'] == contact_id:
            CONTACTS.remove(contact)
            return True
    return False

# route handlers for contacts
# GET grabs data from backend
# POST adds a new dataset from form
@app.route('/contacts', methods=['GET', 'POST'])
def all_contacts():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()

        # API Zip Code lookup

        CONTACTS.append({
            'id': uuid.uuid4().hex,
            'firstName': post_data.get('firstName'),
            'lastName': post_data.get('lastName'),
            'email': post_data.get('email'),
            'phoneNumber': post_data.get('phoneNumber'),
            'zipCode': post_data.get('zipCode'),
            'city': getCity(post_data.get('zipCode')),
            'state': getState(post_data.get('zipCode'))
        })
        response_object['message'] = 'Contact Added!'
    else:
        response_object['contacts'] = CONTACTS
    return jsonify(response_object)

# different route handler for PUT and DELETE as they need a specific contact id
# PUT edits and updates already existing data
# DELETE (self explanatory but deletes contact and data from backend)
@app.route('/contacts/<contact_id>', methods=['PUT', 'DELETE'])
def single_contact(contact_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        remove_contact(contact_id)
        CONTACTS.append({
            'id': uuid.uuid4().hex,
            'firstName': post_data.get('firstName'),
            'lastName': post_data.get('lastName'),
            'email': post_data.get('email'),
            'phoneNumber': post_data.get('phoneNumber'),
            'zipCode': post_data.get('zipCode'),
            'city': getCity(post_data.get('zipCode')),
            'state': getState(post_data.get('zipCode'))
        })
        response_object['message'] = 'Contact Updated!'
    if request.method == 'DELETE':
        remove_contact(contact_id)
        response_object['message'] = 'Contact Removed!'
    return jsonify(response_object)

# calls app to run
if __name__ == '__main__':
    app.run()
