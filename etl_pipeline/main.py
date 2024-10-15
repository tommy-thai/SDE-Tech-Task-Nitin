from api_client import APIClient
from transform_data import DataTransformer
from load_to_database import BigQueryLoader

def main():
    # API URL
    url = "https://jsonplaceholder.typicode.com/posts"

    # Step 1: Fetch Data
    api_client = APIClient(url)
    data = api_client.fetch_data()

    if data:
        # Step 2: Transform Data
        transformer = DataTransformer(data)
        transformed_data = transformer.transform()

        # Step 3: Load Transformed Data into BigQuery
        loader = BigQueryLoader(
            project_id='data-dev',
            dataset_id='ntntemp',
            table_id='post'
        )
        
        # Ensure the table exists
        loader.create_table_if_not_exists()

        # Load transformed data into BigQuery
        loader.load_data(transformed_data)

if __name__ == "__main__":
    main()
