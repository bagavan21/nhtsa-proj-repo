import pyspark
import SparkSession
from pyspark.functions import col, max as max_

# Initialize Spark session
spark = SparkSession.builder.appName("HighestSalary").getOrCreate()

# Sample DataFrames
employee = spark.createDataFrame([
    (1, "Alice", 70000, 1),
    (2, "Bob", 60000, 1),
    (3, "Cathy", 80000, 2),
    (4, "David", 90000, 2),
    (5, "Eve", 50000, 1),
    (6, "Frank", 75000, 2)
], ["empNUM", "empNAME", "empSALARY", "depNUM"])

department = spark.createDataFrame([
    (1, "HR"),
    (2, "Engineering")
], ["depNUM", "depName"])

# Register DataFrames as tables
employee.createOrReplaceTempView("employee")
department.createOrReplaceTempView("department")

# Spark SQL query
highest_salary_query = """
SELECT e.empNUM, e.empNAME, e.empSALARY, d.depName
FROM employee e
JOIN department d ON e.depNUM = d.depNUM
WHERE e.empSALARY = (
    SELECT MAX(empSALARY)
    FROM employee
    WHERE depNUM = e.depNUM
)
"""

# Execute query
result = spark.sql(highest_salary_query)
result.show()
