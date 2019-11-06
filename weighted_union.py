import itertools
import time

class WeightedUnion:
    """Contains unions and can add items to union or check connectivity"""

    def __init__(self, number=0):
        self.__components = list(range(number))
        # init sizes of component trees by ones
        # (each tree has one object on start)
        self.__sizes = list(itertools.repeat(1, number))

    def union(self, _p: int, _q: int):
        """Creates union between _p and _q.
        components[i] is a parent of i
        Parent of each component will be a root,
        because of path compression"""

        p_root = self.find_root(_p)
        # print("finded p_root")
        q_root = self.find_root(_q)
        # print("finded q_root")
        # set parent to the smallest tree
        # parent of each node in the union will be a root node
        # that named path compression

        if self.__sizes[p_root] > self.__sizes[q_root]:
            self.__components[q_root] = p_root
            # print("assigned q_root")
            # in case, if there were more than one node in the old union,
            # assign new root to the nodes in old union
            self.__sizes[p_root] += self.__sizes[q_root]
            # print("assigned size of p_root")

        else:
            self.__components[p_root] = q_root
            # print("assigned p_root")
            self.__sizes[q_root] += self.__sizes[p_root]
            # print("assigned size of q_root")

    def find_root(self, _p: int) -> int:
        """Finds a root of _p and returns it.
        Find root is equal to find recursively parent of i,
        which doesn't have a parent"""
        # creating a short-named reference to our __components
        # in order to decrease amount of code
        comp = self.__components

        while _p != comp[_p]:
            """Compressing path to the root by flatting tree of nodes.
            In ideal case (when all nodes are in one union),
            all nodes will have one parent - root"""
            comp[_p] = comp[comp[_p]]
            _p = comp[_p]
        return _p

    def print_list(self):
        """Prints components list without formatting"""

        print(self.__components)

    def connected(self, _p: int, _q: int) -> bool:
        """Checks, whether _p and _q are in one union or not"""
        if self.find_root(_p) == self.find_root(_q):
            return True
        return False

    def all_connected(self) -> bool:
        """Checks, whether all nodes are connected"""
        first = self.__components[0]
        for node in self.__components:
            if node != first:
                return False
        return True


def input_from_file(filename: str) -> [str]:
    """Reads given file and initialize components list"""

    file_object = open(filename, "r")
    lines = str(file_object.read())
    file_object.close()

    lines = lines.split('\n')
    # print(lines)
    # extracting length of file
    # that is always on first line of the file
    comp_length = int(lines[0])
    lines = [line.split(' ') for line in lines[1:]]
    # filtering blank lines
    lines = [line for line in lines if line != ['']]
    return (comp_length, lines)


def main():
    """Example of using QuickUnion"""

    comp_len, lines = input_from_file("input.txt")
    # print (lines)

    time1 = time.perf_counter_ns()

    _wu = WeightedUnion(comp_len)

    for line in lines:
        _wu.union(int(line[0]), int(line[1]))
        # _wu.print_list()

    time2 = time.perf_counter_ns() - time1
    print(time2, "ns")

    _wu.print_list()


if __name__ == "__main__":
    main()
