# GROUP MKR
## Create User groups in the python shell 





## Procedure

- Install the module
- Create a .py file in the apps folder that contains the views and models file
- Import the add_group function from the module in the file 'from GroupMkr import add_group'
- Add this line to the file 'add_group (group_name='travellers', permission= 'can book rooms')', edit the strings to your choice
- Add as many permissions in new lines before running
- To create the groups from the shell, run the 'python manage.py shell' command and run the 'exec(open('app_name/file').read())'. Edit the app_name and file 
- To create new permissions, remove the already existing permissions and add new ones before running the commands

## Check the github repo for the code if interested
https://github.com/mezardini/GroupMkr.git