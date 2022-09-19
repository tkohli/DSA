class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_hash = defaultdict(list)
        for path in paths:
            files_c = path.split()
            prefix = files_c[0]
            for f_c in files_c[1:]:
                filename, content = f_c.split('(')
                content_hash[content].append(f'{prefix}/{filename}')

        res = []
        for files in content_hash.values():
            if len(files) > 1:
                res.append(files)

        return res
