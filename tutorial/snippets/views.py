# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt

# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser
from rest_framework import status
# from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView


from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
# Create your views here.


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

class SnippetList(APIView):
	"""
 	List all code snippets, or create a new snippet.
 	"""
 	def get(self, request, format=None):
 		
 		snippets = Snippet.objects.all()
 		serializer = SnippetSerializer(snippets, many=True)
 		return Response(serializer.data)

 	def post(self, request, format=None):

 		serializer = SnippetSerializer(data = request.data)
 		if serializer.is_valid():
 			serializer.save()
 			return Response(serializer.data, status=status.HTTP_201_CREATED)
 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SnippetDetails(APIView):
	"""
 	Retreive, update or delete a code snippet.
 	"""
 	def get_objects(self, pk):

 		try:
 			return Snippet.objects.get(pk=pk)
 		except Snippet.DoesNotExist:
 			raise Http404

 	def get(self, request, pk, format=None):

 		snippet = self.get_objects(pk)
 		serializer = SnippetSerializer(snippet)
 		return Response(serializer.data)

 	def put(self, request, pk, format=None):
 		
 		snippet = self.get_objects(pk)
 		serializer = SnippetSerializer(snippet, data = request.data)
 		if serializer.is_valid():
 			serializer.save()
 			return Response(serializer.data)
 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

 	def delete(self, request, pk, format=None):

 		snippet = self.get_objects(pk)
 		snippet.delete()
 		return Response(status=status.HTTP_204_NO_CONTENT)