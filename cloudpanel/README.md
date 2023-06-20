Attack details :
![]()

To exploit this vulnerability, a normal "User" can upload a file to the server using File Manager feature which contains path traversal vulnerability. 

![]()

By uploading a file and modifying the "upload_fullpath" value in the upload request by prepending "../../../../" in front of it, and attacker will be able to traverse the file path and the file will be uploaded with "root" privilege, which is a second vulnerability.

![]()

Since the application requires ssh service, the ssh will be installed into the server, the attacker can upload their own SSH keys and create/overwrite "../../../../../../root/.ssh/authorized_keys" value and get access to the server as root.

![]()

Recommendations :
Ensure proper access control is enforced when uploading file to the server.
