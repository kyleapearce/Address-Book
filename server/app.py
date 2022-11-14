
import uuid
from flask import Flask, jsonify, request
from flask_cors import CORS # to make cross-origin requests

# list of contacts
CONTACTS = [
    {
        'id': uuid.uuid4().hex,
        'firstName': 'Kyle',
        'lastName': 'Pearce',
        'email': 'kylepearce56@gmail.com',
        'phoneNumber': '(847) 363-3373',
        'zipCode': '80302'
    },
    {
        'id': uuid.uuid4().hex,
        'firstName': 'Sedona',
        'lastName': 'Decint',
        'email': 'sfd.2018@gmail.com',
        'phoneNumber': '(571) 236-8817',
        'zipCode': '22003'
    },
    {
        'id': uuid.uuid4().hex,
        'firstName': 'Kristine',
        'lastName': 'Pearce',
        'email': 'krispearce@icloud.com',
        'phoneNumber': '(847) 772-5473',
        'zipCode': '60060'
    }
]

# config
DEBUG = True

# instantiate app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

def remove_contact(contact_id):
    for contact in CONTACTS:
        if contact['id'] == contact_id:
            CONTACTS.remove(contact)
            return True
    return False

# route handler for contacts
@app.route('/contacts', methods=['GET', 'POST'])
def all_contacts():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        CONTACTS.append({
            'id': uuid.uuid4().hex,
            'firstName': post_data.get('firstName'),
            'lastName': post_data.get('lastName'),
            'email': post_data.get('email'),
            'phoneNumber': post_data.get('phoneNumber'),
            'zipCode': post_data.get('zipCode')
        })
        response_object['message'] = 'Contact Added!'
    else:
        response_object['contacts'] = CONTACTS
    return jsonify(response_object)

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
            'zipCode': post_data.get('zipCode')
        })
        response_object['message'] = 'Contact updated!'
    if request.method == 'DELETE':
        remove_contact(contact_id)
        response_object['message'] = 'Contact Removed!'
    return jsonify(response_object)


if __name__ == '__main__':
    app.run()
