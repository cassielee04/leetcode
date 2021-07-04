class Solution():
    def __init__(self):
        self.answer = 0
        
    def dfs(self, emp, man, depth, tree):
        if emp == man:
            self.answer = depth
            return 
        if man in tree:
            for n_emp in tree[man]:
                depth = depth + 1
                self.dfs(emp, n_emp, depth, tree)
                depth = depth - 1
        

    def codingteset1(self, hierachy):
        tree = {}
        depth = int()
        
        target_emp = hierachy[0].split('/')[0]
        target_man = hierachy[0].split('/')[1] 
        
        for item in hierachy[1:]:
            employee = item.split('/')[0]
            manager = item.split('/')[1]
            if manager not in tree:
                tree[manager] = [employee]
            else:
                tree[manager].append(employee)
        print(tree)
        self.dfs(target_emp, target_man, depth, tree)
        # print(depth)
        return self.answer


sol = Solution()
# Test1
hierachy = ["Susan/Amy", "Susan/John", "John/Amy"]
print("================")
print("Test1\n")
print(sol.codingteset1(hierachy))
# print(f"Answer : {sol.codingteset1(hierachy)}")
print("================")

sol = Solution()
hierachy = ["Scott/David","Terry/David","Kyle/David", "Ben/Kyle","Scott/Jon","Chris/Scott","Jon/Kenny","Kenny/David","David/Mike"]
print("================")
print("Test2\n")
print(sol.codingteset1(hierachy))
print("================")

sol = Solution()
hierachy = ["Ben/Jon","Terry/David","Kyle/David","Ben/Kyle","Scott/Jon","Chris/Scott","Jon/Kenny","Kenny/David"]
print("================")
print("Test3\n")
print(sol.codingteset1(hierachy))

sol = Solution()
hierachy = ["Christy/Susan","Aimee/Melissa","Melissa/Susan",
"Stacy/Corinne","Gabrielle/Melissa","Corinne/Melissa",
"Christy/Stacy","Pat/Christy"]
print("================")
print("Test4\n")
print(sol.codingteset1(hierachy))
print("================")