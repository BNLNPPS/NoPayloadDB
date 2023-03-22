get_payload_iovs = '''
SELECT pt.name AS payload_type_name, pi.payload_url, pi.major_iov, pi.minor_iov
FROM "PayloadList" pl
JOIN "GlobalTag" gt ON pl.global_tag_id = gt.id AND gt.name = %(my_gt)s
JOIN LATERAL (
   SELECT *
   FROM   "PayloadIOV" pi
   WHERE  pi.payload_list_id = pl.id
     AND pi.comb_iov <= CAST(%(my_major_iov)s + CAST(%(my_minor_iov)s AS DECIMAL(19,0)) / 10E18 AS DECIMAL(38,19)) 
   ORDER BY pi.comb_iov DESC NULLS LAST
   LIMIT 1
) pi ON true
JOIN "PayloadType" pt ON pl.payload_type_id = pt.id;
'''
