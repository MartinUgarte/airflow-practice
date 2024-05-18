# Data Engineer Practicee

You have to gather information about items published in an **ecommerce site**, save it in a database and launch alerts if certain criteria are met. This pipeline should be implemented in **airflow** and run daily.

To do this you will need to **interact with the public API** from the site. Here is some information you will need:

* List of categories for a given site: https://api.mercadolibre.com/sites/MLA/categories
* Specific category information: https://api.mercadolibre.com/categories/MLA1577
* Search category information: https://api.mercadolibre.com/sites/MLA/search?categry=MLA1577#json
* Specific item information: https://api.mercadolibre.com/items/MLA830173972

## Task 1

Create a data pipeline to gather items information and save it in a database.

From MercadoLibre site, get the 50 most relevant published items, for a particular category, "MLA-MICROWAVES" (category id MLA1577). For each item, get the following info:

* id
* site_id
* title
* price
* sold_quantity
* thumbnail

Store all this data with an extra field "created_date" in a database. This simple Data pipeline must be implemented using Airflow Dag.

## Task 2

Send an alert via mail.

In the same DAG developed for the previous task, each time the data gathering task runs, check if any item has earned more than $7.000.000 (price x sold_quantity) and if so send an email with all the gathered data for every item that meets the criteria

This can have any format as long as the info is there. Notes:

* The output format is not specified
* Any libraries or tools needed are also accepted