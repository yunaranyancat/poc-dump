## CVE-2023-36630 Writeup

Attack details :
![1](https://github.com/yunaranyancat/poc-dump/blob/main/cloudpanel/1.png)

To exploit this vulnerability, a normal "User" can upload a file to the server using File Manager feature which contains path traversal vulnerability. 

![2](https://github.com/yunaranyancat/poc-dump/blob/main/cloudpanel/2.png)

By uploading a file and modifying the "upload_fullpath" value in the upload request by prepending "../../../../" in front of it, and attacker will be able to traverse the file path and the file will be uploaded with "root" privilege, which is a second vulnerability.

![3](https://github.com/yunaranyancat/poc-dump/blob/main/cloudpanel/3.png)

Since the application requires ssh service, the ssh will be installed into the server, the attacker can upload their own SSH keys and create/overwrite "../../../../../../root/.ssh/authorized_keys" value and get access to the server as root.

![4](https://github.com/yunaranyancat/poc-dump/blob/main/cloudpanel/4.png)

Recommendations :
Ensure proper access control is enforced when uploading file to the server.

## AFFECTED VERSION
CloudPanel v2.0.0 - v2.3.0

## FIXED VERSION
CloudPanel v2.3.1 - https://www.cloudpanel.io/docs/v2/changelog/

## TIMELINE
07-06-2023 – Exploit Found

08-06-2023 – Privately disclose to vendor

09-06-2023 – Submitted to CVE assignee

10-06-2023 - Patch released by vendor

25-06-2023 – CVE number assigned by MITRE

26-06-2023 – Exploit released to the public
