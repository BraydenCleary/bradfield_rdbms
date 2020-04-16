def select_movieId_limit_10():
    return {
        'name': 'Limit',
        'lambda': lambda: 10,
        'children': [
            {
                'name': 'Projection',
                'lambda': lambda: ['movieId'],
                'children': [
                    {
                        'name': 'Filescan',
                        'lambda': lambda: 'movies',
                        'children': []
                    }
                ]
            }
        ]
    
    }

def average_medium_cool_rating():
    return {
        'name': 'Average',
        'lambda': lambda r: r['ratings.rating'],
        'children': [
            {
                'name': 'Projection',
                'lambda': lambda r: r['ratings.rating'],
                'children': [
                    {
                        'name': 'NestedLoopsJoin',
                        'lambda': lambda r, s: r['id'] == s['movie_id'],
                        'children': [
                            {
                                'name': 'Selection',
                                'lambda': lambda r: r.name == 'Medium Cool (1969)',
                                'children': [
                                    {
                                        'name': 'Filescan',
                                        'lambda': lambda _: 'movies',
                                        'children': []
                                    }
                                ]
                            },
                            {
                                'name': 'Filescan',
                                'lambda': lambda _: 'ratings',
                                'children': []
                            }
                        ]
                    }
                ]
            }
        ]
    }
