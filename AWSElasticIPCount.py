import boto3
client = boto3.client('ec2')
print(client)

def countUsedEIP(): #Counts and returns number of used EIPs in specified account
    addresses_dict = client.describe_addresses()
    count = 0
    for eip_dict in addresses_dict['Addresses']:
        count+= 1
        # print(eip_dict['PublicIp'])
    return count

def maxAvailableEIP(): #returns maximum number of EIPs available in AWS account
    response = client.describe_account_attributes(
    AttributeNames=[
        'vpc-max-elastic-ips',
    ],)
    for i in response['AccountAttributes']:
       for j in i['AttributeValues']:
           maxEip = j['AttributeValue']
    return maxEip

used = countUsedEIP()
maximum = maxAvailableEIP()

print('Maximum number of Elastic IPs available in AWS account is: ', maximum)
print('Number of Elastic IPs used in AWS account is:', used)