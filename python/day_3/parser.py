import fabric

def parse(string):
    dirty_id, dirty_rest = string.split('@')
    coordinates, dimensions = dirty_rest.split(':')

    id = dirty_id.strip().replace('#', '')
    x, y = coordinates.strip().split(',')
    width, height = dimensions.strip().split('x')

    return fabric.Claim(id, int(x), int(y), int(height), int(width))
