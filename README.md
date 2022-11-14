# Single Page Address Book with Vue.js and Flask

## To use project

1. Clone

1. Run the server-side Flask app using one terminal window:

    ```sh
    > cd path/server
    > py -3 -m venv venv
    > venv/Scripts/activate
    (env)$ pip install -r req.txt
    (env)$ python app.py
    ```

    Navigate to [http://localhost:5000](http://localhost:5000)

1. Run the client-side Vue app in a different terminal window:

    ```sh
    > cd path/client
    > npm install
    > npm run serve
    ```

    Navigate to [http://localhost:8080](http://localhost:8080)