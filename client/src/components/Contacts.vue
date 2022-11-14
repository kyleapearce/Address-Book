<template>
    <div class="container">
        <!-- TODO: Redesign UI  -->
        <div class="row">
            <div class="col-sm-10">
                <h1>Address Book</h1>
                <hr><br><br>
                <!-- Shows dismissable alert with cooresponding message -->
                <!-- TODO: Alert won't dismiss on timer -->
                <b-alert variant="success" 
                         dismissible
                         fade
                         :show="showDismissibleAlert" 
                         @dismissed="dismissCountdown=0"
                         @dismiss-count-down="countDownChanged">
                         {{ message }}
                </b-alert>
                <!-- Add Contact button connected to contact modal -->
                <!-- TODO: add column for address and city/state -->
                <button type="button" class="btn btn-success btn-sm" v-b-modal.contact-modal>Add Contact</button>
                <br><br>
                <table class="table table-hover" border="2px solid black">
                    <thead>
                        <tr>
                            <th scope="col">First Name</th>
                            <th scope="col">Last Name</th>
                            <th scope="col">Email</th>
                            <th scope="col">Phone Number</th>
                            <th scope="col">Zip Code</th>
                            <th scope="col">City</th>
                            <th scope="col">State</th>
                            <th></th>
                        </tr>
                    </thead>
                    <tbody>
                        <!-- fills table with all contacts and details from backend -->
                        <tr v-for="(contact, index) in contacts" :key="index">
                            <td>{{ contact.firstName }}</td>
                            <td>{{ contact.lastName }}</td>
                            <td>{{ contact.email }}</td>
                            <td>{{ contact.phoneNumber }}</td>
                            <td>{{ contact.zipCode }}</td>
                            <td>{{ contact.city }}</td>
                            <td>{{ contact.state }}</td>
                            <td>
                                <div class="btn-group" role="group">
                                    <!-- edit button that is connected to edit contact modal -->
                                    <button type="button"
                                            class="btn btn-secondary btn-sm"
                                            v-b-modal.contact-update-modal
                                            @click="editContact(contact)">Edit</button>
                                    <!-- delete button that deletes contact and information from table and backend -->
                                    <!-- TODO: Deletion dialog confirmation -->
                                    <button type="button"
                                            class="btn btn-danger btn-sm"
                                            @click="onDeleteContact(contact)">Delete</button>
                                </div>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
        <!-- add contact modal to overlay when button is clicked -->
        <b-modal ref="addContactModal"
                 id="contact-modal"
                 title="Add a new contact"
                 hide-footer>
            <!-- <b-form> used to group contact info -->
            <b-form @submit="onSubmit" @reset="onReset" class="w-100">
                <b-form-group id="form-firstName-group"
                            label="First Name:"
                            label-for="form-firstName-input">
                    <b-form-input id="form-firstName-input"
                                type="text"
                                v-model="addContactForm.firstName"
                                required
                                placeholder="Enter first name">
                    </b-form-input>
                </b-form-group>
                <b-form-group id="form-lastName-group"
                              label="Last Name:"
                              label-for="form-lastName-input">
                    <b-form-input id="form-lastName-input"
                                  type="text"
                                  v-model="addContactForm.lastName"
                                  required
                                  placeholder="Enter last name">
                    </b-form-input>
                </b-form-group>
                <b-form-group id="form-email-group"
                              label="Email address:"
                              label-for="form-email-input">
                    <b-form-input id="form-email-input"
                                  type="email"
                                  v-model="addContactForm.email"
                                  required
                                  placeholder="Enter email">
                    </b-form-input>
                </b-form-group>
                <b-form-group id="form-phoneNumber-group"
                              label="Phone Number:"
                              label-for="form-phoneNumber-input">
                    <!-- v-mask used here for correct phone number format -->
                    <b-form-input id="form-phoneNumber-input"
                                  type="tel"
                                  v-model="addContactForm.phoneNumber"
                                  v-mask="'(###) ###-####'"
                                  required
                                  placeholder="Enter Phone Number">
                    </b-form-input>
                </b-form-group>
                <b-form-group id="form-zipCode-group"
                              label="Zip Code:"
                              label-for="form-zipCode-input">
                    <b-form-input id="form-zipCode-input"
                                  type="number"
                                  v-model="addContactForm.zipCode"
                                  required
                                  placeholder="Enter zip code">
                    </b-form-input>
                </b-form-group>
                <br>
                <!-- submit and reset buttons that are linked to onSubmit and onReset methods -->
                <b-button-group>
                    <b-button type="submit" variant="primary">Submit</b-button>
                    <b-button type="reset" variant="danger">Reset</b-button>
                </b-button-group>
            </b-form>
        </b-modal>
        <!-- edit contact modal to overlay when button is clicked -->
        <b-modal ref="editContactModal"
                 id="contact-update-modal"
                 title="Update"
                 hide-footer>
            <!-- <b-form> used to group contact info -->
            <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
                <b-form-group id="form-firstName-edit-group"
                              label="First Name:"
                              label-for="form-firstName-edit-input">
                    <b-form-input id="form-firstName-edit-input"
                                  type="text"
                                  v-model="editContactForm.firstName"
                                  required
                                  placeholder="Enter First Name">
                    </b-form-input>
                </b-form-group>
                <b-form-group id="form-lastName-edit-group"
                              label="Last Name:"
                              label-for="form-lastName-edit-input">
                    <b-form-input id="form-lastName-edit-input"
                                  type="text"
                                  v-model="editContactForm.lastName"
                                  required
                                  placeholder="Enter last name">
                    </b-form-input>
                </b-form-group>
                <b-form-group id="form-email-edit-group"
                              label="Email address:"
                              label-for="form-email-edit-input">
                    <b-form-input id="form-email-edit-input"
                                  type="email"
                                  v-model="editContactForm.email"
                                  required
                                  placeholder="Enter email">
                    </b-form-input>
                </b-form-group>
                <b-form-group id="form-phoneNumber-edit-group"
                              label="Phone Number:"
                              label-for="form-phoneNumber-edit-input">
                    <!-- v-mask used here for correct phone number format -->
                    <b-form-input id="form-phoneNumber-edit-input"
                                  type="tel"
                                  v-model="editContactForm.phoneNumber"
                                  v-mask="'(###) ###-####'"
                                  required
                                  placeholder="Enter phone number">
                    </b-form-input>
                </b-form-group>
                <b-form-group id="form-zipCode-edit-group"
                              label="Zip Code:"
                              label-for="form-zipCode-edit-input">
                    <b-form-input id="form-zipCode-edit-input"
                                  type="number"
                                  v-model="editContactForm.zipCode"
                                  required
                                  placeholder="Enter zip code">
                    </b-form-input>
                </b-form-group>
                <br>
                <!-- apply and disregard buttons that are linked to onSubmitUpdate and onResetUpdate methods -->
                <b-button-group>
                    <b-button type="submit" variant="primary">Apply Changes</b-button>
                    <b-button type="reset" variant="danger">Disgard Changes</b-button>
                </b-button-group>
            </b-form>
        </b-modal>
    </div>
