# S3_IAM_withFlask

I implemented S3 and IAM service for my website :
  - S3 : Create Bucket , Delete Bucket , Upload File , Download File
  - IAM : Listed Policies and created different options for user and groups both.
    
- List Group , 
- Create Group (Create a group and attach as many as all allowed policies to a group) , 
- Edit Group (Change can be implemented to any except the root - priviledge given through 
    python-flask (manually)) , 
- Delete Group (You can delete a group - if empty , if policy attached and even if this group is 
    attached to a user. You can't delete a root group - priviledge from RemoveGroup() in app.py)

- List User , 
- Create User (Create a user and attach a group to user),
- Edit User (Change Username of all user except the root - priviledge given through flask in EditUser() in app.py )
- Delete User (You can delete a user - if empty , if group attached. But root Users can't be deleted - priviledge from RemoveUser() in app.py)
