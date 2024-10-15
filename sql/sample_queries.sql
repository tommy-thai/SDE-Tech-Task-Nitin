-- Write SQL queries to answer these questions using the data you have loaded into BigQuery:
-- 1. Find the top 5 users with the highest number of posts.

SELECT userId, post_count
FROM (
    SELECT userId, COUNT(id) AS post_count, 
           RANK() OVER (ORDER BY COUNT(id) DESC) AS rank
    FROM `data-dev.ntntemp.post`
    GROUP BY userId
)
WHERE rank <= 5;

-- 2. For each of these top 5 users, calculate the average post length.

WITH post_counts AS (
  SELECT 
    userId, 
    COUNT(id) AS post_count,
    AVG(LENGTH(body)) AS avg_post_length
  FROM `data-dev.ntntemp.post`
  GROUP BY userId
),
ranked_users AS (
  SELECT 
    userId,
    post_count,
    avg_post_length,
    RANK() OVER (ORDER BY post_count DESC) AS rank
  FROM post_counts
)

SELECT 
  userId,
  post_count,
  avg_post_length
FROM ranked_users
WHERE rank <= 5
ORDER BY rank;



-- 3. Identify the day of the week when the most `lengthy` posts are created (assume all posts were created in the UTC timezone).
