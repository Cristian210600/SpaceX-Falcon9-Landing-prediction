-- Original query from the supplied IBM capstone SQL notebook.
SELECT
    "Mission_Outcome",
    COUNT(*) AS Number_Of_Missions
FROM SPACEXTABLE
GROUP BY "Mission_Outcome";