</template>

<script>
import axios from 'axios'; // used to send AJAX requests and connect client to server
import Alert from './Alert.vue'; // alert component used to get message and display in template

export default {
    data() {
        return {
            contacts: [], // all contact
            addContactForm: { // form data to add contact
                firstName: '',
                lastName: '',
                email: '',
                phoneNumber: '',
                zipCode: '',
            },
            editContactForm: { // form data to edit contact
                firstName: '',
                lastName: '',
                email: '',
                phoneNumber: '',
                zipCode: '',
            },
            message: '', // message to display on alerts
            dismissSecs: 5, // for alert to dismiss in 5 sec
            dismissCountdown: 0,
            showDismissibleAlert: false, // determines when to show message
        };
    },
    components: {
        alert: Alert, // alert component
    },
    methods: {
        // to change alert dismiss countdown to 5 sec
        countDownChanged(dismissCountDown) {
            this.dismissCountDown = dismissCountDown
        },
        // to get all contacts from backend
        getContacts() {
            const path = 'http://localhost:5000/contacts';
            axios.get(path)
                .then((res) => {
                    this.contacts = res.data.contacts;
                })
                .catch((error) => {
                    // eslint-disable-next-line
                    console.error(error);
                });
        },
        // adding contact via 'payload' which contains all data
        addContact(payload) {
            const path = 'http://localhost:5000/contacts';
            axios.post(path, payload) // allows posting to backend
                .then(() => {
                    this.getContacts();
                    this.message = 'Contact Added!';
                    this.showDismissibleAlert = true;
                    this,dismissCountDown = this.dismissSecs
                })
                .catch((error) => {
                    // eslint-disable-next-line
                    console.log(error);
                    this.getContacts();
                });
        },
        // to update values in editContactForm
        editContact(contact) {
            this.editContactForm = contact;
        },
        // initialize and clear both add and edit contact forms
        initForm() {
            this.addContactForm.firstName = '';
            this.addContactForm.lastName = '';
            this.addContactForm.email = '';
            this.addContactForm.phoneNumber = '';
            this.addContactForm.zipCode = '';
            this.editContactForm.id = '',
            this.editContactForm.firstName = '';
            this.editContactForm.lastName = '';
            this.editContactForm.email = '';
            this.editContactForm.phoneNumber = '';
            this.editContactForm.zipCode = '';
        },
        // called when user submits form successfully
        onSubmit(evt) {
            evt.preventDefault(); // prevent normal browser behavior
            this.$refs.addContactModal.hide(); // close modal
            const payload = {
                firstName: this.addContactForm.firstName,
                lastName: this.addContactForm.lastName,
                email: this.addContactForm.email,
                phoneNumber: this.addContactForm.phoneNumber,
                zipCode: this.addContactForm.zipCode,
            };
            this.addContact(payload);
            this.initForm();
        },
        // called when user clicks the reset button
        // hides and resets
        onReset(evt) {
            evt.preventDefault();
            this.$refs.addContactModal.hide();
            this.initForm();
        },
        // same as onSubmit(evt) but using edit contact modal/form instead
        onSubmitUpdate(evt) {
            evt.preventDefault();
            this.$refs.editContactModal.hide();
            const payload = {
                firstName: this.editContactForm.firstName,
                lastName: this.editContactForm.lastName,
                email: this.editContactForm.email,
                phoneNumber: this.editContactForm.phoneNumber,
                zipCode: this.editContactForm.zipCode,
            };
            this.updateContact(payload, this.editContactForm.id);
        },
        // same as onReset(evt) but using edit contact modal/form instead
        onResetUpdate(evt) {
            evt.preventDefault();
            this.$refs.editContactModal.hide();
            this.initForm();
            this.getContacts();
        },
        // same as addContact but uses the contactID to update backend accordingly
        updateContact(payload, contactID) {
            const path = `http://localhost:5000/contacts/${contactID}`;
            axios.put(path, payload)
                .then(() => {
                    this.getContacts();
                    this.message = 'Contact Updated!';
                    this.showDismissibleAlert = true;
                    this,dismissCountDown = this.dismissSecs
                })
                .catch((error) => {
                    // eslint-disable-next-line
                    console.error(error);
                    this.getContacts();
                });
        },
        // similar to addContact and updateContact but simply removes using axios
        removeContact(contactID) {
            const path = `http://localhost:5000/contacts/${contactID}`;
            axios.delete(path)
                .then(() => {
                    this.getContacts();
                    this.message = 'Contact Removed!';
                    this.showDismissibleAlert = true;
                })
                .catch((error) => {
                    // eslint-disable-next-line
                    console.error(error);
                    this.getContacts();
                });
        },
        // called when user clicks the delete button
        // this then calls removeContact()
        onDeleteContact(contact) {
            this.removeContact(contact.id);
        },
    },
    // lifecycle hook that fetches contacts from back-end endpoint
    created() {
        this.getContacts();
    },
};
</script>
