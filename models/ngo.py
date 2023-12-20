from flask.json import JSONEncoder

class NGO(object):
    new_id = 1
    def __init__(self, name, founder, sector):
        self.name = name
        self.founder = founder
        self.sector = sector
        self.id = NGO.new_id
        NGO.new_id += 1

class NGOEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, NGO):
            return obj.__dict__
        return super(NGOEncoder, self).default(obj)