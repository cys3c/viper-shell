import ConfigParser, os

def config():
    cfg = ConfigParser.ConfigParser()
    for f in ('teamserver-viper.cfg', '/etc/teamserver-viper/teamserver-viper.cfg', '/etc/teamserver-viper.cfg'):
        if os.path.exists(f):
            cfg.read(f)
            return cfg
    return None