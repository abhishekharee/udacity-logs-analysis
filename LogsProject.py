#!/usr/bin/env python

# Import PostgreSQL library
import psycopg2

# Connect to 'news' database
db = psycopg2.connect(database="news")
# Create cursor
cursor = db.cursor()

# Question 1: What are the most popular three articles of all time?

# Execute query
cursor.execute(
    '''SELECT
         articles.title AS title,
         COUNT(log.id) AS hits
       FROM
         log
       LEFT JOIN
         (
           SELECT
             CONCAT('/article/',slug) AS path,
             title
           FROM
             articles
           GROUP BY
             1, 2
         ) AS articles
         ON log.path = articles.path
       WHERE
         articles.title IS NOT NULL
       GROUP BY
         articles.title
       ORDER BY
         hits DESC
       LIMIT 3
         '''
)
# Store results in a variable
results = cursor.fetchall()
# Print results
print 'The top three articles are:'
for i in results:
    print "  ", i[0], "(", i[1], "Views )"

# Question 2: Who are the most popular article authors of all time?

cursor = db.cursor()
cursor.execute(
    '''SELECT
         articles_with_authors.name AS name,
         COUNT(log.id) AS hits
       FROM
         log
       LEFT JOIN
         (
           SELECT
             CONCAT('/article/',articles.slug) AS path,
             authors.name AS name
           FROM
             articles
           LEFT JOIN authors
             ON authors.id = articles.author
           GROUP BY
             1, 2
         ) AS articles_with_authors
         ON log.path = articles_with_authors.path
       WHERE
         articles_with_authors.path IS NOT NULL
       GROUP BY
         articles_with_authors.name
       ORDER BY
         hits DESC
         '''
)
results = cursor.fetchall()
print 'The most popular authors, by page view, are:'
for i in results:
    print "  ", i[0], "(", i[1], "Views )"

# Question 3: On which days did more than 1% of requests lead to errors?

cursor = db.cursor()
cursor.execute(
    '''SELECT
         error_log.date AS date,
         CONCAT(
             ROUND(
                 (
                   CAST(error_log.errors AS DECIMAL)
                   / CAST(total_hits.total_hits AS DECIMAL)
                   * 100),
                  1),
              '%') AS error_rate
       FROM
         (
           SELECT
             DATE(time) as date,
             COUNT(status) AS errors
           FROM
             log
           WHERE
             status != '200 OK'
           GROUP BY 1
         ) error_log
       LEFT JOIN
         (
           SELECT
             DATE(time) as date,
             COUNT(status) total_hits
           FROM
             log
           GROUP BY
             1
         ) AS total_hits
         ON error_log.date = total_hits.date
       WHERE
         ROUND(
             (
               CAST(error_log.errors AS DECIMAL)
               / CAST(total_hits.total_hits AS DECIMAL)
               * 100
              ),
              2) > 1
       ORDER BY
         error_rate DESC
         '''
)
results = cursor.fetchall()
print 'Days where errors exceeded 1% are:'
for i in results:
    print "  ", i[0], "( Error Rate:", i[1], ")"

# Disconnect from database
db.close()
