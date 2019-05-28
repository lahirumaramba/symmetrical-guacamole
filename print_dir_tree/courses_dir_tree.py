input = [
	{"id": 1, "name": "US History", "parent_id": None},
	{"id": 2, "name": "Third Assignment", "parent_id": 3},
	{"id": 3, "name": "First Chapter", "parent_id": 1},
	{"id": 4, "name": "Second Assignment", "parent_id": 1},
	{"id": 5, "name": "First Assignment", "parent_id": 6},
	{"id": 6, "name": "Canadian History", "parent_id": None},
]

"""
Expected Output:
US History
-First Chapter
--Third Assignment
-Second Assignment
Canadian History
-First Assignment
"""

"""
Dictionary:
{parent_id: [Array of Nodes]}
None -> [node1, node6]
3 -> [node2]
1 -> [node3, node4]
6 -> [node5]
"""

# Iterative Solution
# time: O(N)
# space: O(N)
def print_materials_iterative(materials_list):
	dict = {}

	for item in materials_list:
		parent_id = item['parent_id']

		if parent_id in dict:
			dict[parent_id].append(item)
			continue

		dict[parent_id] = [item]

	nodes = dict[None]
	levels = [0] * len(nodes)

	while nodes:
		node = nodes.pop(0)
		level = levels.pop()

		print('{}{}'.format('-'*level, node['name']))

		if node['id'] in dict:
			new_nodes = dict[node['id']]
			levels += [level+1] * len(new_nodes)
			nodes = dict[node['id']] + nodes


# Recursive Solution
# time: O(N)
# space: O(N) <- recursive stack + dict of len N
def print_materials_recursive(materials_list):
	dict = {}

	for item in materials_list:
		parent_id = item['parent_id']

		if parent_id in dict:
			dict[parent_id].append(item)
			continue

		dict[parent_id] = [item]

	print_in_order(dict, dict[None], 0)

def print_in_order(dict, nodes, level):
	if nodes is None:
		return

	for node in nodes:
		print('{}{}'.format('-'*level, node['name']))
		print_in_order(dict, dict.get(node['id']), level+1)


#Driver Code

print("----------- iterative: -----------")
print_materials_iterative(input)
print("----------- recursive: -----------")
print_materials_recursive(input)


"""
Output:

----------- iterative: -----------
US History
-First Chapter
--Third Assignment
-Second Assignment
Canadian History
-First Assignment
----------- recursive: -----------
US History
-First Chapter
--Third Assignment
-Second Assignment
Canadian History
-First Assignment

[Finished in 0.06s]
"""
