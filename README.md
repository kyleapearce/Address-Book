# Single Page Address Book with Vue.js and Flask

## Description

This project is a single-page address book utilizing Vue.js as frontend framework and Flask to create a REST API as backend framework.
In addition, the project utilizes a webservice integration to USPS for zip code lookup to get city and state.
The Address Book utilizes Docker to start the services using a single command.  
  
**Disclaimer:** *City State Lookup only works using a 5zip Zip Code.*

## Dependencies:
* [Vue](https://vuejs.org/guide/quick-start.html): Version 2.7.14
* [Vue CLI](https://cli.vuejs.org/): Version 5.0.8
* [Node](https://nodejs.org/en/): Version 15.7.0
* [npm](https://docs.npmjs.com/getting-started): Version 7.4.3
* [Flask](https://flask.palletsprojects.com/en/2.2.x/): Version 2.2.2
* [Flask-Cors](https://flask-cors.readthedocs.io/en/latest/): Version 3.0.10
* [Python](https://www.python.org/downloads/): Version 3.9
* [Axios](https://axios-http.com/docs/intro): Version 1.1.3
* [Bootstrap](https://getbootstrap.com/): Version 5.2.2
* [Bootstrap-vue](https://bootstrap-vue.org/docs): Version 2.23.1
* [uuid](https://www.npmjs.com/package/uuid): Version 9.0.0
* [v-mask](https://www.npmjs.com/package/v-mask): Version 2.3.0
* [Docker](https://docs.docker.com/): Version 4.14.0

## Installation

1. Clone

1. Image the server-side folder using Docker:

    ```sh
    > cd [path]/Address-Book/server
    > docker build -f Dockerfile.server -t docker-flask .
    ```

1. Image the client-side folder using Docker:

    ```sh
    > cd [path]/Address-Book/client
    > docker build -f Dockerfile.client -t docker-vuejs .
    ```

1. Build and start the Docker Container:

    ```sh
    > docker-compose up
    ```

    Navigate to [http://localhost:8080](http://localhost:8080) for the Application.  
    Navigate to [http://localhost:5000/contacts](http://localhost:5000/contacts) for the data.

## Resources
* [Creating a Vue App](https://vuejs.org/guide/essentials/application.html)
* [Flask Documentation](https://flask.palletsprojects.com/en/2.2.x/quickstart/)
* [USPS Web Tools API Documentation](https://www.usps.com/business/web-tools-apis/address-information-api.pdf)
* [Developing Single-Page App with Flask and Vue.js](https://testdriven.io/blog/developing-a-single-page-app-with-flask-and-vuejs/)
* [USPS Web Tools API in Python](https://www.youtube.com/watch?v=QYhQcsrOFXY)
* [Docker Documentation](https://docs.docker.com/get-started/)
* [Using Docker with Vue.js](https://www.middlewareinventory.com/blog/docker-vuejs/)
* [Using Docker with Flask](https://www.freecodecamp.org/news/how-to-dockerize-a-flask-app/)
* [Using Docker Compose](https://docs.docker.com/get-started/08_using_compose/)
* [Building Vue App with Flask using Docker](https://www.section.io/engineering-education/how-to-build-a-vue-app-with-flask-sqlite-backend-using-docker/#dockerizing-the-application)

## 📫 Contact
Cell: (847) 363-3373  
[Email (kylepearce56@gmail.com)](mailto:kylepearce56@gmail.com)  
[LinkedIn](https://www.linkedin.com/in/kyle-a-pearce/)  
[Github](https://github.com/kyleapearce/Portfolio)  