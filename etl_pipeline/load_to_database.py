from google.cloud import bigquery
from google.oauth2 import service_account

class BigQueryLoader:
    def __init__(self, project_id, dataset_id, table_id):
        self.project_id = project_id
        self.dataset_id = dataset_id
        self.table_id = table_id
        #self.credentials = service_account.Credentials.from_service_account_file(credentials_path)
        #self.client = bigquery.Client(credentials=self.credentials, project=self.project_id)
        self.client = bigquery.Client(project=self.project_id)

    def create_table_if_not_exists(self):
        table_ref = self.client.dataset(self.dataset_id).table(self.table_id)
        try:
            self.client.get_table(table_ref)
            print(f"Table {self.table_id} already exists.")
        except Exception:
            schema = [
                bigquery.SchemaField('userId', 'INTEGER'),
                bigquery.SchemaField('id', 'INTEGER'),
                bigquery.SchemaField('title', 'STRING'),
                bigquery.SchemaField('body', 'STRING'),
                bigquery.SchemaField('source', 'STRING'),
            ]
            table = bigquery.Table(table_ref, schema=schema)
            self.client.create_table(table)
            print(f"Table {self.table_id} created.")

    def load_data(self, data):
        table_ref = self.client.dataset(self.dataset_id).table(self.table_id)
        errors = self.client.insert_rows_json(table_ref, data)

        if not errors:
            print("Data loaded successfully.")
        else:
            print(f"Errors occurred: {errors}")
