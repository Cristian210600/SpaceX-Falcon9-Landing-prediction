-- Original query from the supplied IBM capstone SQL notebook.
SELECT AVG("PAYLOAD_MASS__KG_") AS Average_Payload_Mass
FROM SPACEXTABLE
WHERE "Booster_Version" LIKE 'F9 v1.1%';
