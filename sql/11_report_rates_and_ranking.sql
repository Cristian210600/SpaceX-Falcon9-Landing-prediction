-- site_rates
SELECT Launch_Site, COUNT(*) AS launches,
 SUM(CASE WHEN TRIM(Landing_Outcome) LIKE 'Success%' THEN 1 ELSE 0 END) AS successes,
 ROUND(100.0*SUM(CASE WHEN TRIM(Landing_Outcome) LIKE 'Success%' THEN 1 ELSE 0 END)/COUNT(*),2) AS rate_pct
 FROM SPACEXTBL GROUP BY Launch_Site ORDER BY rate_pct DESC;

-- historical_rank
SELECT TRIM(Landing_Outcome) AS outcome, COUNT(*) AS launches
 FROM SPACEXTBL WHERE Date BETWEEN '2010-06-04' AND '2017-03-20'
 GROUP BY TRIM(Landing_Outcome) ORDER BY launches DESC, outcome;

-- annual
SELECT substr(Date,1,4) AS year, COUNT(*) AS launches,
 SUM(CASE WHEN TRIM(Landing_Outcome) LIKE 'Success%' THEN 1 ELSE 0 END) AS successes
 FROM SPACEXTBL GROUP BY substr(Date,1,4) ORDER BY year;