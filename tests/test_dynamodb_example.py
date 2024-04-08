import boto3
import pytest
from moto import mock_aws
from botocore.exceptions import ClientError
from src.boto3_example import DynamodBExample

@mock_aws
def test_create_dynamo_table():
    '''
    Test creating a DynamoDB table.
    '''
    # Create DynamoDB resource
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

    # Create a table
    dynamodb.create_table(
        TableName='my_table',
        KeySchema=[
            {
                'AttributeName': 'id',
                'KeyType': 'HASH'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'id',
                'AttributeType': 'N'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )

    # Check if table with name 'my_table' exists
    tables = dynamodb.tables.all()
    table_names = [table.name for table in tables]
    assert 'my_table' in table_names

@mock_aws
def test_add_dynamo_record_table():
    '''
    Test adding a record to a DynamoDB table.
    '''
    # Create DynamoDB resource
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

    # Create a table
    table = dynamodb.create_table(
        TableName='my_table',
        KeySchema=[
            {
                'AttributeName': 'id',
                'KeyType': 'HASH'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'id',
                'AttributeType': 'N'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )

    # Wait until the table exists
    table.meta.client.get_waiter('table_exists').wait(TableName='my_table')

    # Instantiate DynamodBExample
    dynamodb_example = DynamodBExample()

    # Add record to the table
    dynamodb_example.add_dynamo_record('my_table', {'id': 123, 'name': 'John Doe'})

@mock_aws
def test_add_dynamo_record_table_failure():
    '''
    Test failure scenario when adding a record to a DynamoDB table.
    '''
    # Instantiate DynamodBExample
    dynamodb_example = DynamodBExample()

    # Create the Movies table
    dynamodb_example.create_movies_table()

    # Attempt to add record to the Movies table with invalid data
    with pytest.raises(ClientError):
        dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
        table = dynamodb.Table('Movies')  # Access the Movies table
        table.put_item(Item={'year': 'invalid', 'title': 'John Doe'})