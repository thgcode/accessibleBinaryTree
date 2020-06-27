# Based from https://www.blog.pythonlibrary.org/2017/05/16/wxpython-learning-about-treectrls/import wx
import wx

class MyTree(wx.TreeCtrl):

    def __init__(self, parent, id, pos, size, style):
         wx.TreeCtrl.__init__(self, parent, id, pos, size, style)

class TreePanel(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        self.tree = MyTree(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                           wx.TR_HAS_BUTTONS | wx.TR_EDIT_LABELS)

        self.root = self.tree.AddRoot('2')
        self._fillLeaves(self.root)
        self._addNumberToTree(1)
        self._addNumberToTree(3)
        self._addNumberToTree(4)
        self.tree.Expand(self.root)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.tree, 0, wx.EXPAND)
        self.SetSizer(sizer)

    def _fillLeaves(self, node):
        self.tree.AppendItem(node, "empty left leaf")
        self.tree.AppendItem(node, "empty right leaf")

    def _isLeaf(self, node):
        return self.tree.GetItemText(node).endswith("leaf")

    def _addNumberToTree(self, number, startingNode=None):
        """Adds a number to the tree and returns the node that was added."""
        if startingNode is None:
            startingNode = self.root
        currentNode = startingNode
        while not self._isLeaf(currentNode):
            nodeNumber = int(self.tree.GetItemText(currentNode))
            left, unusedCookie = self.tree.GetFirstChild(currentNode)
            right, unusedCookie2 = self.tree.GetNextChild(left, unusedCookie)
            if number < nodeNumber:
                currentNode = left
            else:
                currentNode = right
        # Found the node we need to change
        self.tree.SetItemText(currentNode, str(number))
        self._fillLeaves(currentNode)
        return currentNode

class MainFrame(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, parent=None, title="Binary tree")
        panel = TreePanel(self)
        self.Show()

if __name__ == '__main__':
    app = wx.App(redirect=False)
    frame = MainFrame()
    app.MainLoop()
