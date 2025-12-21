class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:

        d = defaultdict(list)

        def parse_contents(path):
            arr = path.split(" ")
            base_path = arr[0]
            file_names = arr[1:]
            for file_name in file_names:
                a, b = file_name.index("("), file_name.index(")")
                name, content = file_name[:a], file_name[a + 1 : b]
                d[content].append(base_path + "/" + name)

        for path in paths:
            parse_contents(path)

        res = [value for value in d.values() if len(value) >= 2]
        return res
