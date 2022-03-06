import vpk
import os


this_path = os.getcwd() + "/DECOMPILED"
if not os.path.exists("./File.vpk"):
	class VpkNotFound(BaseException):
		pass
	raise VpkNotFound("\033[31mFile.pak not found,\033[1m rename your .vpk file to File.vpk\033[0m")

PAK = vpk.open("File.vpk")
if not os.path.exists(this_path):
	os.mkdir(this_path)
	
clear = "\033[0m"
green = "\033[1m\033[32m"
for path in PAK:
	file = PAK.get_file(path)
	full_path = this_path + "/" + path
	if not os.path.exists(full_path):
		dir = path.split("/")[:-1]
		file_dir = ""
		for folder in dir:
			file_dir += folder + "/"
			if not os.path.exists(f"{this_path}/{file_dir}"):
				os.mkdir(f"{this_path}/{file_dir}")
		
		print(f"""\033[1mExtracting:{clear} \033[1m\033[33mFile.vpk/{path}
\033[0m\033[1mto \033[33m{this_path}/{path}{clear}""")
		status = os.path.exists(this_path+'/'+file_dir)
		print(f"\033[1mStatus: {green}{status}{clear}", end = "\n\n")
	else:
		print(f"""
\033[1mFile: \033[33mFile.vpk/{path}
  \033[36mExists:{green} {os.path.exists(full_path)}
  \033[36mPath: \033[33m{full_path}
{clear}""")
	file.save(f"{this_path}/{path}")