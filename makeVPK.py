import vpk
import os

PAK_path = os.getcwd() + "/NEWVPK"
if not os.path.exists(PAK_path):
	class DirNotFound(BaseException):
		pass
	raise DirNotFound("""
\033[31m You must create folder \033[1mNEWVPK\033[0m\033[31m and move files to compile inside
\033[0m""")
else:
	try:
		newVpk = vpk.new("./NEWVPK")
		newVpk.save("NewVpk.vpk")
		print(f"""
\033[1m\033[33mFile saved as NewVpk.vpk
in {os.getcwd()}\033[0m\n""")
	except RuntimeError as error:
		print(f"\033[1m\033[31m{error}\033[0m")