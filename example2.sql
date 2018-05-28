--====
SELECT Name, Composer, Milliseconds 
  FROM %s 
 WHERE Milliseconds >= %d 
       AND 
       Milliseconds <= %d
 ORDER BY Milliseconds;
--====
