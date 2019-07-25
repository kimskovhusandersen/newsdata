# Project: Log Analysis
The Log Analysis project is the first project in Udacity's full stack web development nanodegree program. The task was to build an internal reporting tool answering the following three questions:

- What are the most popular three articles of all time?
- Who are the most popular article authors of all time?
- On which days did more than 1% of requests lead to errors?

## The webapp makes use of

- We are using a tools called Vagrant and VirtualBox to manage our VM.
- a [newsdata.sql](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) file provided by Udacity
- [Flask](https://palletsprojects.com/p/flask/)
- [Python](https://docs.python.org/3/)
- [PostgreSQL](https://www.postgresql.org/)

## Getting started

- To get started, install vagrant and VirtualBox. You'll find a detailed guide for installing [here](https://classroom.udacity.com/nanodegrees/nd004-ent/parts/72d6fe39-3e47-45b4-ac52-9300b146094f/modules/0f94ae26-c39d-4231-924b-b1eb6e06cf41/lessons/5475ecd6-cfdb-4418-85a2-f2583074c08d/concepts/14c72fe3-e3fe-4959-9c4b-467cf5b7c3a0).
- Cd into the _vagrant_ directory and create a folder called _newsdata_
- Download the files [news.py](https://github.com/kimskovhusandersen/newsdata/blob/master/news.py), [newsdb.py](https://github.com/kimskovhusandersen/newsdata/blob/master/newsdb.py) and [newsdata.sql](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip), unzip and put them into the _newsdata_ directory.
- Start up the VM and login by using the commands `vagrant up` followed by `vagrant ssh`.
- On your virtual Linux machine, cd into _/vagrant/newsdata_ and use the command `psql -d news -f newsdata.sql.` to load the data.
- Run the webapp with the command `python news.py`
- Open your favorite browser and go to [localhost:8000](http://localhost:8000/)
- Once the webapp has loaded, you'll see the Newsdata log including the three following sections:
  1. Top 3 articles by views
  2. Top 3 authors by article views
  3. Dates on which requests errors were above 1%
- To close the connection from the command line press `ctrl + c`, logout of the VM with the command `ctrl + d` and shutdown your VM with the command `vagrant halt`.
