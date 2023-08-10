class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        simplePath = []
        
        for i in path:
            if i == "" or i == ".":
                continue
            elif i == "..":
                if not simplePath:
                    continue
                else:
                    simplePath.pop()
            else:
                simplePath.append(i)
        return "/" + "/".join(simplePath)
            
        