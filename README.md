# Stock Viewer

A web app to check out the latest updates in stock market. Check it out here:

**https://stock-viewer-murex.vercel.app/**

*(NOTE: It will show Table not found because backend has not been configured as explained in demo)*

**Demo Video Link** : ***https://drive.google.com/file/d/1ZbvG-i-Univ4W42PctKvMtw1URsvasTR/view?usp=sharing***

### Idea behind storing data

There are a few ways to approach this:

1. In one way, we can use 2 sorts of data structures : A Hashed set for storing the dictionary (row) as value and Stock Name as key. And we use another data structure, a Sorted Set to store the key (Stock Names) along with the values as same constant. This way, when called with the range, it returns keys in lexographical manner, which results in faster response of values.
    - **Advantage** : Faster retrieval of sorted Stock Names and their corresponding rows.
    - **Disadvantages** : Since Redis works in-memory, it consumes memory for 2 data structures, which can be expensive if low on resource.

2. Another way was to use Hashed set to store all the keys daily, and match the input pattern using SCAN and get the data in a Python list, sort it server-side by Stock Name as key, and send this array as response.
    - **Advantages** : Less memory consumption since only 1 data structure is being used.
    - **Disadvantages** : Increase retrieval time, compared to above as first it matches the pattern with keys and then sorts the data.

**_Because of low resource, and less amount of data to be stored, I went for the second approach as this sorting does not cost much overhead for less number of objects, but it could be easily done in other way too._**

## Frontend

* Frontend is built using Vue.js, with Buefy for UI components, and some personal specifications.
* For pagination, to reduce the load on client, I have implemented **backend pagination**. This way, it only loads data for the current page.
* Number of rows to be displayed per page can be changed by choice, the table is responsive.
* I have given 2 type of search fields:
    - *Search by Prefix* : It matches and displays the Stocks whose names begin with the search query.
    - *Seach in Text*: This search field matches all the stocks which contain the search query as substring in their names.
* An `Export CSV` has been provided to download all the data which matches your search criteria in the form of a CSV file.

## Backend

* Backend has been built using Django and its components.
* `APScheduler` library is used to schedule the CRON job of updating Redis database daily at 6 PM IST. It clears the previous data and updates database with new data.
* For fetching the latest Stocks ZIP data, following issues and their resolutions were encountered:
    - The ZIP file URL does have a fixed URL format, where only the date changes.
    - But, making a fixed rule to name it could result in error if Stock Markets were closed at any particular day due to any reason.
    - Hence a better way, which I used is to use a small crawler to get the fixed XPath of element which contains the file URL, and fetch that file.
* The ZIP file is not downloaded as file, but directly read into memory, parsed and its contents stored to Redis database, using a Hashed Set with Stock Name as Key and the Stock object as Value. This ensures better clean-up.
* Four APIs have been constructed to fetch data:
    - API to fetch all the data
    - API to fetch data by search query as prefix
    - API to fetch data by search query to be searched in full text
    - API to Download CSV file

## Production

* Dockerized the full stack application
* This way, the docker images can directly be deployed to any VPS without thinking of any configurations
* If you want to check the front end application, its deployed to Vercel [here](https://stock-viewer-murex.vercel.app/).

## For checking it out yourself :

*(Note: You need to have Docker installed in your system for this)*

1. Either clone the repo

```
git clone https://github.com/Pranjalya/stock-viewer
cd stock-viewer
```

OR

Simply download the [ `.env` file](https://raw.githubusercontent.com/Pranjalya/stock-viewer/main/.env)  and [ `docker-compose.yml` file](https://raw.githubusercontent.com/Pranjalya/stock-viewer/main/docker-compose.yml) from this repository in a folder, since the docker images have already been pushed to [Docker Hub](https://hub.docker.com/u/pranjalya).

The files have also been hosted in [Google Drive](https://drive.google.com/drive/folders/1GpP_cTdVL67limkpu1wgrp3js9KbqSA8?usp=sharing).

2. Run the docker-compose

```
docker-compose up -d
```

3. Open `0.0.0.0` in your browser

4. Close the running containers

```
docker-compose down
```

## Screenshots

- __Landing Page__

![Landing Page](https://raw.githubusercontent.com/Pranjalya/stock-viewer/main/assets/Screenshot%20from%202021-02-02%2013-46-05.png)

- __Stock Table__

![Stock Table](https://raw.githubusercontent.com/Pranjalya/stock-viewer/main/assets/Screenshot%20from%202021-02-02%2013-46-51.png)