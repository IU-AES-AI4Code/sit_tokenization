from treelib import Tree

def traverse_tree(tree):
    cursor = tree.walk()

    reached_root = False
    while reached_root == False:
        yield cursor.node

        if cursor.goto_first_child():
            continue

        if cursor.goto_next_sibling():
            continue

        retracing = True
        while retracing:
            if not cursor.goto_parent():
                retracing = False
                reached_root = True

            if cursor.goto_next_sibling():
                retracing = False

def visualize_ast(cs_tree):
    tree = Tree()
    for node in traverse_tree(cs_tree):
        #node_name = node.type
        node_name = str(node)
        node_id = node.id
        if node.parent == None:
            tree.create_node(node_name, node_id)
        else:
            parent_id = node.parent.id
            tree.create_node(node_name, node_id, parent=parent_id)
    tree.show()