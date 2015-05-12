import numpy


class Importer(object):

    def import_data(filename):

        filelines = Importer._read_file(filename)
        info, breaklines = Importer._read_info(filelines)
        node_coordinates_list, demand_list = Importer._return_nodes_and_delivery_lists(info, breaklines)
        adjacency_matrix_list = Importer._create_adjacency_matrix(node_coordinates_list)

        adjacency_matrix_array = numpy.array(adjacency_matrix_list)
        demand_array = numpy.array(demand_list)
        return adjacency_matrix_array, demand_array

    def _read_file(my_filename):
        filelines = []
        with open(my_filename, "rt") as f:
            filelines = f.readlines()
        return filelines

    def _read_info(my_filelines):

        info = {}
        start = 0
        middle = 0
        end = 0

        for i, line in enumerate(my_filelines):
            if line.startswith("NODE_COORD_SECTION"):
                start = i
            elif line.startswith("DEMAND_SECTION"):
                middle = i
            elif line.startswith("DEPOT_SECTION"):
                end = i
            elif line.split(' ')[0].isupper():  # checks if line begins with UPPERCASE key
                splited = line.split(':')
                info[splited[0].strip()] = splited[1].strip()

        return info, (start, middle, end)

    def _return_nodes_and_delivery_lists(my_filelines, my_breaklines):
        start, middle, end = my_breaklines
        node_coordinates_list = []
        demand_list = []

        for i, line in enumerate(my_filelines):
            if start < i < middle:
                splited = line.split(' ').strip()
                splited = map(float(), splited)
                node_coordinates_list.append((splited[1], splited[2]))

            if middle < i < end:
                splited = line.split(' ').strip()
                splited = map(int(), splited)
                demand_list.append(splited[1])

        return (node_coordinates_list, demand_list)

    def _create_adjacency_matrix(my_node_coordinates_list):
        ncl = my_node_coordinates_list
        for node in ncl:
            pass

    def _euclidian_distance(my_node1, my_node2):
        x1, y1 = my_node1
        x2, y2 = my_node2

        distance = ((x1-x2)**2 + (y1-y2)**2) ** 0.5
        return distance

class Drawer(object):
    pass
