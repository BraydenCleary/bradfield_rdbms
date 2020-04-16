import pytest
from query_planner import QueryPlanner
from query_executor import QueryExecutor
from filescan import Filescan
from projection import Projection
from selection import Selection
from limit import Limit
from .sample_queries import select_movieId_limit_10
from .sample_queries import average_medium_cool_rating
from .mock_iterator import MockIterator

class TestRdbms:
    def test_filescan_iterator(self):
        node = Filescan(lambda: 'movies')
        assert node.current_row == 0
        assert node.next() == {'movieId': '1', 'title': 'Toy Story (1995)', 'genres': 'Adventure|Animation|Children|Comedy|Fantasy'}
        assert node.current_row == 1
        assert node.next() == {'movieId': '2', 'title': 'Jumanji (1995)', 'genres': 'Adventure|Children|Fantasy'}

    def test_projection_iterator(self):
        node = Projection(lambda: ['title'])
        node.children = [MockIterator([{'title': 'Best Movie Ever'}])]
        assert node.next() == {'title': 'Best Movie Ever'}
        assert node.next() == None

    def test_selection_iterator(self):
        node = Selection(lambda r: r['title'] == 'Mission Impossible')
        node.children = [MockIterator([{'title': 'Good Will Hunting'}, {'title': 'Mission Impossible'}, {'title': 'Happy Gilmore'}])]
        assert node.next() == {'title': 'Mission Impossible'}
        assert node.next() == None

    def test_limit_iterator(self):
        node = Limit(lambda: 2)
        node.children = [MockIterator([{'movieId': '1'}, {'movieId': '2'}, {'movieId': '3'}])]
        assert node.next() == {'movieId': '1'}
        assert node.next() == {'movieId': '2'}
        assert node.next() == None

    def test_select_movieId_limit_10(self):
        planner = QueryPlanner(select_movieId_limit_10())
        executor = QueryExecutor(planner.get_root())
        result = executor.get_result()
        assert result == [{'movieId': '1'}, {'movieId': '2'}, {'movieId': '3'}, {'movieId': '4'}, {'movieId': '5'}, {'movieId': '6'}, {'movieId': '7'}, {'movieId': '8'}, {'movieId': '9'}, {'movieId': '10'}]
