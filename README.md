# SToreManager-APIs
[![Build Status](https://travis-ci.org/MusyokiBryan/SToreManager-APIs.svg?branch=fixes-for-badges-161452294)](https://travis-ci.org/MusyokiBryan/SToreManager-APIs) [![Coverage Status](https://coveralls.io/repos/github/MusyokiBryan/StoreManager-APIv1/badge.svg?branch=tavis-config)](https://coveralls.io/github/MusyokiBryan/StoreManager-APIv1?branch=tavis-config)  [![Maintainability](https://api.codeclimate.com/v1/badges/c63a623d87c2cbf91ddb/maintainability)](https://codeclimate.com/github/MusyokiBryan/SToreManager-APIs/maintainability) 

# STORE-MANAGER-APIs
- Admin can add a product
- Admin/store attendant can get all products
- Admin/store attendant can get a specific product
- Store attendant can add a sale order
- Admin can get all sale order records

## Endpoints

| HTTP Method   |     Endpoint                |     Function            |
| ------------- |:--------------------------: | -----------------------:|
| GET           | /api/v1/products            |   Get all products      |
| GET           | /api/v1/products/product_id |   Get one product       |
| POST          | /api/v1/products            |   Create a new product  |
| PUT           | /api/v1/product/product_id  |   Edit a  product       |
| DELETE        | /api/v1/product/product_id  |   Delete a product      |
| GET           | /api/v1/sales               |   Get all sales         |
| GET           | /api/v1/products/product_id |   Get one sale record   |
| POST          | /api/v1/sales               |   Create a new product  |
| PUT           | /api/v1/sale/product_id     |   Edit a  sale          |
| DELETE        | /api/v1/sale/product_id     |   Delete a sale         |



## Pivotal Tracker Board
https://www.pivotaltracker.com/n/projects/2204291

## Heroku Link
https://storemanager-apis.herokuapp.com/api/v1/documentation

## Prerequisites
- pip
- virtualenv
- python 3 or python 2.7

## Setting Up Locally
- Clone the repo
- git clone https://github.com/MusyokiBryan/SToreManager-APIs
- create a virtual environment and activate it
- virtualenv venv
- install dependencies
- pip install -r requirements.txt
- on terminal execute run.py
- on a browser or postman enter 27.0.0.1:5000/api/v1/documentation
- test endpoints

## Author
### MUSYOKI BRIAN