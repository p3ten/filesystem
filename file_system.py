class FileSystem:
    def __init__(self):
        self.file_system = {"": {"type": "dir", "contents": {}}}
        self.current_dir = ""

    def create_file(self, path, content=""):
        components = path.split("/")
        file_name = components[-1]
        dir_path = "/".join(components[:-1])
        dir_dict = self.get_directory_dict(dir_path)
        if dir_dict:
            dir_dict["contents"][file_name] = {"type": "file", "content": content}
        else:
            print(f"Directory '{dir_path}' not found.")

    def create_directory(self, path):
        components = path.split("/")
        dir_name = components[-1]
        dir_path = "/".join(components[:-1])
        dir_dict = self.get_directory_dict(dir_path)
        if dir_dict:
            dir_dict["contents"][dir_name] = {"type": "dir", "contents": {}}
        else:
            print(f"Directory '{dir_path}' not found.")

    def list_directory(self, path):
        dir_dict = self.get_directory_dict(path)
        if dir_dict:
            for name, item in dir_dict["contents"].items():
                print(name)
        else:
            print(f"Directory '{path}' not found.")

    def change_directory(self, path):
        if path.startswith("/"):
            self.current_dir = path
        else:
            new_path = self.current_dir + "/" + path
            if self.get_directory_dict(new_path):
                self.current_dir = new_path
            else:
                print(f"Directory '{new_path}' not found.")

    def get_directory_dict(self, path):
        if path == "":
            return self.file_system[""]
        components = path.split("/")
        current_dir = self.file_system[""]
        for component in components:
            if component:
                if component in current_dir["contents"] and current_dir["contents"][component]["type"] == "dir":
                    current_dir = current_dir["contents"][component]
                else:
                    return None
        return current_dir

fs = FileSystem()

while True:
    command = input(f"\n{fs.current_dir} $ ")

    if command.startswith("touch "):
        file_path = fs.current_dir + "/" + command[6:]
        fs.create_file(file_path)
    elif command.startswith("mkdir "):
        dir_path = fs.current_dir + "/" + command[6:]
        fs.create_directory(dir_path)
    elif command.startswith("ls"):
        fs.list_directory(fs.current_dir)
    elif command.startswith("cd "):
        new_path = command[3:]
        fs.change_directory(new_path)
    elif command == "exit":
        break
    else:
        print("Invalid command. Available commands: touch, mkdir, ls, cd, exit")
