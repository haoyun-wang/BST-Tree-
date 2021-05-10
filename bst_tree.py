import copy
from typing import Optional, Callable, TypeVar, Generic

from Trees.src.errors import MissingValueError, EmptyTreeError
from Trees.src.nodes.bst_node import BSTNode

T = TypeVar('T')
K = TypeVar('K')


class BST(Generic[T, K]):
    """
    T: The value stored in the node
    K: The value used in comparing nodes
    """

    def __init__(self, root: Optional[BSTNode[T]] = None, key: Callable[[T], K] = lambda x: x) -> None:
       
        self.root = root
        ...

    @property
    def height(self) -> int:
        
        if self.root is None:
            return -1
        else:
            return self._height(self.root,-1)
    def _height(self,cur_node,len):
        if cur_node==None:
            return len
        rightPath=self._height(cur_node.right,len+1)
        leftPath=self._height(cur_node.left,len+1)
        return max(rightPath,leftPath)


    def __len__(self) -> int:
       
        if self.root is None:
           return False
        else:
            return self.count(self.root)

    def count(self, cur_node):

        if cur_node == None: return 0
        return 1+self.count(cur_node.right)+self.count(cur_node.left,)






    def add_value(self, value: T) -> None:
        
        if self.root == None:

            self.root = BSTNode(value)

        else:

            self.insert(value, self.root)

    def insert(self,value,cur_node):
        if value < cur_node.value:

            if cur_node.left == None:

                cur_node.left = BSTNode(value)

                cur_node.left.parent = cur_node

            else:

                self.insert(value, cur_node.left)

        elif value >= cur_node.value:

            if cur_node.right == None:

                cur_node.right = BSTNode(value)

                cur_node.right.parent = cur_node

            else:

                self.insert(value, cur_node.right)






    def get_node(self, value: K) -> BSTNode[T]:
      



        if self.root == None:

            raise MissingValueError

        else:

            return self._get_node(value, self.root)

    def _get_node(self, value, cur_node):

        if value == cur_node.value:
            if cur_node.right !=None:


                if cur_node.right.value==value:
                    return self._get_node(value, cur_node.right)




            return cur_node




        elif value < cur_node.value and cur_node.left != None:

                return self._get_node(value, cur_node.left)

        elif value > cur_node.value and cur_node.right != None:

                return self._get_node(value, cur_node.right)
        else:

            raise MissingValueError

    def get_max_node(self) -> BSTNode[T]:
       
        if self.root is None:
            raise EmptyTreeError

        current = self.root

        while current.right != None:
            current = current.right

        return current

    def get_min_node(self) -> BSTNode[T]:
       
        if self.root is None:
            raise EmptyTreeError
        current = self.root

        while current.left != None:
            current = current.left

        return current


    def remove_value(self, value: K) -> None:
       
        if  value == None:


             raise MissingValueError

        node=self.get_node(value)
        self._remove_value(node)


    def _remove_value(self,node:T):







        def num_children(n):

            num_children = 0

            if n.left != None: num_children += 1

            if n.right!= None: num_children += 1

            return num_children



        node_parent = node.parent




        def min_value_node(n:T)-> BSTNode[T]:
            current = n
            while current.right != None:
                  current = current.right
            return current




        node_children = num_children(node)

        if node_children == 0:


            if node_parent != None:



                if node_parent.left == node:

                    node_parent.left = None

                else:

                    node_parent.right= None

            else:

                self.root = None



        if node_children == 1:



            if node.left != None:

                child = node.left

            else:

                child = node.right



            if node_parent != None:



                if node_parent.left == node:

                    node_parent.left = child

                else:

                    node_parent.right = child

            else:

                self.root = child



            child.parent = node_parent



        if node_children == 2:


            successor = min_value_node(node.left)



            node.value = successor.value



            self._remove_value(successor)

    def __eq__(self, other: object) -> bool:
        if self is other:
            return True
        elif isinstance(other, BST):
            if len(self) == 0 and len(other) == 0:
                return True
            else:
                return len(self) == len(other) and self.root.value == other.root.value and \
                       BST(self.root.left) == BST(other.root.left) and \
                       BST(self.root.right) == BST(other.root.right)
        else:
            return False

    def __ne__(self, other: object) -> bool:
        return not (self == other)

    def __deepcopy__(self, memodict) -> "BST[T,K]":
        
        new_root = copy.deepcopy(self.root, memodict)
        new_key = copy.deepcopy(self.key, memodict)
        return BST(new_root, new_key)
