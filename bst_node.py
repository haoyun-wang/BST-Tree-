import copy
from typing import Generic, Iterable, TypeVar, Optional

T = TypeVar('T')


class BSTNode(Generic[T]):
   
    def __init__(self, value: T, children: Optional[Iterable["BSTNode[T]"]] = None,
                 parent: Optional["BSTNode[T]"] = None) -> None:
        
        self.value=value
        self.right=None
        self.left=None
        self.parent=parent
        self.children=children

    def has_no_children(self):
        if (self.left and self.right) is None:
            return True
        return False


    def __iter__(self) -> Iterable["BSTNode[T]"]:


        if self.left is not None:
            yield self.left
        if self.right is not None:
            yield self.right

    def __deepcopy__(self, memodict) -> "BSTNode[T]":
       
        copy_node = BSTNode(copy.deepcopy(self.value, memodict))
        copy_node.left = copy.deepcopy(self.left, memodict)
        copy_node.right = copy.deepcopy(self.right, memodict)
        return copy_node
