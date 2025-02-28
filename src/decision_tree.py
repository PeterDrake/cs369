import math

ATTRIBUTES = ('Alternative', 'Bar', 'Friday/Saturday', 'Hungry', 'Patrons', 'Price', 'Raining',
              'Reservation', 'Type', 'Wait')


class Datum:
    def __init__(self, target, *values):
        self.target = target
        self.attributes = dict(zip(ATTRIBUTES, values))


data = (Datum(True, True, False, False, True, 'Some', '$$$', False, True, 'French', '0-10'),
        Datum(False, True, False, False, True, 'Full', '$', False, False, 'Thai', '30-60'),
        Datum(True, False, True, False, False, 'Some', '$', False, False, 'Burger', '0-10'),
        Datum(True, True, False, True, True, 'Full', '$', True, False, 'Thai', '10-30'),
        Datum(False, True, False, True, False, 'Full', '$$$', False, True, 'French', '>60'),
        Datum(True, False, True, False, True, 'Some', '$$', True, True, 'Italian', '0-10'),
        Datum(False, False, True, False, False, 'None', '$', True, False, 'Burger', '0-10'),
        Datum(True, False, False, False, True, 'Some', '$$', True, True, 'Thai', '0-10'),
        Datum(False, False, True, True, False, 'Full', '$', True, False, 'Burger', '>60'),
        Datum(False, True, True, True, True, 'Full', '$$$', False, True, 'Italian', '10-30'),
        Datum(False, False, False, False, False, 'None', '$', False, False, 'Thai', '0-10'),
        Datum(True, True, True, True, True, 'Full', '$', False, False, 'Burger', '30-60'))


def impurity(data):
    """
    :param data: A sequence of Datum objects.
    :return: The Gini impurity of the data, as per equation 6.1 on p. 197 of Géron.
    """
    # TODO You have to write this


def split_cost(data, attribute, value):
    """
    :param data: A sequence of Datum objects.
    :param attribute: An attribute on which to split.
    :param value: The value to distinguish from other values at this node.
    :return: The cost of splitting in this way, as per equation 6.2 on p. 200 of Géron.
    """
    # TODO You have to write this


def best_split(data):
    """
    :param data: A sequence of Datum objects.
    :return: The best attribute and value to split on at this node.
    """
    # TODO You have to write this
    # Hint: Return two values


class Tree:
    def __init__(self, data):
        # TODO You have to wrie this to build the tree from data
        # Hint: It's recursive, because you may be building subtrees

    def __repr__(self, indent=''):
        # TODO You have to write this
        # Hint: It's recursive. A recursive call might be something like:
        # self.left.__repr__(indent + '  ')

    def predict(self, datum):
        """
        :param datum: A Datum object.
        :return: The tree's prediction for the attribute values of datum.
        """
        # TODO You have to write this
        # Hint: You guessed it, recursive!


def main():
    tree = Tree(data)
    print(tree)


if __name__ == '__main__':
    main()
