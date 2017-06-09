# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse, Http404

from rest_framework import status


from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from django.contrib.auth.models import User
# Create your views here.

#===================== API ROOT ENDPOINT ===========================================

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

@api_view(['GET'])
def api_root(request, format=None):

    return Response({
            'users': reverse('user-list', request=request, format=format),
            'snippets': reverse('snippet-list', request=request, format=format)
        })


#======================================== USING FUNCTION BASED VIEWS ===================================
# from django.views.decorators.csrf import csrf_exempt
# from django.http import JsonResponse

# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser
# from rest_framework.decorators import api_view


# @api_view(['GET', 'POST'])
# def snippet_list(request, format=None):
# 	"""
# 	List all code snippets, or create a new snippet.
# 	"""
# 	if request.method == 'GET':
# 		snippets = Snippet.objects.all()
# 		serializer = SnippetSerializer(snippets, many=True)
# 		return Response(serializer.data)

# 	elif request.method == 'POST':
# 		# data = JSONParser().parse(request) # use on when not using Response() but JsonResponse()
# 		serializer = SnippetSerializer(data=request.data)
# 		if serializer.is_vallid():
# 			serializer.save()
# 			return Response(serializer.data, status.HTTP_201_CREATED)
# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT', 'DELETE'])
# def snippet_detail(request, pk, format=None):
# 	"""
# 	Retreive, update or delete a code snippet.
# 	"""
# 	try:
# 		snippet = Snippet.objects.get(pk=pk)
# 	except Snippet.DoesNotExist:
# 		return Response(status=status.HTTP_404_NOT_FOUND)

# 	if request.method == 'GET':
# 		serializer = SnippetSerializer(snippet)
# 		return Response(serializer.data)

# 	elif request.method == 'PUT':
# 		# data = JSONParser().parse(request)
# 		serializer = SnippetSerializer(data=request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data)
# 		return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

# 	elif request.method == 'DELETE':
# 		snippet.delete()
# 		return Response(status=HTTP_204_NO_CONTENT)

#======================================= USING CLASS BASED VIEWS=============================================

# from rest_framework.response import Response
# from rest_framework.views import APIView

# class SnippetList(APIView):
# 	"""
#  	List all code snippets, or create a new snippet.
#  	"""
#  	def get(self, request, format=None):
 		
#  		snippets = Snippet.objects.all()
#  		serializer = SnippetSerializer(snippets, many=True)
#  		return Response(serializer.data)

#  	def post(self, request, format=None):

#  		serializer = SnippetSerializer(data = request.data)
#  		if serializer.is_valid():
#  			serializer.save()
#  			return Response(serializer.data, status=status.HTTP_201_CREATED)
#  		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class SnippetDetails(APIView):
# 	"""
#  	Retreive, update or delete a code snippet.
#  	"""
#  	def get_objects(self, pk):

#  		try:
#  			return Snippet.objects.get(pk=pk)
#  		except Snippet.DoesNotExist:
#  			raise Http404

#  	def get(self, request, pk, format=None):

#  		snippet = self.get_objects(pk)
#  		serializer = SnippetSerializer(snippet)
#  		return Response(serializer.data)

#  	def put(self, request, pk, format=None):
 		
#  		snippet = self.get_objects(pk)
#  		serializer = SnippetSerializer(snippet, data = request.data)
#  		if serializer.is_valid():
#  			serializer.save()
#  			return Response(serializer.data)
#  		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#  	def delete(self, request, pk, format=None):

#  		snippet = self.get_objects(pk)
#  		snippet.delete()
#  		return Response(status=status.HTTP_204_NO_CONTENT)

#================================= USING MIXIN MODELS ================================================

# from rest_framework import mixins
# from rest_framework import generics

# class SnippetList(mixins.ListModelMixin, 
# 					mixins.CreateModelMixin,
# 					generics.GenericAPIView):
	
# 	queryset = Snippet.objects.all()
# 	serializer_class = SnippetSerializer

# 	def get(self, request, *args, **kwargs):
# 		return self.list(request, *args, **kwargs)

# 	def post(self, request, *args, **kwargs):
# 		return self.create(request, *args, **kwargs)

# class SnippetDetails(mixins.RetrieveModelMixin,
# 						mixins.UpdateModelMixin,
# 						mixins.DestroyModelMixin,
# 						generics.GenericAPIView):
	
# 	queryset = Snippet.objects.all()
# 	serializer_class = SnippetSerializer

# 	def get(self, request, *args, **kwargs):
# 		return self.retrieve(request, *args, **kwargs)

# 	def put(self, request, *args, **kwargs):
# 		return self.update(request, *args, **kwargs)

# 	def delete(self, request, *args, **kwargs):
# 		return self.destroy(request, *args, **kwargs)


#============================== USING GENERIC CLASS BASED VIEWS ==========================================

# from django.contrib.auth.models import User

# from rest_framework import generics
# from rest_framework import permissions

# from snippets.serializers import UserSerializer
# from snippets.permissions import IsOwnerOrReadOnly


# class SnippetList(generics.ListCreateAPIView):

#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

#     def perform_create(self, serializer):
#         serializer.save(owner = self.request.user)

# class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):

#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)


# class UserList(generics.ListAPIView):

#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# class UserDetail(generics.RetrieveAPIView):

#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# # endpoints for highlighted snippets

# from rest_framework import renderers
# from rest_framework.response import Response

# class SnippetHighlight(generics.GenericAPIView):

#     queryset = Snippet.objects.all()
#     renderer_classes = (renderers.StaticHTMLRenderer,)

#     def get(self, request, *args, **kwargs):

#         snippet = self.get_object()
#         return Response(snippet.highlighted)

#================================= USING VIEWSETS ===========================================

from rest_framework import viewsets 
from rest_framework import renderers
from rest_framework.decorators import detail_route
from rest_framework import permissions

from snippets.serializers import UserSerializer
from snippets.permissions import IsOwnerOrReadOnly

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class SnippetViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):

        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)