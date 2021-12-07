class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_Child(self, child):
        child.parent = self
        self.children.append(child)
    
    def getLevel(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def printtree(self):
        spaces = ' ' * self.getLevel() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        for child in self.children:
            child.printtree()

def build_product_tree():
    Branch1Level2 = TreeNode("Vishwa (Infrastructure Head")
    Branch1Level2.add_Child(TreeNode("Dhaval (CLoud Manager"))

    Branch1Level1 = TreeNode("Chinmay (CTO)")
    Branch1Level1.add_Child(Branch1Level2)
    Branch1Level1.add_Child(TreeNode("Aamir (Application Head)"))

    Branch2Level1 = TreeNode("Gels (HR Head)")
    Branch2Level1.add_Child(TreeNode("Peter (Recruitment Manager)"))
    Branch2Level1.add_Child(TreeNode("Waqas (Poilcy Manager)"))

    root = TreeNode("Nilupul (CEO)") 
    root.add_Child(Branch1Level1)
    root.add_Child(Branch2Level1)

    root.printtree()

if __name__ == '__main__':
    root = build_product_tree()