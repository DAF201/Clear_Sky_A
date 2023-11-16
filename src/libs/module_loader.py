MODULES = [

    {'id': 'test',
     'protocol': {
         'head': b'<test>.*<test>',
         'ver': b'<test_ver>.*<test_ver>',
                'data': b'<test_data>.*<test_data>'
     },
     'path': r'external_modules\\test\\',
     'host': '127.0.0.1',
     'port': 919
     },

    {'id': 'bloom_in',
     'protocol':
     {'head': b'<bloom_in>.*<bloom_in>',
      'ver': b'<bloom_in_ver>.*<bloom_in_ver>',
             'is_command': b'<bloom_in_command>',
             'data': b'<bloom_in_data>.*<bloom_in_data>'},
     'path': r'external_modules\\bloom_in_v0.03\\',
     'host': '127.0.0.1',
     'port': 921
     }
]
