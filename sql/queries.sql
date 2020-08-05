---	How many different species of mushroom are there, if a species is identified by the attributes 1-20?

SELECT COUNT(DISTINCT (cap-shape, cap-color, odor, gill-size, gill-color, stalk-color-above-ring,
                        veil-color, ring-type, spore-print-color)) FROM mushrooms;

--- Does habitat and cap-color correlate?

--- Method 1 - this is a non-traditional way

SELECT COUNT(DISTINCT (habitat, cap-color)) FROM mushrooms;
SELECT COUNT(*) FROM mushrooms;

--- then calculate the ratio/% of distinct vs total number of records and use the result as an estimation of degree of "correlation" / or rather alignment

--- Method 2

--- use an ETL job to turn the two columns from String into Categorical Values and then use the SQL Pearson Correlation function (although it doesnt make a full sense
--- for categorical data)

SELECT corr("habitat", "cap-color") as "Corr Coef Using PGSQL Func" FROM mushrooms;

--- Method 3

---- probably thisis best done in programming code rather than SQL and by applying an ML algo like Clustering but using Gower Distance

--- Considering a specific geographical point, what colours should we be able to see in the 10 km around it?

