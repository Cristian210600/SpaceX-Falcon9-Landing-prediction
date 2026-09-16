-- Original query from the supplied IBM capstone SQL notebook.
SELECT MIN("Date") AS First_Successful_Ground_Landing
FROM SPACEXTABLE
WHERE "Landing_Outcome" = 'Success (ground pad)';
