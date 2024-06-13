import boto3
from datetime import datetime


def main():
    ACCESS_KEY = 'YOUR_ACCESS_KEY_ID' # YOUR_ACCESS_KEY_ID
    SECRET_KEY = 'YOUR_SECRET_ACCESS_KEY' # YOUR_SECRET_ACCESS_KEY
    INPUT_HOURS = 5 # HOURS
   
    # Getting access key age AWS Boto3
    #  reference - https://stackoverflow.com/questions/45156934/getting-access-key-age-aws-boto3
    iam = boto3.client('iam',
                       aws_access_key_id=ACCESS_KEY,
                       aws_secret_access_key=SECRET_KEY)

    # Get a list of IAM users
    response = iam.list_users()

    for user in response['Users']:
        # Get list of access keys by user
        res = iam.list_access_keys(UserName=user['UserName'])

        try:
            # Check if CreateDate information exists
            if res['AccessKeyMetadata'][0]['CreateDate'].date():
                # user information
                user_accesskeyid = res['AccessKeyMetadata'][0]['AccessKeyId']
                user_id = user['UserId']

                # Convert creation date string to standard format
                accesskey_timestamp = res['AccessKeyMetadata'][0]['CreateDate']
                accesskey_timestamp = accesskey_timestamp.strftime("%Y-%m-%d %H:%M:%S+00:00")
                accesskey_datetime = datetime.strptime(accesskey_timestamp, "%Y-%m-%d %H:%M:%S+00:00")

                # Convert current date and time string to standard format
                current_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S+00:00")
                current_datetime = datetime.strptime(current_timestamp, "%Y-%m-%d %H:%M:%S+00:00")

                # Units of time elapsed since access key creation
                time_delta = current_datetime - accesskey_datetime
                hours_difference = time_delta.total_seconds() / 3600
                hours_difference_int = int(hours_difference)

                # Return the User ID and Access Key ID of IAM Users that have been inactive for more than N hours.
                if INPUT_HOURS < hours_difference_int:
                    print('[DEBUG] user_id: '+ user_id + ' \t user_accesskeyid: '+ user_accesskeyid)
        except:
            pass


if __name__ == '__main__':
    main()
