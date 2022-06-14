
--dual source query processing
SELECT
	AD.*, A.Implant_Chip_ID , A.Breed 
FROM
	riya.Animals a
JOIN riya.Adoptions ad ON
	ad.Name = a.Name
	AND ad.Species = a.Species;

SELECT
	AD.*, A.Implant_Chip_ID , A.Breed 
FROM
	riya.Animals a
LEFT JOIN riya.Adoptions ad ON
	ad.Name = a.Name
	AND ad.Species = a.Species;

--joining multiple source dataset
SELECT
	*
FROM
	riya.Animals a
JOIN riya.Adoptions ad ON
	ad.Name = a.Name
	AND ad.Species = a.Species
JOIN riya.Persons p ON
	p.Email = ad.Adopter_Email ;
---
--Challenge: Query to report animal and their vaccination and include the one not vaccinated.
SELECT
	a.name,
	a.Species,
	a.Breed,
	a.Primary_Color ,
	v.Vaccination_Time,
	v.Name,
	p.first_name,
	p.last_name,
	sa.[Role]
FROM
	riya.Animals a
LEFT JOIN (riya.Vaccinations v --chiastic order
JOIN riya.Staff_Assignments sa ON
	sa.Email = v.Email
JOIN riya.Persons p ON
	p.Email = sa.Email) ON
	v.Name = a.Name
	AND v.Species = a.Species
ORDER BY
	a.Name ,
	a.Species,
	v.Vaccination_Time ;

--Grouping:  It is critical to understand and remember that whenever we leave the individual source rows behind and group them, we lose access to the original row details.
SELECT
	COUNT(*) species_count,
	a.Species, 	--only the group identifier(species) has the same value for all rows within the group.
	max(a.name) -- all the other expressions must be enclosed in a aggreagate function
	FROM riya.Animals a
GROUP BY
	a.Species;
--
SELECT
	name,
	species,
	count(*) AS count
FROM
	riya.Vaccinations v
GROUP BY
	name,
	Species ;
--Grouping Nulls:  Grouping of nullable expressions treats all nulls as a single group although one null is not equal to another null
SELECT
	species,
	Breed,
	count(*) AS num_of_animals
FROM
	riya.Animals a
GROUP BY
	species ,
	Breed ;
--Grouping Filters
 SELECT
	Adopter_Email ,
	count (*) num_of_adoptions
FROM
	riya.Adoptions a
GROUP BY
	Adopter_Email
HAVING
	count(*) > 1
	AND Adopter_Email NOT LIKE '%gmail.com' SELECT
	Adopter_Email ,
	count (*) num_of_adoptions
FROM
	riya.Adoptions a 
GROUP BY Adopter_Email 
HAVING count(*) > 1 AND Adopter_Email NOT LIKE '%gmail.com' -- It doesn't make sense to let the GROUP BY process all adopters, including those with a Gmail account, only to remove them immediately after.
	ORDER BY num_of_adoptions DESC;

--
SELECT
	Adopter_Email ,
	count (*) num_of_adoptions
FROM
	riya.Adoptions a
WHERE
	Adopter_Email NOT LIKE '%gmail.com'
GROUP BY
	Adopter_Email
HAVING
	count(*) > 1
ORDER BY
	num_of_adoptions DESC;

--Challenge: Filtering and Grouped query
SELECT
	A.species,
	a.name,
	max(a.Primary_Color),
	max(a.breed),
	COUNT(v.Vaccine) AS num_of_vaccination
FROM
	riya.Animals a
LEFT JOIN riya.Vaccinations v ON
	v.Name = a.Name
	AND v.Species = a.Species
GROUP BY
	a.Species,
	a.Name ;



