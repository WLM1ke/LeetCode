SELECT product_id
FROM (SELECT *
      FROM Products
      WHERE low_fats = 'Y'
        AND recyclable = 'Y')
         AS T