from __future__ import print_function

# no standard tests in this file, ignore
__test__ = False

if __name__ == '__main__':
    import MySQLdb as m
    from eventlet import patcher
    from eventlet.green import MySQLdb as gm
    patcher.monkey_patch(all=True, MySQLdb=True)
    patched_set = set(patcher.already_patched) - set(['psycopg'])
    assert patched_set == frozenset(['MySQLdb', 'os', 'select', 'socket', 'thread', 'time'])
    assert m.connect == gm.connect
    print('pass')
