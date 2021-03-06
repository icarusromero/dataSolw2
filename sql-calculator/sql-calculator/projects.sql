--BASIC INFO
--Problem 1
SELECT AVG(grade)
FROM grades
WHERE project_title = 'News Aggregator';
--Result: 30

--Problem 2
SELECT SUM(grade)
FROM grades
WHERE project_title = 'Recipe Storage';
--Result: nothing

--Problem 3
SELECT COUNT(project_title)
FROM grades;
--Result: 13

--Problem 4
SELECT MAX(grade)
FROM grades
WHERE project_title = 'News Aggregator';
--Result: 50

-- Problem 5
SELECT MIN(grade)
FROM grades
--Result: 0


--JOINS
--Problem 1
SELECT grades.grade, grades.project_title, students.first_name || ' ' || students.last_name student_name
FROM grades
JOIN students
ON grades.student_github=students.github;
--Result: 
--  grade |  project_title  |  student_name
-- -------+-----------------+-----------------
--     10 | News Aggregator | Jane Hacker
--     50 | News Aggregator | Sarah Developer
--      2 | Snake Game      | Jane Hacker
--    100 | Snake Game      | Sarah Developer

--Problem 2
SELECT p.id, p.title, COUNT(g.grade)
FROM projects p
INNER JOIN grades g
ON p.title=g.project_title
GROUP BY p.id;
--Result: 
--  id |      title      | count
-- ----+-----------------+-------
--   1 | Snake Game      |    11
--   2 | News Aggregator |     2


--FILTERING USING AGGREGATES
--Problem 1
SELECT grade
FROM grades
WHERE project_title = 'News Aggregator'
AND grade >
    (SELECT AVG(grade)
    FROM grades
    WHERE project_title = 'News Aggregator');
--Result: 1

--Problem 2
SELECT COUNT(grade)
FROM grades
WHERE project_title = 'Snake Game'
AND grade >
    (SELECT max_grade
    FROM projects
    WHERE title = 'Snake Game');
--Result: 7

--Problem 3

--Result:


--WORKING WITH STRINGS
--Problem 1
SELECT CONCAT('Congrats, ', s.first_name, ' ', s.last_name, ', you recieved a ', g.grade, ' on ', g.project_title, '.')
FROM students s 
JOIN grades g 
ON s.github=g.student_github 
WHERE g.grade >= 90;
--Result: Congrats, Sarah Developer, you recieved a 100 on Snake Game.

--Problem 2
SELECT CONCAT('Your assignment needs improvement, you recieved a ', grade, ' on ', project_title, '.') 
FROM grades 
WHERE grade <= 70;
--Result: 
--                                   concat
-- --------------------------------------------------------------------------
--  Your assignment needs improvement, you recieved a 10 on News Aggregator.
--  Your assignment needs improvement, you recieved a 50 on News Aggregator.
--  Your assignment needs improvement, you recieved a 2 on Snake Game.
--  Your assignment needs improvement, you recieved a 0 on Snake Game.
--  Your assignment needs improvement, you recieved a 0 on Snake Game.
--  Your assignment needs improvement, you recieved a 50 on Snake Game.
--  Your assignment needs improvement, you recieved a 64 on Snake Game.

--Problem 3
SELECT CONCAT(LOWER(first_name), '-', LOWER(last_name)) 
FROM students;
--Result: jane-hacker, sarah-developer