import clouddns
import gflags
import wnyc_dns.common

FLAGS = gflags.FLAGS

gflags.DEFINE_string('username',
                     None,
                     'Your rackspace username')
gflags.DEFINE_string('apikey', 
                     None,
                     'Your rackspace API key')

def connection():
    return clouddns.connection.Connection(FLAGS.username, FLAGS.apikey)

def update_ip_addresses(old_type, old_data, new_type, new_data, *excludes):
    dns = connection()
    for domain in dns.get_domains():
        for record in domain.get_records():
                    
            if (record.type, record.data) == (old_type, old_data):
                for exclude in excludes:
                    if record.name.startswith(exclude):
                        continue
                if FLAGS.live:
                    print "Changing", 
                    record.update(type=new_type, data=new_data)
                else:
                    print "Would have changed", 
                print domain.name, record.name, "from", old_type, old_data, "to", new_type, new_data

COMMANDS = {'update_ip_addresses': update_ip_addresses}

def main(argv=None, stdin=None, stdout=None, stderr=None):
    import sys
    argv = argv or sys.argv
    stdin = stdin or sys.stdin
    stdout = stdout or sys.stdout
    stderr = stderr or sys.stderr

    try:
        argv = FLAGS(argv)[1:]
        if  argv[0] not in COMMANDS:
            stderr.write("\\nUsage: %s update_id_addresses\\n%s\n" %
                         (sys.argv[0], FLAGS))
            return 1
    except gflags.FlagsError, e:
        stderr.write("%s\\nUsage: %s update_id_addresses\\n%s\n" %
                     (e, sys.argv[0], FLAGS))
        return 1
    
    COMMANDS[argv[0]](*argv[1:])
    
