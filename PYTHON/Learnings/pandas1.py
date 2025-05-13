import pandas as pd

# Sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Alice', 'Eve', 'Bob', 'Eve'],
    'City': ['New York', 'Los Angeles', 'New York', 'Chicago', 'Los Angeles', 'Chicago'],
    'Event': ['Concert', 'Sports', 'Concert', 'Theatre', 'Sports', 'Theatre']
}
df = pd.DataFrame(data)

# Detect duplicates
duplicates = df.duplicated()
print(duplicates)
