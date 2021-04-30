##### CREATE TABLE #####
import boto3

# Get the service resource.
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('DOI')
# def create_table():
#   table = dynamodb.create_table(
#       TableName='DOI',
#       KeySchema=[
#           {
#               'AttributeName': 'DOI',
#               'KeyType': 'HASH'
#           },
#       ],
#       AttributeDefinitions=[
#           {
#               'AttributeName': 'DOI',
#               'AttributeType': 'S'
#           },
#       ],
#       ProvisionedThroughput={
#           'ReadCapacityUnits': 5,
#           'WriteCapacityUnits': 5
#       }
#   )

def put_item(DOI):
  table.put_item(
     Item={
          'DOI': DOI,
      }
  )
  
# def get_item (DOI):
#   response = table.get_item(
#       Key={
#           'DOI': DOI,
#       }
#   )
#   item = response['Item']
#   return len(item)


def exists(DOI):
  try:
    item = len(self.table.get_item(hash_key=DOI))
  except:
    item = 0
  return item

def write_DOI(DOI):
  if exists(DOI) != 0:
    return True
  else:
    put_item(DOI)
    return False

#write_DOI('yoyo')
