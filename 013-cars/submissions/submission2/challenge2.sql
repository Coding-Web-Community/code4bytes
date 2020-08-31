SELECT ROUND(AVG((mileage / price)), 2) AS mpp, color FROM car
where price != 0 
GROUP BY color
ORDER BY mpp DESC
