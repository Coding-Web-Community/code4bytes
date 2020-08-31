SELECT
	color,
	AVG(price/mileage) AS ppm
FROM
	car.car
GROUP BY
	color;
