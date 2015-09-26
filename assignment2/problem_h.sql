SELECT a.docid, b.docid, SUM(a.count*b.count)
FROM Frequency a, Frequency b
WHERE a.term = b.term AND  a.docid = "10080_txt_crude" AND b.docid = "17035_txt_earn" 
GROUP BY a.docid, b.docid;

--substitute a.docid > b.docid for the last two WHERE expressions to get the upper triangular similarity matrix