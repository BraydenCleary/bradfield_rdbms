def select_movies_limit_10():
  return {
    'name': 'LIMIT',
    'lambda': lambda : 10,
    'children': [
      {
        'name': 'FILESCAN',
        'lambda': lambda _: 'movies',
        'children': []
      }
    ]
  }

def average_medium_cool_rating():
  return {
    'name': 'AVERAGE',
    'lambda': lambda r: r['ratings.rating'],
    'children': [
      {
        'name': 'PROJECTION',
        'lambda': lambda r: r['ratings.rating'],
        'children': [
          {
            'name': 'NESTED_LOOPS_JOIN',
            'lambda': lambda r, s: r['id'] == s['movie_id'],
            'children': [
              {
                'name': 'SELECTION',
                'lambda': lambda r: r.name == 'Medium Cool (1969)',
                'children': [
                  {
                    'name': 'FILESCAN',
                    'lambda': lambda _: 'movies',
                    'children': []
                  }
                ]
              },
              {
                'name': 'FILESCAN',
                'lambda': lambda _: 'ratings',
                'children': []
              }
            ]
          }
        ]
      }
    ]
  }
