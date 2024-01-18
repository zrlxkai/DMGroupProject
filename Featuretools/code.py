import featuretools as ft
import pandas as pd

# Define data for Customers, Products, Orders, and Time
sales_df = pd.read_csv(r"C:\Users\User\OneDrive\Desktop\Tutorial UM\WIE3007 DATA MINING AND WAREHOUSING\dataset\sales_receipts.csv")
customer_df = pd.read_csv(r"C:\Users\User\OneDrive\Desktop\Tutorial UM\WIE3007 DATA MINING AND WAREHOUSING\dataset\customer.csv")
product_df = pd.read_csv(r"C:\Users\User\OneDrive\Desktop\Tutorial UM\WIE3007 DATA MINING AND WAREHOUSING\dataset\product.csv")

# Create an EntitySet
es = ft.EntitySet(id='coffee_data')

# Add dataframes as entities to the EntitySet
es.add_dataframe(dataframe_name='customer', dataframe=customer_df, index=' customer_id')
es.add_dataframe(dataframe_name='product', dataframe=product_df, index=' product_id')
es.add_dataframe(dataframe_name='sales', dataframe=sales_df, index=' sales_id')

# Define the relationships between entities
relationships = [
    ('customer', ' customer_id', 'sales', ' customer_id'),
    ('product', ' product_id', 'sales', ' product_id')
]

# Add the defined relationships to the EntitySet
for relationship in relationships:
    es = es.add_relationship(parent_dataframe_name=relationship[0], 
                            parent_column_name=relationship[1],
                            child_dataframe_name=relationship[2],
                            child_column_name=relationship[3])


# Perform Deep Feature Synthesis with aggregation primitives
feature_matrix, feature_defs = ft.dfs(entityset=es, target_dataframe_name='sales',
                                      agg_primitives=['sum', 'mean', 'count', 'mode'],  # Add your aggregation primitives
                                      trans_primitives=['month', 'weekday', 'day'],  # Add your transformation primitives
                                      max_depth=2)

# Print the generated features
print(feature_matrix)

