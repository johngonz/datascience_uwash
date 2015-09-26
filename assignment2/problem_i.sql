SELECT x,y,MAX(s) FROM(
SELECT a.docid x, b.docid y, SUM(a.count*b.count) s
FROM (

SELECT * FROM frequency
UNION
SELECT 'q' as docid, 'washington' as term, 1 as count 
UNION
SELECT 'q' as docid, 'taxes' as term, 1 as count
UNION 
SELECT 'q' as docid, 'treasury' as term, 1 as count) a, Frequency b

WHERE a.term = b.term AND  a.docid = "q" 
GROUP BY a.docid, b.docid);
