from http import client
from pydoc import cli
import boto3

class Iam:

    def list_Users():
        
        client = boto3.client('iam')
        return client.list_users()

    def create_User(Name,gName):

        client = boto3.client('iam')
        client.create_user(UserName=Name)
        client.add_user_to_group(GroupName=gName,UserName=Name)
    
    def edit_User(Name,newName):
        client = boto3.client('iam')
        client.update_user(UserName=Name,NewUserName=newName)

    def delete_User(Name):
        client = boto3.client('iam')
        Group_names = client.list_groups_for_user(UserName=Name)['Groups']
        for ele in Group_names:
            client.remove_user_from_group(GroupName=ele['GroupName'],UserName=Name)
        client.delete_user(UserName=Name)

    def list_Groups():
        client = boto3.client('iam')
        return client.list_groups()

    def create_Group(Name,PName):
        client = boto3.client('iam')
        client.create_group(GroupName=Name)
        print(PName)
        if len(PName) == 1:
            client.attach_group_policy(GroupName=Name,PolicyArn=PName[0])
        else:
            for ele in PName:
                print(ele)
                client.attach_group_policy(GroupName=Name,PolicyArn=ele)

    def edit_Group(name,NewName):
        client = boto3.client('iam')
        client.update_group(GroupName=name,NewGroupName=NewName)

    def remove_Group(Name):
        client = boto3.client('iam')
        Policy_names = client.list_attached_group_policies(GroupName=Name)['AttachedPolicies']
        user_names = client.list_users()['Users']
        
        for ele in Policy_names:
            client.detach_group_policy(PolicyArn=ele['PolicyArn'],GroupName=Name)
            for i in user_names:
                try:
                    client.remove_user_from_group(UserName=i['UserName'], GroupName=Name)
                except :               
                    pass

        client.delete_group(GroupName=Name)

    def list_Policy():
        client = boto3.client('iam')
        return client.list_policies()

    # def test(val):
    #     client = boto3.client('iam')
        
    #     return client.list_policies(PolicyUsageFilter='PermissionsBoundary') 