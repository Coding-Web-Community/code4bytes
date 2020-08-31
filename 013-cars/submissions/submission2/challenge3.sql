SELECT ROUND(AVG(price), 2) AS mean, ROUND(STDDEV(price), 2) as standard_deviation
FROM car WHERE state = 'california'
