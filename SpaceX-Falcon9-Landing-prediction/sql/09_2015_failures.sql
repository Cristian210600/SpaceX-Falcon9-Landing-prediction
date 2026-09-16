-- Original query from the supplied IBM capstone SQL notebook.
SELECT
    SUBSTR("Date", 6, 2) AS Month,
    "Landing_Outcome",
    "Booster_Version",
    "Launch_Site"
FROM SPACEXTABLE
WHERE SUBSTR("Date", 1, 4) = '2015'
  AND "Landing_Outcome" = 'Failure (drone ship)';
