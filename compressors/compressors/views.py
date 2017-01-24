from pyramid.view import view_config
from LZCompressor import RLE

@view_config(route_name='rle', renderer='json')
def get_rle(request):
    characters = request.matchdict['characters']
    return {'encoded': RLE().encode(characters)}
