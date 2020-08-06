---	How many different species of mushroom are there, if a species is identified by the attributes 1-20?

SELECT COUNT(DISTINCT (cap_shape, cap_color, odor, gill_size, gill_color, stalk_color_above_ring,
                        veil_color, ring_type, spore_print_color)) FROM mushrooms;

--- Does habitat and cap-color correlate?

-- the data in these 2 columns is a) categorical and b) of different business semantics

--- Method 1 - find and count all rows containinng duplicate values in the 2 target columns. Then re;ate the count to the totl record count
-- to find a "pearson" like correlation cofecient but for Categroical data moreover f different business semantics

SELECT count(m.*)
FROM mushrooms m
JOIN (SELECT habitat, cap_color, COUNT(*)
FROM mushrooms
GROUP BY habitat, cap-color
HAVING count(*) > 1 ) b
ON m.habitat = b.habitat
AND m.cap_color = b.cao_color

-- the following query would have been true only in the case if the business semantics of the two columns were the same

SELECT count(*)
FROM mushrooms m
WHERE m.habitat = m.cap_color;

-- then determine the ration of the count obtained from the above and the total number of records in the dataset - this will provide a "pearson" like correlation coeficient

--- then calculate the ratio/% of distinct vs total number of records and use the result as an estimation of degree of "correlation" / or rather alignment

--- Method 2

--- use an ETL job to turn the two columns from String into Categorical Values and then use the SQL Pearson Correlation function (although it doesnt make a full sense
--- for categorical data)

--- Method 3

---- probably thisis best done in programming code rather than SQL and by applying an ML algo like Clustering but using Gower Distance


SELECT corr("habitat", "cap-color") as "Corr Coef Using PGSQL Func" FROM mushrooms;


-- Method 1 - based on faithful model of a circle

-- Equation of all points inside a Circle with Center with coordinates cx, cy and radius R
-- power((x-xc), 2) + power((y-cy), 2) <= power(R, 2)
-- Outstanding - need to include the formula for conversion from lat/lon degrees to miles - time is up however

SELECT cap_color, gill_color, Vail_color
FROM mushrooms
WHERE     power((lon-cx), 2) + power((lat-cy), 2) <= power(R, 2)

-- Method 2 - based on Square aproximation of Circle

--- Considering a specific geographical point, what colours should we be able to see in the 10 km around it?

-- Params

-- @MinLat, @MaxLat, @MinLong, @MaxLong: derived from the coordinates of square with side which is equal to the required radius

-- Query

SELECT cap_color, gill_color, Vail_color
FROM mushrooms
WHERE     lat >= @MinLat AND lat <= @MaxLat
      AND lon >= @MinLong AND lon <= @MaxLong
