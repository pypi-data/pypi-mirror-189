class ScriptParser:
    @staticmethod
    def parse(path: str) -> str:
        parsed = ""
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            status = []
            status_info = []
            
            curr_str = ""
            charstack = []

            opened_brackets = 0

            command = ""
            for line in lines:
                for char in line:
                    if len(status) == 0:
                        if char == '\t' or char == ' ':
                            charstack.append(char)
                        else: curr_str += char

                        if len(status_info) != 0 and status_info[0] == "cmd":
                            if char == '[': opened_brackets += 1
                            elif char == ']': opened_brackets -= 1
                            
                            if opened_brackets == 0:
                                status_info.pop(0)
                                parsed += command + "\n"
                                command = ""
                            else: command += char

                        if curr_str == 'command':
                            status.append('skip')
                            status_info.append('cmd')
                    elif status[0] == 'skip':
                        status.pop(0)
                        if len(status_info) != 0:
                            if status_info[0] == 'cmd':
                                if char != '[':
                                    status.append('skip')
                                else: 
                                    curr_str = ''
                                    opened_brackets = 1
                                
                                status_info.append('cmd')
                            status_info.pop()
                
                curr_str = ""

        return parsed

    