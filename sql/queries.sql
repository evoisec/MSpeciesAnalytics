---	How many different species of mushroom are there, if a species is identified by the attributes 1-20?

SELECT COUNT(DISTINCT (cap_shape, cap_color, odor, gill_size, gill_color, stalk_color_above_ring,
                        veil_color, ring_type, spore_print_color)) FROM mushrooms;

--- Does habitat and cap-color correlate?

--- Method 1

SELECT count(*)
FROM mushrooms m
WHERE m.habitat = m.cap_color;

-- then determine the ration of the count obtained from the above and the total number of records in the dataset - this will provide a "pearson" like correlation coeficient

--- then calculate the ratio/% of distinct vs total number of records and use the result as an estimation of degree of "correlation" / or rather alignment

--- Method 2

--- use an ETL job to turn the two columns from String into Categorical Values and then use the SQL Pearson Correlation function (although it doesnt make a full sense
--- for categorical data)

SELECT corr("habitat", "cap-color") as "Corr Coef Using PGSQL Func" FROM mushrooms;

--- Method 3

---- probably thisis best done in programming code rather than SQL and by applying an ML algo like Clustering but using Gower Distance

--- Considering a specific geographical point, what colours should we be able to see in the 10 km around it?

