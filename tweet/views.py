from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import AllowAny
import xml.etree.ElementTree as ET
import albumentations as A
import cv2
from .serializers import ImageUploadSerializer
from django.http import HttpResponse, Http404, JsonResponse
import numpy as np
from rest_framework.parsers import MultiPartParser, FormParser
# from .models import Tweet
# from django.conf import settings
# from rest_framework.response import Response
# from rest_framework.decorators import api_view, permission_classes, authentication_classes
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.authentication import SessionAuthentication
# from .serializers import TweetSerializer, TweetActionSerializer, TweetCreateSerializer
# # Create your views here.


class AugmentImageView(APIView):
    permission_classes = [AllowAny]
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request):
        if request.FILES:
            data = {}
            xmlfile = request.FILES['file']
            data['image_name'] = 'image'
            # data['object_name'] = request.FILES['file']
            data['object_name'] = 'file'
            # image = cv2.imdecode(np.fromstring(
            #     request.data['image'], np.uint8), cv2.IMREAD_COLOR)
            # img = Image.open(request.files['file'])
            # npimg = np.fromfile(request.data['image'], np.uint8)
            nparr = np.fromstring(request.data['image'], np.uint8)
            image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
            # image = cv2.imread(request.FILES['image'])
            # image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            mytree = ET.parse(xmlfile)
            myroot = mytree.getroot()
            width = myroot.find('size').find('width').text
            height = myroot.find('size').find('height').text
            bboxes = []
            for x in myroot.findall('object'):
                item = x.find('bndbox')
                coord = [item.find('xmin').text, item.find(
                    'ymin').text, item.find('xmax').text, item.find('ymax').text, 'dog']
                # coord = [int(item.find('xmin').text)/int(width), int(item.find(
                #     'ymin').text)/int(height), int(item.find('xmax').text)/int(width), int(item.find('ymax').text)/int(height)]
                data['x_min'] = item.find('xmin').text
                data['y_min'] = item.find('ymin').text
                data['x_max'] = item.find('xmax').text
                data['y_max'] = item.find('ymax').text
                bboxes.append(coord)

            transform = A.Compose([
                A.RandomCrop(width=width, height=height),
            ], bbox_params=A.BboxParams(format='pascal_voc'))
            # ])
            transformed = transform(image=np.array(image), bboxes=bboxes)
            transformed_image = transformed['image']
            data['image_path'] = transformed_image
            data['xml_path'] = xmlfile
            image_upload = ImageUploadSerializer(data=data)
            if image_upload.is_valid():
                image_upload.save()
                return JsonResponse({'message': 'Image Augmented Successfully', 'status_code': 200, 'status': True, 'data': image_upload}, status=200)
            return JsonResponse({'message': image_upload.errors, 'status_code': 400}, status=200)
        return JsonResponse({'message': 'Error', 'status_code': 400}, status=200)


# class CustomUserCreate(APIView):
#     permission_classes = [AllowAny]

#     def post(self, request):
#         reg_serializer = RegisterUserSerializer(data=request.data)
#         if reg_serializer.is_valid():
#             newuser = reg_serializer.save()
#             if newuser:
#                 return Response(status=status.HTTP_201_CREATED)
#         return Response(reg_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# def home_view(request, *args, **kwargs):
#     return render(request, 'pages/home.html', context={}, status=200)
#     # return HttpResponse('<h1>Hello World</h1>')


# # def tweet_list_view(request, *args, **kwargs):
# #     '''
# #     REST API VIEW
# #     Consume by javascript or Swift/java.ios.android
# #     return json data
# #     '''
# #     qs = Tweet.objects.all()
# #     tweet_list = [{'id': x.id, 'content': x.content} for x in qs]
# #     data = {
# #         'isUser': False,
# #         'response': tweet_list}
# #     return JsonResponse(data)


# @api_view(['POST'])
# # @authentication_classes([SessionAuthentication])
# @permission_classes([IsAuthenticated])
# def tweet_create_view(request, *args, **kwargs):
#     serializer = TweetCreateSerializer(data=request.POST or None)
#     if serializer.is_valid(raise_exception=True):
#         obj = serializer.save(user=request.user)
#         return Response(serializer.data, status=201)
#     return Response({}, status=400)


# @api_view(['GET'])
# def tweet_list_view(request, *args, **kwargs):

#     qs = Tweet.objects.all()
#     serializer = TweetSerializer(qs, many=True)
#     return Response(serializer.data, status=200)


# @api_view(['GET'])
# def tweet_detail_view(request, tweet_id, *args, **kwargs):
#     qs = Tweet.objects.filter(id=tweet_id)
#     if not qs.exists():
#         return Response({}, status=404)
#     obj = qs.first()
#     serializer = TweetSerializer(qs, many=True)
#     return Response(serializer.data)


# @api_view(['DELETE', 'POST'])
# @permission_classes([IsAuthenticated])
# def tweet_delete_view(request, tweet_id, *args, **kwargs):
#     qs = Tweet.objects.filter(id=tweet_id)
#     if not qs.exists():
#         return Response({}, status=404)
#     qs = qs.filter(user=request.user)
#     if not qs.exists():
#         return Response({'message': 'You cannot delete this tweet'}, status=404)
#     obj = qs.first()
#     obj.delete()
#     return Response({'message': 'Tweet removed'}, status=200)


# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def tweet_action_view(request, *args, **kwargs):
#     '''
#     id is required.
#     Action options are: like,unlike,retweet
#     '''
#     serializer = TweetActionSerializer(data=request.data)
#     if serializer.is_valid(raise_exception=True):
#         data = serializer.validated_data
#         tweet_id = data.get('id')
#         action = data.get('action')
#         content = data.get('content')
#         qs = Tweet.objects.filter(id=tweet_id)
#         if not qs.exists():
#             return Response({}, status=404)
#         obj = qs.first()
#         if action == 'like':
#             obj.likes.add(request.user)
#         elif action == 'unlike':
#             obj.likes.remove(request.user)
#         elif action == 'retweet':
#             parent_obj = obj
#             new_tweet = Tweet.objects.create(
#                 user=request.user, parent=parent_obj, content=content)
#             serializer = TweetSerializer(new_tweet)
#             return Response(serializer.data, status=200)
#     return Response({}, status=200)


# def tweet_view(request, tweet_id, *args, **kwargs):
#     '''
#     REST API VIEW
#     Consume by javascript or Swift/java.ios.android
#     return json data
#     '''
#     print(args, kwargs)
#     data = {
#         'id': tweet_id,
#     }
#     status = 200
#     try:
#         obj = Tweet.objects.get(id=tweet_id)
#         data['content'] = obj.content
#     except:
#         data['message'] = 'Not Found'
#         status = 404

#     return JsonResponse(data, status=status)
#     # return HttpResponse(f'<h1>Hello {tweet_id}-{obj.content}</h1>')

# # Consition if user is not authenticated and he trys to tweet

# # if not request.user.is_authenticated:
# #     if request.is_ajax():
# #         return JsonResponse({},status=401)
# #     return redirect(settings.LOGIN_URL)


# # obj.user=request.user or None
