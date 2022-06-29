-- SQL script that lists all bands with Glam rock as their main style, ranked by their longevity

-- Requirements:

--	Import this table dump: metal_bands.sql.zip
--	Column names must be: band_name and lifespan (in years)
--	You should use attributes formed and split for computing the lifespan

SELECT band_name AS band_name, IFNULL(split, 2022) - IFNULL(formed, 0) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
