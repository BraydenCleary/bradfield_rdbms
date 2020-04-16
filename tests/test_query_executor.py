import pytest
from query_planner import QueryPlanner
from filescan import Filescan
from projection import Projection
from selection import Selection
from .sample_queries import select_movies_limit_10
from .sample_queries import average_medium_cool_rating
from .mock_iterator import MockIterator

class TestRdbms:
    def test_filescan_iterator(self):
        node = Filescan(lambda: 'movies', 0)
        assert node.current_row == 0
        assert node.next() == {'movieId': '1', 'title': 'Toy Story (1995)', 'genres': 'Adventure|Animation|Children|Comedy|Fantasy'}
        assert node.current_row == 1

    def test_projection_iterator(self):
        node = Projection(lambda: ['title'], 0)
        node.children = [MockIterator([{'title': 'Best Movie Ever'}])]
        assert node.next() == {'title': 'Best Movie Ever'}

    def test_selection_iterator(self):
        node = Selection(lambda r: r['title'] == 'Mission Impossible', 0)
        node.children = [MockIterator([{'title': 'Good Will Hunting'}, {'title': 'Mission Impossible'}, {'title': 'Happy Gilmore'}])]
        assert node.next() == {'title': 'Mission Impossible'}
        assert node.next() == None

