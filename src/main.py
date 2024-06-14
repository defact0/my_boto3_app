import boto3
from datetime import datetime


def main():
    ACCESS_KEY = 'YOUR_ACCESS_KEY_ID' # YOUR_ACCESS_KEY_ID
    SECRET_KEY = 'YOUR_SECRET_ACCESS_KEY' # YOUR_SECRET_ACCESS_KEY
    INPUT_HOURS = 25000 # HOURS
    
    # Convert current date and time string to standard format
    current_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    current_datetime = datetime.strptime(current_timestamp, "%Y-%m-%d %H:%M:%S")
   
    # Getting access key age AWS Boto3
    #  reference - https://stackoverflow.com/questions/45156934/getting-access-key-age-aws-boto3
    iam = boto3.client('iam',
                       aws_access_key_id=ACCESS_KEY,
                       aws_secret_access_key=SECRET_KEY)

    # Get a list of IAM users
    response = iam.list_users()
    for user in response['Users']:
        # Get list of access keys by user
        response_access_key = iam.list_access_keys(UserName=user['UserName'])
        UserId = user['UserId']
        
        for access_key in response_access_key['AccessKeyMetadata']:
            UserName = access_key['UserName']
            AccessKeyId = access_key['AccessKeyId']
            Status = access_key['Status']
            CreateDate = access_key['CreateDate']
            
            if 'Active' == Status:
                # Convert creation date string to standard format
                access_key_timestamp = access_key['CreateDate']
                access_key_timestamp = access_key_timestamp.strftime("%Y-%m-%d %H:%M:%S")
                access_key_datetime = datetime.strptime(access_key_timestamp, "%Y-%m-%d %H:%M:%S")

                # Units of time elapsed since access key creation
                time_delta = current_datetime - access_key_datetime
                hours_difference = time_delta.total_seconds() / 3600
                hours_difference_int = int(hours_difference)
                                
                # Return the User ID and Access Key ID of IAM Users that have been inactive for more than N hours.
                if INPUT_HOURS < hours_difference_int:
                    print(UserId + ", " + AccessKeyId)

if __name__ == '__main__':
    main()
