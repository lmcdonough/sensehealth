
class CustomViewSet(object):

	@staticmethod
	def register(viewset, viewset_type):

		return viewset.as_view(viewset_type)



class ViewSetType(object):

	GENERIC_LIST = {'get': 'list', 'post': 'create'}
	GENERIC_DETAIL = {'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}
	READ_ONLY_LIST = {'get': 'list'}
	READ_ONLY_DETAIL = {'get': 'retrieve'}


