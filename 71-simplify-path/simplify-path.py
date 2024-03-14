import re

class Solution:
    def simplifyPath(self, path: str) -> str:
        path = re.sub(r"\/+$", "", re.sub(r"\/+", "/", re.sub(r"(?<=\/)\.\/", "/", path)))
        # print(f"{path = }")
        pathSplit = path.split("/")
        pathSplit1 = path.split("/")
        i = len(pathSplit) - 1
        count = 0
        while i >= 0:
            if pathSplit[i] == ".":
                del pathSplit1[i]
            if pathSplit[i] == "..":
                # print(f"{pathSplit1 = }")
                count += 1
                while i > 0:
                    i -= 1
                    if pathSplit[i] == "..":
                        count += 1
                    else:
                        i += 1
                        break
                from_, to = i+count-1, i-count-1
                for k in range(from_, i-1, -1):
                    if 0 <= k < len(pathSplit1):
                        # print(f"from {pathSplit1[k] = }")
                        pathSplit1[k] = ""
                for k in range(i-1, -1, -1):
                    if count > 0 and pathSplit1[k] != ".." and pathSplit1[k] != "":
                        count -= 1
                        # print(f"to {pathSplit1[k] = }, {count = }")
                        pathSplit1[k] = ""
            i -= 1
            
        path = re.sub(r"\/+", "/", "/" + re.sub(r"\/+$", "", "/".join(pathSplit1)))
        return path