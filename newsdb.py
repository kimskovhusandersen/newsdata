#!/usr/bin/env python3
#
# PostgreSQL queries to fetch data from the database using Psycopg2
import psycopg2

DBNAME = "news"


def execute_query(sql):
    try:
        db = psycopg2.connect(database=DBNAME)
        c = db.cursor()
        c .execute(sql)
        query = c.fetchall()
        db.close()
        return query
    except:
        pass


"""Return the most popular three articles of all time."""
def get_top_articles():
    return execute_query("""
    SELECT articles.title AS title, count(log.path) AS num
    FROM articles, log
    WHERE '/article/' || articles.slug = log.path
    GROUP BY articles.title
    ORDER BY num DESC
    LIMIT 3
    """)


"""Return the most popular article authors of all time."""
def get_top_authors():
    return execute_query("""
    SELECT authors.name AS author, count(log.path) AS num
    FROM authors, articles, log
    WHERE authors.id = articles.author
    AND '/article/' || articles.slug = log.path
    GROUP BY authors.name
    ORDER BY num DESC
    LIMIT 3
    """)


"""Return dates where requests errors were above 1%."""
def get_errors():
    return execute_query("""
    SELECT date, round((num404/(num404+num200)*100.0), 2)
        AS error_ratio
    FROM(
        SELECT t1.date, t1.num AS num200, t2.num AS num404
        FROM(
            SELECT time::timestamp::date AS date,
                status, count(status)::numeric AS num
            FROM log
            GROUP BY date, status
        ) t1
        INNER JOIN(
            SELECT time::timestamp::date AS date,
                status, count(status)::numeric AS num
            FROM log
            GROUP BY date, status
        ) t2
        ON t1.date = t2.date
        AND t1.num > t2.num
    ) AS temporary
    WHERE round((num404/(num404+num200)*100.0),2) >= 1.00
    """)
